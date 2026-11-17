"""Kiểm các quyết định đã chốt ngày 17/11/2026 (docs/CONVENTIONS.md mục 7)."""
from __future__ import annotations

from src import config, guards


def test_run_seeds_are_consecutive_from_seed():
    seeds = config.get_run_seeds()
    assert seeds == [config.get_seed() + i for i in range(config.N_RUN_SEEDS)]
    assert len(seeds) >= 5  # đề B4.3: ít nhất 5 hạt giống


def test_bootstrap_meets_spec():
    assert config.BOOTSTRAP_ITERS >= 1000  # đề B9.1
    assert 0.0 < config.BOOTSTRAP_CI < 1.0


def test_feature_lags_respect_72h_rule():
    assert all(guards.is_lag_valid(lag) for lag in config.FEATURE_LAGS_HOURS)
    assert min(config.FEATURE_LAGS_HOURS) >= guards.min_safe_lag()
    assert config.FEATURE_LAGS_HOURS[0] == config.BASELINE_LAG_HOURS


def test_tref_quantiles_are_valid_and_sorted():
    q = config.TREF_QUANTILES
    assert list(q) == sorted(q) and all(0.0 < v < 1.0 for v in q)
