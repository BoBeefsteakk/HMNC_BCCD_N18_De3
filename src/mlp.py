"""B5 – MLP hồi quy bằng NumPy: lan truyền thuận/ngược (BP1–BP4), cập nhật mini-batch, kiểm tra gradient.

Khối chấm: B5.1–B5.5 (2,0 điểm — khối lớn nhất).
Đề 3: tầng ra TUYẾN TÍNH + MSE; chuẩn hóa biến mục tiêu (khớp trên train); mỗi giờ cần dự báo là một mẫu.
KHÔNG dùng autograd (đề mục 2.4). sklearn MLPRegressor / PyTorch chỉ để ĐỐI CHỨNG (B5.5).

Giao diện (tests/test_interfaces.py kiểm):
  MLP(layer_sizes, hidden="tanh"|"sigmoid"|"relu", init="xavier"|"he"|"zeros", seed=0)   # >= 2 hàm kích hoạt ẩn
  .forward(X) -> y_hat           .loss(X, y) -> float (MSE, có thể + L2)
  .backward(X, y) -> grads       # theo δ(l)
  .fit(X, y, lr, epochs, batch_size, optimizer="sgd"|"momentum", l2=0.0)
  .predict(X)
  .grad_check(X, y, eps=1e-6) -> dict[tên ma trận trọng số -> sai số tương đối]   # <= 1e-6 (float64), >= 2 kiến trúc, 1 kiến trúc >= 2 tầng ẩn
"""
from __future__ import annotations

import numpy as np  # noqa: F401


class MLP:
    def __init__(self, layer_sizes, hidden="tanh", init="xavier", seed=0):
        raise NotImplementedError("B5: MLP.__init__")


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B5.3–B5.5: kiến trúc (>= 3 cấu hình), khởi tạo 0 vs Xavier/He, sigmoid sâu, SGD vs momentum, L2/dừng sớm."""
    raise NotImplementedError("B5: mlp")
