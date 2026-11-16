"""B3 – GD theo lô, SGD, mini-batch, momentum cho HỒI QUY TUYẾN TÍNH (MSE + L2).

Khối chấm: B3.1–B3.4, câu hỏi nghiên cứu (3).
TỰ CÀI ĐẶT bằng NumPy; KHÔNG dùng sklearn/autograd cho phần lõi (đề mục 2.4). Mã tham khảo phải ghi nguồn ngay tại chỗ.

Quy ước mặc định (nhóm có thể đổi, nhưng phải ghi quyết định và sửa báo cáo cho khớp):
  X là ma trận đã mở rộng X̃ = [X, 1] (cột 1 ở cuối); w có d+1 phần tử, hệ số tự do là phần tử cuối.
  J(w) = 1/(2n) * ||X̃ w - y||^2 + (lam/2) * ||w[:-1]||^2        (KHÔNG phạt hệ số tự do)
  grad = 1/n * X̃ᵀ(X̃ w - y) + lam * [w[:-1], 0]

Giao diện (tests/test_interfaces.py kiểm các hàm này; đổi tên thì sửa test cùng PR):
  mse_l2_loss(w, X, y, lam) -> float
  mse_l2_grad(w, X, y, lam) -> ndarray
  gd(X, y, lam, eta, n_iter, w0=None) -> (w, loss_history)
  sgd(X, y, lam, eta, n_epochs, seed) -> (w, loss_history)                       # mỗi mẫu một lần cập nhật
  minibatch_gd(X, y, lam, eta, n_epochs, batch_size, seed) -> (w, loss_history)
  momentum_gd(X, y, lam, eta, beta, n_iter, w0=None) -> (w, loss_history)        # khuyến khích thêm Nesterov/Adam
  ridge_closed_form(X, y, lam) -> w                                              # đối chiếu B3.4b
  finite_diff_check(loss_fn, grad_fn, w, eps=1e-6) -> float                      # sai số tương đối, yêu cầu <= 1e-6 (float64)
"""
from __future__ import annotations

import numpy as np  # noqa: F401


def mse_l2_loss(w, X, y, lam):
    raise NotImplementedError("B3: mse_l2_loss")


def mse_l2_grad(w, X, y, lam):
    raise NotImplementedError("B3: mse_l2_grad")


def gd(X, y, lam, eta, n_iter, w0=None):
    raise NotImplementedError("B3: gd")


def sgd(X, y, lam, eta, n_epochs, seed):
    raise NotImplementedError("B3: sgd")


def minibatch_gd(X, y, lam, eta, n_epochs, batch_size, seed):
    raise NotImplementedError("B3: minibatch_gd")


def momentum_gd(X, y, lam, eta, beta, n_iter, w0=None):
    raise NotImplementedError("B3: momentum_gd")


def ridge_closed_form(X, y, lam):
    raise NotImplementedError("B3: ridge_closed_form")


def finite_diff_check(loss_fn, grad_fn, w, eps=1e-6):
    raise NotImplementedError("B3: finite_diff_check")


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B3.2–B3.4: so GD/momentum, quét η (>= 4 giá trị theo log), z-score vs không chuẩn hóa."""
    raise NotImplementedError("B3: optim_linear")
