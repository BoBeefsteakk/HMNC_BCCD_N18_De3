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
