"""Kiểm hành vi của các phần TỰ CÀI ĐẶT (đề mục 2.4) bằng nguồn tham chiếu độc lập.

Khi một hàm còn là stub (NotImplementedError) test được SKIP, không đỏ. Cài xong thì test tự chạy.
Các test chỉ kiểm tính đúng (hội tụ, khớp tham chiếu, gradient), KHÔNG chứa lời giải của đề.
"""
import numpy as np
import pytest

from src import features as ft
from src import hand_calc as hc
from src import mlp as nn
from src import optim_linear as ol
from src import perceptron as pc


def _call(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except NotImplementedError:
        pytest.skip(f"chưa cài đặt: {getattr(fn, '__qualname__', fn)}")


def _regression_data(n=200, seed=0):
    rng = np.random.default_rng(seed)
    X = np.c_[rng.normal(size=(n, 3)), np.ones(n)]
    w_true = np.array([1.0, -2.0, 0.5, 3.0])
    return X, X @ w_true + 0.01 * rng.normal(size=n)


# ---------------------------------------------------------------- B3
def test_b3_grad_matches_central_finite_difference_of_own_loss():
    X, y = _regression_data()
    w = np.array([0.3, -0.1, 0.2, 0.5])
    g = _call(ol.mse_l2_grad, w, X, y, 0.1)
    num = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w)
        e[i] = 1e-6
        num[i] = (_call(ol.mse_l2_loss, w + e, X, y, 0.1) - ol.mse_l2_loss(w - e, X, y, 0.1)) / 2e-6
    assert np.linalg.norm(g - num) / max(np.linalg.norm(g), 1e-12) < 1e-6


def test_b3_ridge_closed_form_is_stationary_point_of_own_loss():
    X, y = _regression_data()
    w = _call(ol.ridge_closed_form, X, y, 0.1)
    assert np.linalg.norm(ol.mse_l2_grad(w, X, y, 0.1)) < 1e-8


def test_b3_gd_converges_to_least_squares_when_no_regularization():
    X, y = _regression_data()
    w, hist = _call(ol.gd, X, y, lam=0.0, eta=0.1, n_iter=3000)
    assert np.allclose(w, np.linalg.lstsq(X, y, rcond=None)[0], atol=1e-3)
    assert hist[-1] <= hist[0]


def test_b3_gd_converges_to_own_closed_form_with_l2():
    X, y = _regression_data()
    w_cf = _call(ol.ridge_closed_form, X, y, 0.1)
    w, _ = _call(ol.gd, X, y, lam=0.1, eta=0.1, n_iter=3000)
    assert np.allclose(w, w_cf, atol=1e-3)


# ---------------------------------------------------------------- B4
def _blobs(n=60, gap=4.0, flip=0.0, seed=0):
    rng = np.random.default_rng(seed)
    X = np.r_[rng.normal(-gap / 2, 1, size=(n, 2)), rng.normal(gap / 2, 1, size=(n, 2))]
    y = np.r_[-np.ones(n), np.ones(n)]
    if flip:
        idx = rng.choice(len(y), int(flip * len(y)), replace=False)
        y[idx] *= -1
    return np.c_[X, np.ones(len(y))], y


def test_b4_pla_reaches_zero_errors_on_separable_data():
    X, y = _blobs(gap=10.0)
    w, errs = _call(pc.pla, X, y, max_epochs=500, shuffle=False, seed=0)
    assert errs[-1] == 0
    assert np.all(y * (X @ w) > 0)  # quy ước: y·g <= 0 là sai, kể cả g = 0


def test_b4_pocket_is_never_worse_than_last_pla_iterate():
    X, y = _blobs(gap=1.0, flip=0.15)
    w_last, _ = _call(pc.pla, X, y, max_epochs=50, shuffle=False, seed=0)
    w_best, _ = _call(pc.pocket, X, y, max_epochs=50, shuffle=False, seed=0)
    assert pc.count_errors(w_best, X, y) <= pc.count_errors(w_last, X, y)


# ---------------------------------------------------------------- B5
def test_b5_gradient_check_passes_on_deep_net():
    rng = np.random.default_rng(1)
    X, y = rng.normal(size=(8, 3)), rng.normal(size=(8, 1))
    net = _call(nn.MLP, [3, 5, 4, 1], hidden="tanh", seed=1)
    errs = _call(net.grad_check, X, y)
    assert max(errs.values()) <= 1e-6, errs


def test_b5_training_reduces_loss():
    rng = np.random.default_rng(2)
    X = rng.normal(size=(64, 3))
    y = np.sin(X[:, :1]) + 0.1 * X[:, 1:2]
    net = _call(nn.MLP, [3, 8, 1], hidden="tanh", seed=2)
    before = net.loss(X, y)
    _call(net.fit, X, y, lr=0.05, epochs=200, batch_size=16)
    assert net.loss(X, y) < before


# ---------------------------------------------------------------- B6
def test_b6_pca_eigenvalues_match_sklearn():
    from sklearn.decomposition import PCA

    rng = np.random.default_rng(3)
    X = rng.normal(size=(100, 5)) @ rng.normal(size=(5, 5))
    res = _call(ft.pca, X, 3)
    ref = PCA(n_components=3).fit(X)
    assert np.allclose(res["eigvals"], ref.explained_variance_, atol=1e-6)
    overlap = np.abs(np.sum(res["components"] * ref.components_, axis=1))
    assert np.allclose(overlap, 1.0, atol=1e-6)  # trùng hướng, chấp nhận khác dấu


def test_b6_lda_two_class_direction_is_sw_inverse_times_mean_difference():
    rng = np.random.default_rng(4)
    X0 = rng.normal([0, 0, 0], [1, 2, 0.5], size=(80, 3))
    X1 = rng.normal([2, 1, 0], [1, 2, 0.5], size=(80, 3))
    X, y = np.r_[X0, X1], np.r_[np.zeros(80), np.ones(80)]
    w = _call(ft.lda_two_class, X, y)
    sw = sum(((c - c.mean(0)).T @ (c - c.mean(0))) for c in (X0, X1))
    ref = np.linalg.solve(sw, X1.mean(0) - X0.mean(0))
    ref /= np.linalg.norm(ref)
    assert abs(float(np.dot(w / np.linalg.norm(w), ref))) > 1 - 1e-6


# ---------------------------------------------------------------- B7 (đoạn mã chọn mẫu do đề cho sẵn)
def test_b7_six_samples_alternate_and_are_reproducible():
    y_train = np.r_[np.ones(40), -np.ones(160)][np.random.default_rng(0).permutation(200)]
    idx = hc.select_six_samples(y_train, seed=2033)
    assert [int(y_train[i] == 1) for i in idx] == [1, 0, 1, 0, 1, 0]
    assert len(set(idx)) == 6
    assert idx == hc.select_six_samples(y_train, seed=2033)
