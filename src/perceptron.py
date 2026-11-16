"""B4 – PLA và Pocket trên bài toán phụ "giờ cao điểm cần cảnh báo" (y = +1 / -1).

Khối chấm: B4.1–B4.4.
TỰ CÀI ĐẶT bằng NumPy (đề mục 2.4). Quy ước BẮT BUỘC nêu trong báo cáo (B4.1):
  nhãn ±1; véc tơ mở rộng x̃ = (x, 1); khởi tạo w̃ = 0; mẫu có y·g <= 0 là SAI (kể cả g = 0);
  nêu rõ thứ tự duyệt và điều kiện dừng.

Giao diện (tests/test_interfaces.py kiểm):
  count_errors(w, X, y) -> int                                   # số mẫu y*g <= 0
  pla(X, y, max_epochs=100, shuffle=False, seed=0) -> (w_last, errors_per_epoch)
  pocket(X, y, max_epochs=100, shuffle=False, seed=0) -> (w_best, errors_per_epoch)
  check_separable_lp(X, y) -> bool      # B4.2: bài toán quy hoạch tuyến tính khả thi [3, §8.6.1] với scipy.optimize.linprog
"""
from __future__ import annotations

import numpy as np  # noqa: F401


def count_errors(w, X, y):
    raise NotImplementedError("B4: count_errors")


def pla(X, y, max_epochs=100, shuffle=False, seed=0):
    raise NotImplementedError("B4: pla")


def pocket(X, y, max_epochs=100, shuffle=False, seed=0):
    raise NotImplementedError("B4: pocket")


def check_separable_lp(X, y):
    raise NotImplementedError("B4: check_separable_lp")


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B4.2–B4.4: khả tách (LP), lỗi theo epoch, >= 5 hạt giống, vùng quyết định 2 đặc trưng."""
    raise NotImplementedError("B4: perceptron")
