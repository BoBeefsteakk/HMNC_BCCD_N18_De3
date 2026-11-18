"""T001 – nạp dữ liệu, chia tuần, nhãn cao điểm. Phần lõi dùng dữ liệu giả (CI không có dữ liệu thật)."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src import config, data_prep

HPW = config.HOURS_PER_WEEK
N_WEEKS = sum(config.EXPECTED_WEEKS.values())


def _synthetic_raw(shift_labels_by_hours: int = 1, seed: int = 0) -> pd.DataFrame:
    """Bảng thô giả: đủ 286 tuần, nhãn là GIỜ KẾT THÚC như tệp thật (lệch +1 giờ so với giờ bắt đầu)."""
    start = pd.Timestamp(config.SPLITS["train"][0])
    hours_start = pd.date_range(start, periods=N_WEEKS * HPW, freq="h")
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({config.TIME_COL: hours_start + pd.Timedelta(hours=shift_labels_by_hours)})
    df[config.TARGET_COL] = rng.uniform(800, 1600, len(df))
    for c in config.WEATHER_COLS:
        df[c] = rng.normal(size=len(df))
    for c in config.CALENDAR_COLS:
        df[c] = 0
    return df


@pytest.fixture(scope="module")
def prepared() -> pd.DataFrame:
    return data_prep.parse_raw(_synthetic_raw())


# ------------------------------------------------------------------ tuần và chia tập
def test_week_starts_are_saturdays_and_match_expected_counts():
    for name, n in config.EXPECTED_WEEKS.items():
        starts = data_prep.week_starts(name)
        assert len(starts) == n
        assert (starts.day_of_week == 5).all()
        assert (starts.hour == 0).all()


def test_split_weeks_counts_and_complete_weeks(prepared):
    parts = data_prep.split_weeks(prepared)
    assert {k: v["week_idx"].nunique() for k, v in parts.items()} == config.EXPECTED_WEEKS
    for part in parts.values():
        assert (part.groupby("week_idx").size() == HPW).all()
        first = part[part["hour_in_week"] == 0][config.TIME_COL]
        assert (first.dt.day_of_week == 5).all() and (first.dt.hour == 0).all()
        assert part["hour_in_week"].between(0, HPW - 1).all()


def test_splits_are_disjoint_and_in_time_order(prepared):
    parts = data_prep.split_weeks(prepared)
    names = list(config.SPLITS)
    for a, b in zip(names, names[1:]):
        assert parts[a][config.TIME_COL].max() < parts[b][config.TIME_COL].min()
    assert sum(len(p) for p in parts.values()) == len(prepared)


def test_end_of_hour_labels_need_the_shift():
    """Nhãn giờ kết thúc mà không lùi 1 giờ thì chia tuần phải vỡ (đây là lý do có TIMESTAMP_SHIFT_HOURS)."""
    raw = _synthetic_raw()
    with pytest.raises(AssertionError):
        data_prep.split_weeks(data_prep.parse_raw(raw, shift_hours=0))


def test_shift_moves_first_label_to_saturday_midnight(prepared):
    assert prepared[config.TIME_COL].iloc[0] == pd.Timestamp(config.SPLITS["train"][0])
    assert prepared["datetime_raw"].iloc[0] == prepared[config.TIME_COL].iloc[0] + pd.Timedelta(hours=1)


# ------------------------------------------------------------------ kiểm thiếu/trùng giờ
def test_parse_raw_rejects_duplicate_hour():
    raw = _synthetic_raw()
    raw = pd.concat([raw, raw.iloc[[10]]], ignore_index=True)
    with pytest.raises(ValueError, match="trùng"):
        data_prep.parse_raw(raw)


def test_parse_raw_rejects_missing_hour():
    raw = _synthetic_raw().drop(index=[100]).reset_index(drop=True)
    with pytest.raises(ValueError, match="nhảy giờ"):
        data_prep.parse_raw(raw)


def test_parse_raw_rejects_missing_column():
    with pytest.raises(ValueError, match="Thiếu cột"):
        data_prep.parse_raw(_synthetic_raw().drop(columns=[config.TARGET_COL]))


def test_parse_raw_sorts_shuffled_rows():
    raw = _synthetic_raw().sample(frac=1.0, random_state=1)
    out = data_prep.parse_raw(raw)
    assert out[config.TIME_COL].is_monotonic_increasing


# ------------------------------------------------------------------ nhãn cao điểm
def test_peak_label_values_and_threshold_from_train_only():
    rng = np.random.default_rng(1)
    y = rng.uniform(0, 100, 1000)
    mask = np.zeros(1000, dtype=bool)
    mask[:600] = True
    lab = data_prep.peak_label(y, mask)
    assert set(np.unique(lab)) <= {-1, 1}
    thr = np.quantile(y[mask], config.PEAK_QUANTILE)
    assert np.array_equal(lab, np.where(y > thr, 1, -1))
    # xấp xỉ 10% mẫu train là cao điểm
    assert abs((lab[mask] == 1).mean() - (1 - config.PEAK_QUANTILE)) < 0.01


def test_peak_threshold_unchanged_when_val_test_data_changes():
    """Chứng minh không rò rỉ: đổi hẳn giá trị ngoài train thì ngưỡng và nhãn trên train không đổi."""
    rng = np.random.default_rng(2)
    y = rng.uniform(0, 100, 1000)
    mask = np.zeros(1000, dtype=bool)
    mask[:600] = True
    lab_a = data_prep.peak_label(y, mask)
    y2 = y.copy()
    y2[~mask] = y2[~mask] * 10 + 500  # val/test bị thay đổi mạnh
    lab_b = data_prep.peak_label(y2, mask)
    assert np.array_equal(lab_a[mask], lab_b[mask])
    assert data_prep.peak_threshold(y[mask]) == data_prep.peak_threshold(y2[mask])
    # val/test cao hơn ngưỡng nhiều nên toàn +1: ngưỡng không "học" từ chúng
    assert (lab_b[~mask] == 1).all()


def test_peak_label_validates_inputs():
    with pytest.raises(ValueError):
        data_prep.peak_label(np.arange(5.0), np.zeros(5, dtype=bool))
    with pytest.raises(ValueError):
        data_prep.peak_label(np.arange(5.0), np.ones(4, dtype=bool))


# ------------------------------------------------------------------ tuần khởi động
def test_warmup_weeks_follow_longest_lag():
    assert config.WARMUP_WEEKS * HPW >= max(config.FEATURE_LAGS_HOURS)
    assert (config.WARMUP_WEEKS - 1) * HPW < max(config.FEATURE_LAGS_HOURS)


def test_drop_warmup_removes_only_first_weeks_of_train(prepared):
    train = data_prep.split_weeks(prepared)["train"]
    kept = data_prep.drop_warmup(train)
    assert kept["week_idx"].min() == config.WARMUP_WEEKS
    assert len(kept) == len(train) - config.WARMUP_WEEKS * HPW
    assert kept["week_idx"].nunique() == config.EXPECTED_WEEKS["train"] - config.WARMUP_WEEKS


def test_warmup_leaves_enough_history_for_first_kept_week(prepared):
    """Tuần huấn luyện đầu tiên phải có đủ lịch sử cho trễ xa nhất trong chính dữ liệu (kể cả tuần đã bỏ)."""
    train = data_prep.split_weeks(prepared)["train"]
    first_kept = data_prep.drop_warmup(train)[config.TIME_COL].iloc[0]
    oldest_needed = first_kept - pd.Timedelta(hours=max(config.FEATURE_LAGS_HOURS))
    assert oldest_needed >= train[config.TIME_COL].iloc[0]


# ------------------------------------------------------------------ giờ phụ tải thấp
def test_low_load_hours_flags_below_half_of_train_median(prepared):
    df = prepared.copy()
    idx = [5, 6, 20000]
    df.loc[idx, config.TARGET_COL] = 10.0
    low = data_prep.low_load_hours(df)
    assert list(low.index) == idx
    assert (low["ratio_to_median"] < config.LOW_LOAD_FRACTION).all()


def test_low_load_hours_uses_given_reference(prepared):
    low = data_prep.low_load_hours(prepared, ref_median=1e9)
    assert len(low) == len(prepared)


# ------------------------------------------------------------------ dữ liệu thật (chỉ chạy khi có tệp)
real = pytest.mark.skipif(not data_prep.RAW_CONTINUOUS.exists(), reason="chưa có data/raw/continuous.csv")


@real
def test_real_data_loads_and_splits_into_expected_weeks():
    df = data_prep.load_raw()
    assert len(df) == N_WEEKS * HPW
    assert df[config.TIME_COL].iloc[0] == pd.Timestamp(config.SPLITS["train"][0])
    parts = data_prep.split_weeks(df)
    assert {k: v["week_idx"].nunique() for k, v in parts.items()} == config.EXPECTED_WEEKS
    assert df[config.TARGET_COL].notna().all()


@real
def test_real_data_peak_rate_on_train_is_about_ten_percent():
    parts = data_prep.split_weeks(data_prep.load_raw())
    y = parts["train"][config.TARGET_COL].to_numpy()
    lab = data_prep.peak_label(y, np.ones(len(y), dtype=bool))
    assert abs((lab == 1).mean() - (1 - config.PEAK_QUANTILE)) < 0.001


# ------------------------------------------------------------------ T002: căn dự báo CND
def _synthetic_cnd(prepared: pd.DataFrame, label_offset_hours: int, noise: float = 0.0, seed: int = 3) -> pd.DataFrame:
    """CND giả: dự báo = phụ tải thực (+ nhiễu), gắn nhãn lệch `label_offset_hours` so với nhãn giờ bắt đầu."""
    rng = np.random.default_rng(seed)
    y = prepared[config.TARGET_COL].to_numpy()
    fc = y * (1 + noise * rng.normal(size=len(y)))
    ts = prepared[config.TIME_COL] + pd.Timedelta(hours=label_offset_hours)
    return pd.DataFrame({"cnd_ts": ts.to_numpy(), data_prep.CND_COL: fc})


def test_load_cnd_parses_month_day_year_with_bom(tmp_path):
    p = tmp_path / "cnd.csv"
    p.write_text("\ufeffdatetime,load_forecast\n1/2/2016 0:00,1056.9\n1/2/2016 1:00,1057.1\n", encoding="utf-8")
    cnd = data_prep.load_cnd(p)
    assert cnd["cnd_ts"].iloc[0] == pd.Timestamp("2016-01-02 00:00")  # M/D: 2 tháng 1, Thứ Bảy
    assert cnd["cnd_ts"].iloc[0].day_of_week == 5
    assert list(cnd.columns) == ["cnd_ts", data_prep.CND_COL]


def test_load_cnd_rejects_duplicate_and_gap(tmp_path):
    dup = tmp_path / "dup.csv"
    dup.write_text("datetime,load_forecast\n1/2/2016 0:00,1\n1/2/2016 0:00,2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="trùng"):
        data_prep.load_cnd(dup)
    gap = tmp_path / "gap.csv"
    gap.write_text("datetime,load_forecast\n1/2/2016 0:00,1\n1/2/2016 2:00,2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="nhảy giờ"):
        data_prep.load_cnd(gap)


def test_align_cnd_matches_by_shifted_label(prepared):
    cnd = _synthetic_cnd(prepared, label_offset_hours=1)  # nhãn CND lớn hơn nhãn phụ tải 1 giờ
    aligned = data_prep.align_cnd(prepared, cnd, shift_hours=-1)
    assert np.allclose(aligned[data_prep.CND_COL], aligned[config.TARGET_COL])


def test_align_cnd_gives_nan_where_cnd_does_not_cover(prepared):
    cnd = _synthetic_cnd(prepared, 0).iloc[config.HOURS_PER_WEEK:]  # CND bắt đầu muộn 1 tuần
    aligned = data_prep.align_cnd(prepared, cnd, shift_hours=0)
    assert aligned[data_prep.CND_COL].iloc[: config.HOURS_PER_WEEK].isna().all()
    assert aligned[data_prep.CND_COL].iloc[config.HOURS_PER_WEEK :].notna().all()
    assert len(aligned) == len(prepared)


@pytest.mark.parametrize("offset", [-1, 0, 1])
def test_select_cnd_shift_recovers_known_label_offset(prepared, offset):
    """CND giả gắn nhãn lệch `offset` giờ -> độ dịch đúng là -offset, MAPE gần 0 ở đúng độ dịch đó."""
    val = data_prep.split_weeks(prepared)["val"]
    cnd = _synthetic_cnd(prepared, offset, noise=0.02)
    table = data_prep.select_cnd_shift(val, cnd)
    best = int(table.loc[table["mape"].idxmin(), "shift_hours"])
    assert best == -offset
    assert table["mape"].min() < 0.03 < table["mape"].max()


def test_select_cnd_shift_refuses_train_and_test_data(prepared):
    parts = data_prep.split_weeks(prepared)
    cnd = _synthetic_cnd(prepared, 0)
    for name in ("train", "test_a", "test_b"):
        with pytest.raises(ValueError, match="kiểm định"):
            data_prep.select_cnd_shift(parts[name], cnd)


def test_cnd_mape_is_mean_of_weekly_means(prepared):
    val = data_prep.split_weeks(prepared)["val"].copy()
    val[data_prep.CND_COL] = val[config.TARGET_COL] * 1.1
    ape = (val[config.TARGET_COL] - val[data_prep.CND_COL]).abs() / val[config.TARGET_COL]
    assert data_prep.cnd_mape(val) == pytest.approx(float(ape.mean()))  # tuần đủ giờ nên trung bình tuần = trung bình giờ
    assert data_prep.cnd_mape(val) == pytest.approx(0.1, rel=1e-9)


real_cnd = pytest.mark.skipif(
    not (data_prep.RAW_CONTINUOUS.exists() and data_prep.RAW_CND.exists()), reason="chưa có tệp phụ tải và CND trong data/raw"
)


@real_cnd
def test_real_cnd_best_shift_on_validation_matches_config():
    df = data_prep.load_raw()
    val = data_prep.split_weeks(df)["val"]
    table = data_prep.select_cnd_shift(val, data_prep.load_cnd())
    best = int(table.loc[table["mape"].idxmin(), "shift_hours"])
    assert best == config.CND_SHIFT_HOURS
    assert (table["n_hours"] == len(val)).all()  # CND phủ trọn tập kiểm định
