"""Test bổ sung cho B6 (T007): ví dụ nhỏ tính tay được và quy ước dấu PCA.

Bổ sung cho tests/test_interfaces.py (test_b6_*), không thay thế.
"""
import numpy as np
import pytest

from src import features as ft


def test_fisher_score_matches_hand_calculation():
    # Lớp 0: x = 1, 2, 3 -> m0 = 2, s0^2 = (1 + 0 + 1)/3 = 2/3
    # Lớp 1: x = 5, 7    -> m1 = 6, s1^2 = (1 + 1)/2 = 1
    # J = (6 - 2)^2 / (1 + 2/3) = 16 / (5/3) = 9.6
    x = np.array([1.0, 2.0, 3.0, 5.0, 7.0])
    y = np.array([-1, -1, -1, 1, 1])
    assert ft.fisher_score(x, y) == pytest.approx(9.6)


def test_fisher_score_label_coding_does_not_matter():
    rng = np.random.default_rng(0)
    x = rng.normal(size=50)
    y_pm = np.where(rng.random(50) < 0.3, 1, -1)
    assert ft.fisher_score(x, y_pm) == pytest.approx(ft.fisher_score(x, (y_pm + 1) // 2))
    assert ft.fisher_score(x, y_pm) == pytest.approx(ft.fisher_score(x, -y_pm))


def test_fisher_score_constant_feature():
    y = np.array([0, 0, 1, 1])
    assert ft.fisher_score(np.array([3.0, 3.0, 3.0, 3.0]), y) == 0.0
    assert ft.fisher_score(np.array([1.0, 1.0, 2.0, 2.0]), y) == np.inf


def test_fisher_score_rejects_non_binary_labels():
    with pytest.raises(ValueError):
        ft.fisher_score(np.arange(6.0), np.array([0, 1, 2, 0, 1, 2]))


def test_pca_sign_convention_and_ratios():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(40, 4)) @ rng.normal(size=(4, 4))
    res = ft.pca(X, 4)
    comps = res["components"]
    biggest = comps[np.arange(4), np.argmax(np.abs(comps), axis=1)]
    assert np.all(biggest > 0)
    assert np.allclose(comps @ comps.T, np.eye(4))  # trực chuẩn
    assert np.all(np.diff(res["eigvals"]) <= 0)  # giảm dần
    assert res["explained_ratio"].sum() == pytest.approx(1.0)  # k = d thì giải thích hết
    assert np.allclose(res["mean"], X.mean(axis=0))


def test_pca_two_points_hand_example():
    # Hai điểm (0, 0) và (2, 2): mean (1, 1), cov = [[2, 2], [2, 2]] (chia n - 1 = 1)
    # -> trị riêng 4 và 0, véc tơ riêng thứ nhất (1, 1)/sqrt(2).
    res = ft.pca(np.array([[0.0, 0.0], [2.0, 2.0]]), 1)
    assert res["eigvals"][0] == pytest.approx(4.0)
    assert np.allclose(res["components"][0], np.array([1.0, 1.0]) / np.sqrt(2.0))
    assert res["explained_ratio"][0] == pytest.approx(1.0)
