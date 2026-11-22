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

import numpy as np


def pca(X, k):
    """PCA qua trị riêng của ma trận hiệp phương sai (chia n - 1, khớp sklearn).

    X: (n, d) KHÔNG có cột 1 (khác quy ước X̃ ở perceptron/hồi quy). Biến khác đơn vị thì người gọi
    chuẩn hóa z-score theo train trước. Trả về dict:
      mean[d]               trung bình từng cột (để chiếu dữ liệu mới: (X_new - mean) @ components.T)
      components[k, d]      k véc tơ riêng đơn vị, xếp theo trị riêng giảm dần (mỗi HÀNG là một thành phần)
      eigvals[k]            k trị riêng lớn nhất = phương sai dữ liệu dọc theo từng thành phần
      explained_ratio[k]    eigvals / tổng MỌI trị riêng (tổng phương sai), chưa cộng dồn
    Dấu véc tơ riêng (quy ước B7.3): phần tử có trị tuyệt đối lớn nhất mang dấu dương.
    """
    X = np.asarray(X, dtype=np.float64)
    if X.ndim != 2:
        raise ValueError(f"X phải có dạng (n, d); nhận {X.shape}")
    n, d = X.shape
    if not 1 <= k <= d:
        raise ValueError(f"k phải trong [1, {d}]; nhận {k}")
    if n < 2:
        raise ValueError("cần ít nhất 2 mẫu để tính hiệp phương sai chia n - 1")

    mean = X.mean(axis=0)
    Xc = X - mean
    cov = Xc.T @ Xc / (n - 1)

    # eigh cho ma trận đối xứng: trị riêng thực, xếp TĂNG dần -> đảo lại cho giảm dần.
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = np.argsort(eigvals)[::-1]
    eigvals, eigvecs = eigvals[order], eigvecs[:, order]
    total_var = eigvals.sum()

    components = eigvecs[:, :k].T  # cột của eigh là véc tơ riêng -> chuyển thành hàng
    biggest = np.argmax(np.abs(components), axis=1)
    signs = np.sign(components[np.arange(k), biggest])
    components = components * signs[:, None]

    return {
        "mean": mean,
        "components": components,
        "eigvals": eigvals[:k],
        "explained_ratio": eigvals[:k] / total_var,
    }


def lda_two_class(X, y):
    raise NotImplementedError("B6: lda_two_class")


def lda_multiclass(X, y, k):
    raise NotImplementedError("B6: lda_multiclass")


def fisher_score(x, y):
    """Tiêu chí Fisher của MỘT đặc trưng cho bài toán hai lớp:  J = (m1 - m0)^2 / (s1^2 + s0^2).

    m_c, s_c^2: trung bình và phương sai (chia n_c, không phải n_c - 1) của x trong lớp c.
    Nhãn y là hai giá trị bất kỳ (±1 hoặc {0, 1}); J đối xứng nên lớp nào là "1" không quan trọng.
    J lớn = hai lớp cách xa nhau so với độ tản trong lớp = đặc trưng phân biệt tốt.
    Hai lớp đều hằng số (mẫu số 0): trả về inf nếu hai trung bình khác nhau, 0 nếu trùng.
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    y = np.asarray(y).ravel()
    if x.shape != y.shape:
        raise ValueError(f"x và y phải cùng độ dài; nhận {x.shape} và {y.shape}")
    classes = np.unique(y)
    if classes.size != 2:
        raise ValueError(f"fisher_score cần đúng 2 lớp; nhận {classes.size}")

    x0, x1 = x[y == classes[0]], x[y == classes[1]]
    between = (x1.mean() - x0.mean()) ** 2
    within = x1.var() + x0.var()
    if within == 0:
        return float(np.inf) if between > 0 else 0.0
    return float(between / within)


def run(seed: int, final: bool = False) -> None:
    raise NotImplementedError("B6: features")
