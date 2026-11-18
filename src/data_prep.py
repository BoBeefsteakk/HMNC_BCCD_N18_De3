"""B1 – đọc, làm sạch, chia dữ liệu theo tuần Thứ Bảy -> Thứ Sáu.

Khối chấm: B1.2, B1.4 (+ nền cho mọi khối khác).
Đầu vào: data/raw/continuous.csv, data/raw/forecast_cnd.csv  (tải tay, kiểm bằng python data/download_data.py)
Quy định (đề mục 4.4d): chia theo thời gian, KHÔNG xáo trộn; số tuần phải khớp config.EXPECTED_WEEKS.

Hàm (T001 làm các hàm đầu; align_cnd thuộc T002):
  parse_raw(df, shift_hours)  chuẩn hóa nhãn thời gian về "giờ bắt đầu", kiểm thiếu/trùng giờ
  load_raw(path)              đọc CSV rồi gọi parse_raw
  week_starts(split)          các thời điểm Thứ Bảy 00:00 của từng tuần trong một split
  split_weeks(df)             {train, val, test_a, test_b} -> DataFrame (thêm week_idx, hour_in_week); assert số tuần
  peak_threshold / peak_label nhãn +1/-1 "giờ cao điểm": ngưỡng = phân vị 90% TÍNH TRÊN TẬP HUẤN LUYỆN
  drop_warmup(train)          bỏ tuần khởi động (config.WARMUP_WEEKS) khi huấn luyện
  low_load_hours(df, ref)     liệt kê giờ có phụ tải < 50% trung vị của train
  align_cnd(...)              (T002) căn dự báo CND với phụ tải thực
Lưu ý rò rỉ: mọi phép "học" (ngưỡng phân vị, trung vị tham chiếu, chuẩn hóa) chỉ khớp trên train (đề mục 3.1d).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from . import config

RAW_CONTINUOUS = config.RAW_DIR / config.DATA_FILES["continuous"]["local_name"]


def parse_raw(df: pd.DataFrame, shift_hours: int = config.TIMESTAMP_SHIFT_HOURS) -> pd.DataFrame:
    """Chuẩn hóa bảng thô: datetime về giờ bắt đầu, sắp theo thời gian, kiểm trùng/thiếu giờ.

    Trùng giờ hoặc thiếu giờ -> ValueError (dữ liệu của đề không có cả hai; nếu sau này có thì phải quyết cách
    xử lý, không được lặng lẽ bỏ qua). Giữ nhãn gốc ở cột `datetime_raw`.
    """
    need = [config.TIME_COL, config.TARGET_COL, *config.WEATHER_COLS, *config.CALENDAR_COLS]
    missing_cols = [c for c in need if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Thiếu cột: {missing_cols}")
    out = df.copy()
    out[config.TIME_COL] = pd.to_datetime(out[config.TIME_COL])
    out = out.sort_values(config.TIME_COL).reset_index(drop=True)
    out.insert(1, "datetime_raw", out[config.TIME_COL])
    out[config.TIME_COL] = out[config.TIME_COL] + pd.Timedelta(hours=shift_hours)

    dup = int(out[config.TIME_COL].duplicated().sum())
    if dup:
        raise ValueError(f"Có {dup} dòng trùng giờ")
    gaps = out[config.TIME_COL].diff().dropna()
    bad = gaps[gaps != pd.Timedelta(hours=1)]
    if len(bad):
        raise ValueError(f"Có {len(bad)} chỗ nhảy giờ khác 1 giờ, đầu tiên tại {out.loc[bad.index[0], config.TIME_COL]}")
    return out


def load_raw(path: Path | str = RAW_CONTINUOUS, shift_hours: int = config.TIMESTAMP_SHIFT_HOURS) -> pd.DataFrame:
    """Đọc continuous.csv rồi `parse_raw`."""
    return parse_raw(pd.read_csv(path), shift_hours=shift_hours)


def week_starts(split: str) -> pd.DatetimeIndex:
    """Thứ Bảy 00:00 của từng tuần trong `split`, tính từ config.SPLITS (không đọc dữ liệu)."""
    start, end = (pd.Timestamp(s) for s in config.SPLITS[split])
    n_days = (end - start).days + 1
    return pd.date_range(start, periods=n_days // 7, freq="7D")


def split_weeks(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Chia df (đã qua parse_raw) thành train/val/test_a/test_b theo tuần; assert đủ số tuần và đủ 168 giờ/tuần.

    Thêm hai cột: `week_idx` (0.. trong split) và `hour_in_week` (0 = Thứ Bảy 00:00 ... 167 = Thứ Sáu 23:00).
    Giờ nằm ngoài mọi split (nếu có) bị loại và được báo qua assert tổng số giờ.
    """
    t = df[config.TIME_COL]
    out: dict[str, pd.DataFrame] = {}
    for name in config.SPLITS:
        starts = week_starts(name)
        lo = starts[0]
        hi = starts[-1] + pd.Timedelta(hours=config.HOURS_PER_WEEK)
        part = df[(t >= lo) & (t < hi)].copy()
        n_weeks = config.EXPECTED_WEEKS[name]
        assert len(starts) == n_weeks, f"{name}: lịch cho {len(starts)} tuần, đề cần {n_weeks}"
        assert len(part) == n_weeks * config.HOURS_PER_WEEK, (
            f"{name}: {len(part)} giờ, cần {n_weeks * config.HOURS_PER_WEEK} (kiểm config.TIMESTAMP_SHIFT_HOURS)"
        )
        pt = part[config.TIME_COL]
        part["week_idx"] = ((pt - lo).dt.days // 7).astype(int)
        part["hour_in_week"] = (((pt.dt.day_of_week - 5) % 7) * 24 + pt.dt.hour).astype(int)
        assert (part.groupby("week_idx").size() == config.HOURS_PER_WEEK).all(), f"{name}: có tuần không đủ giờ"
        assert (part.groupby("week_idx")["hour_in_week"].apply(lambda s: s.is_monotonic_increasing)).all()
        out[name] = part.reset_index(drop=True)
    return out


def peak_threshold(y_train: np.ndarray) -> float:
    """Ngưỡng cao điểm = phân vị `config.PEAK_QUANTILE` (nội suy tuyến tính của NumPy) của phụ tải TẬP HUẤN LUYỆN."""
    return float(np.quantile(np.asarray(y_train, dtype=np.float64), config.PEAK_QUANTILE))


def peak_label(y: np.ndarray, train_mask: np.ndarray) -> np.ndarray:
    """Nhãn +1 nếu y > ngưỡng cao điểm, ngược lại -1. Ngưỡng chỉ tính từ `y[train_mask]` (không rò rỉ val/test)."""
    y = np.asarray(y, dtype=np.float64)
    train_mask = np.asarray(train_mask, dtype=bool)
    if y.shape != train_mask.shape:
        raise ValueError("y và train_mask phải cùng kích thước")
    if not train_mask.any():
        raise ValueError("train_mask rỗng: không có dữ liệu huấn luyện để tính ngưỡng")
    return np.where(y > peak_threshold(y[train_mask]), 1, -1)


def low_load_hours(df: pd.DataFrame, ref_median: float | None = None) -> pd.DataFrame:
    """Giờ có phụ tải < `config.LOW_LOAD_FRACTION` x trung vị. Trung vị mặc định tính trên train (đúng tuần, theo split_weeks).

    Chỉ liệt kê, KHÔNG xóa: việc xử lý (giữ, hay báo MAPE có/không các giờ này) do nhóm quyết, ghi ở task.
    """
    if ref_median is None:
        t = df[config.TIME_COL]
        lo = week_starts("train")[0]
        hi = week_starts("train")[-1] + pd.Timedelta(hours=config.HOURS_PER_WEEK)
        ref_median = float(df.loc[(t >= lo) & (t < hi), config.TARGET_COL].median())
    flagged = df[df[config.TARGET_COL] < config.LOW_LOAD_FRACTION * ref_median]
    return flagged[[config.TIME_COL, config.TARGET_COL]].assign(ratio_to_median=lambda d: d[config.TARGET_COL] / ref_median)


def drop_warmup(train: pd.DataFrame) -> pd.DataFrame:
    """Bỏ `config.WARMUP_WEEKS` tuần đầu của train khi HUẤN LUYỆN (chúng chưa đủ lịch sử cho trễ xa nhất).

    Chỉ dùng cho tập học; khi tính đặc trưng trễ, các tuần đó vẫn được dùng làm lịch sử cho tuần sau.
    """
    return train[train["week_idx"] >= config.WARMUP_WEEKS].reset_index(drop=True)


def split_of(ts: pd.Timestamp) -> str:
    """Tên split chứa thời điểm `ts` (giờ bắt đầu), hoặc 'ngoài' nếu không thuộc split nào."""
    for name in config.SPLITS:
        starts = week_starts(name)
        if starts[0] <= ts < starts[-1] + pd.Timedelta(hours=config.HOURS_PER_WEEK):
            return name
    return "ngoài"


def run(seed: int, final: bool = False) -> None:
    """Đọc, chia tuần, in tóm tắt (chưa sinh bảng/hình; EDA là T005)."""
    df = load_raw()
    parts = split_weeks(df)
    for name, part in parts.items():
        print(f"{name:7s} {part['week_idx'].nunique():3d} tuần  {len(part):6d} giờ  {part[config.TIME_COL].min()} -> {part[config.TIME_COL].max()}")
    train_y = parts["train"][config.TARGET_COL].to_numpy()
    print(f"ngưỡng cao điểm (phân vị {config.PEAK_QUANTILE:.0%} của train): {peak_threshold(train_y):.2f} MWh")
    low = low_load_hours(df)
    print(f"giờ phụ tải < {config.LOW_LOAD_FRACTION:.0%} trung vị train: {len(low)}")
    for _, r in low.iterrows():
        print(f"  {r[config.TIME_COL]}  {r[config.TARGET_COL]:8.2f} MWh  {r['ratio_to_median']:.0%}  [{split_of(r[config.TIME_COL])}]")
