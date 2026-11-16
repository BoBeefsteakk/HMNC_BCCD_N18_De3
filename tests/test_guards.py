"""Quy tắc 72 giờ (R1) và khóa tập kiểm tra (đề mục 3.1d, 6.4)."""
import pytest

from src import guards


def test_min_safe_lag_is_240_hours():
    # Thứ Ba 23:00 -> Thứ Bảy 00:00 cách 73 giờ; giờ cuối tuần dự báo (Thứ Sáu 23:00) cách thêm 167 giờ.
    assert guards.min_safe_lag() == 240


@pytest.mark.parametrize("lag", [24, 72, 168, 239])
def test_short_lags_are_invalid_for_whole_week(lag):
    assert not guards.is_lag_valid(lag)


@pytest.mark.parametrize("lag", [240, 336, 504, 672])
def test_weekly_multiples_from_two_weeks_are_valid(lag):
    assert guards.is_lag_valid(lag)


def test_lag_168_is_only_partly_valid():
    # Hợp lệ cho Thứ Bảy..Thứ Ba (giờ 0..95), rò rỉ cho Thứ Tư..Thứ Sáu.
    assert guards.valid_hours_for_lag(168) == 96
    assert guards.is_lag_valid(168, hour_in_week=95)
    assert not guards.is_lag_valid(168, hour_in_week=96)


def test_lag_24_is_never_valid():
    assert guards.valid_hours_for_lag(24) == 0


def test_lag_violations_report():
    table = {"L_h-336": 336, "L_h-168": 168, "L_h-24": 24}
    bad = guards.lag_violations(table)
    assert len(bad) == 2 and any("168" in b for b in bad) and not any("336" in b for b in bad)


def test_test_set_needs_final_flag(tmp_path):
    with pytest.raises(guards.TestSetLockError):
        guards.open_test_set(final=False, lock_path=tmp_path / "lock")


def test_test_set_opens_only_once(tmp_path):
    lock = tmp_path / "lock"
    guards.open_test_set(final=True, lock_path=lock)
    assert lock.exists()
    with pytest.raises(guards.TestSetLockError):
        guards.open_test_set(final=True, lock_path=lock)
