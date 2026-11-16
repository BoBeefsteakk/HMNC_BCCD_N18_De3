"""B6 – đặc trưng, PCA và LDA tự cài đặt, chọn đặc trưng.

Khối chấm: B6.1–B6.5, R4 (PCA đồ thị ngày, LDA loại ngày), câu hỏi nghiên cứu (2).
PCA (trị riêng của ma trận hiệp phương sai hoặc SVD) và LDA (Fisher) PHẢI tự cài đặt bằng NumPy (đề mục 2.4).
sklearn.decomposition.PCA chỉ để ĐỐI CHỨNG (trị riêng khớp thư viện đến 1e-6, B6.3).

Giao diện (tests/test_interfaces.py kiểm):
  pca(X, k) -> dict(mean, components[k, d], eigvals[k], explained_ratio[k])      # hiệp phương sai chia n-1
  lda_two_class(X, y) -> w                                                       # w ∝ S_W^{-1}(m1 - m0), chuẩn hóa ||w|| = 1
  lda_multiclass(X, y, k) -> W                                                   # S_W^{-1} S_B, cho 3 loại ngày ở R4
  fisher_score(x, y) -> float                                                    # tiêu chí Fisher từng đặc trưng (B6.1)
Đặc trưng mới (>= 5, B6.2): trễ hợp lệ >= 240 giờ (xem src/guards.py), trung bình/độ lệch chuẩn trượt theo tuần,
lịch (sin/cos giờ, thứ, cuối tuần, lễ, kỳ học), thời tiết (T trung bình 3 thành phố, CDH = max(0, T - Tref), giờ x T).
Mọi thống kê dùng để tạo đặc trưng chỉ tính trên train.
"""
from __future__ import annotations

import numpy as np  # noqa: F401


def pca(X, k):
    raise NotImplementedError("B6: pca")


def lda_two_class(X, y):
    raise NotImplementedError("B6: lda_two_class")


def lda_multiclass(X, y, k):
    raise NotImplementedError("B6: lda_multiclass")


def fisher_score(x, y):
    raise NotImplementedError("B6: fisher_score")


def run(seed: int, final: bool = False) -> None:
    raise NotImplementedError("B6: features")
