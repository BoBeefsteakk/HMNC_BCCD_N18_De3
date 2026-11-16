"""Cách chia dữ liệu của đề (mục 4.4d) và công thức SEED (mục 2.1) — kiểm bằng số học lịch, không cần dữ liệu."""
from datetime import date, timedelta

import pytest

from src import config


def _d(s: str) -> date:
    return date.fromisoformat(s)


@pytest.mark.parametrize("name", list(config.SPLITS))
def test_split_is_whole_saturday_to_friday_weeks(name):
    start, end = map(_d, config.SPLITS[name])
    assert start.weekday() == 5, f"{name} phải bắt đầu Thứ Bảy"
    assert end.weekday() == 4, f"{name} phải kết thúc Thứ Sáu"
    n_days = (end - start).days + 1
    assert n_days % 7 == 0
    assert n_days // 7 == config.EXPECTED_WEEKS[name]


def test_splits_are_contiguous_and_ordered():
    order = ["train", "val", "test_a", "test_b"]
    for prev, nxt in zip(order, order[1:]):
        assert _d(config.SPLITS[nxt][0]) == _d(config.SPLITS[prev][1]) + timedelta(days=1)


def test_expected_week_counts_match_assignment():
    assert config.EXPECTED_WEEKS == {"train": 209, "val": 26, "test_a": 37, "test_b": 14}


def test_seed_formula_matches_assignment_example():
    assert config.seed_for(7) == 2033  # ví dụ nhóm 07 trong đề mục 2.1


def test_seed_refuses_to_guess_group(monkeypatch):
    monkeypatch.setattr(config, "GROUP_ID", None)
    with pytest.raises(RuntimeError):
        config.get_seed()


def test_weather_columns_are_twelve():
    assert len(config.WEATHER_COLS) == 12  # "PCA trên 12 biến thời tiết" (đề mục 4.4d)
