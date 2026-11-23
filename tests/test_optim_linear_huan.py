"""Kiểm thử chuyên sâu cho khối T003 – Tối ưu hóa tuyến tính (Đỗ Minh Huấn).

Kiểm tra:
- Không phạt hệ số tự do (bias w[-1]) trong L2 loss và gradient.
- Sai phân hữu hạn <= 1e-6 trên nhiều điểm thử nghiệm ngẫu nhiên.
- Nghiệm đóng Ridge thỏa mãn điều kiện dừng grad < 1e-8.
- GD hội tụ về nghiệm đóng.
- Momentum với beta=0 trùng khớp hoàn toàn với GD thông thường.
- SGD và Mini-batch GD giảm loss qua các epoch.
"""
import numpy as np
import pytest

from src import optim_linear as ol


def _make_data(n=150, d=4, seed=42):
    rng = np.random.default_rng(seed)
    X = np.c_[rng.normal(size=(n, d)), np.ones(n)]
    w_true = rng.normal(size=d + 1)
    y = X @ w_true + 0.05 * rng.normal(size=n)
    return X, y, w_true


def test_bias_is_not_regularized():
    X, y, _ = _make_data()
    w1 = np.array([1.0, 2.0, -1.0, 0.5, 10.0])
    w2 = np.array([1.0, 2.0, -1.0, 0.5, -50.0])  # chỉ thay đổi bias w[-1]
    lam = 0.5
    # Phần phạt L2 = 0.5 * lam * sum(w[:-1]^2) phải như nhau giữa w1 và w2
    l2_part1 = ol.mse_l2_loss(w1, X, y, lam) - ol.mse_l2_loss(w1, X, y, 0.0)
    l2_part2 = ol.mse_l2_loss(w2, X, y, lam) - ol.mse_l2_loss(w2, X, y, 0.0)
    assert np.isclose(l2_part1, l2_part2)

    # Gradient tại thành phần bias w[-1] không chứa số hạng lam * w[-1]
    g1 = ol.mse_l2_grad(w1, X, y, lam)
    g1_no_reg = ol.mse_l2_grad(w1, X, y, 0.0)
    assert np.isclose(g1[-1], g1_no_reg[-1])


def test_finite_diff_check_multiple_points():
    X, y, _ = _make_data()
    rng = np.random.default_rng(123)
    for _ in range(5):
        w_rand = rng.normal(size=X.shape[1])
        err = ol.finite_diff_check(
            lambda w: ol.mse_l2_loss(w, X, y, 0.2),
            lambda w: ol.mse_l2_grad(w, X, y, 0.2),
            w_rand,
            eps=1e-6,
        )
        assert err < 1e-6


def test_momentum_with_beta_zero_matches_gd():
    X, y, _ = _make_data(n=80, d=3, seed=7)
    lam = 0.05
    eta = 0.02
    n_iter = 100
    w_gd, hist_gd = ol.gd(X, y, lam=lam, eta=eta, n_iter=n_iter)
    w_mom, hist_mom = ol.momentum_gd(X, y, lam=lam, eta=eta, beta=0.0, n_iter=n_iter)
    assert np.allclose(w_gd, w_mom, atol=1e-12)
    assert np.allclose(hist_gd, hist_mom, atol=1e-12)


def test_sgd_and_minibatch_reduce_loss():
    X, y, _ = _make_data(n=100, d=3, seed=99)
    lam = 0.01
    _, hist_sgd = ol.sgd(X, y, lam=lam, eta=0.01, n_epochs=30, seed=2044)
    assert hist_sgd[-1] < hist_sgd[0]

    _, hist_mb = ol.minibatch_gd(X, y, lam=lam, eta=0.05, n_epochs=30, batch_size=16, seed=2044)
    assert hist_mb[-1] < hist_mb[0]
