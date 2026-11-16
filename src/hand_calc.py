"""B7 – tính tay đối chiếu với mã (in kết quả cho Phụ lục A). Làm tròn 4 chữ số thập phân.

Bài toán hai lớp "giờ cao điểm cần cảnh báo": hồi quy logistic dùng nhãn {0,1}, PLA dùng nhãn ±1.
Dùng HAI đặc trưng có tiêu chí Fisher lớn nhất, đã chuẩn hóa z-score theo tập huấn luyện.
Việc cần làm (mã phải khớp tính tay đến 1e-4):
  B7.1a  một bước GD theo lô, hồi quy logistic, 6 mẫu, w(0)=0, eta=0,1, J = trung bình BCE không chính quy hóa
  B7.1b  một epoch PLA trên 6 mẫu theo thứ tự quy định, w(0)=0
  B7.2   forward + backward mạng 2-2-1 (sigmoid, BCE) trên mẫu đầu, khởi tạo và eta=0,5 do đề cho; kiểm chứng >= 1 đạo hàm bằng sai phân hữu hạn
  B7.3   PCA 6x2 (chia n-1, dấu véc tơ riêng: thành phần có |giá trị| lớn nhất là dương) và LDA hai lớp (||w|| = 1)
"""
from __future__ import annotations

import numpy as np


def select_six_samples(y_train, seed: int):
    """Chọn 6 mẫu theo ĐÚNG đoạn mã của đề (mục 3.3, B7): 3 mẫu +1 và 3 mẫu -1, thứ tự duyệt +,-,+,-,+,-.

    y_train: nhãn của bài toán hai lớp trên tập huấn luyện, theo thứ tự của tập huấn luyện (+1 / không phải +1).
    seed: SEED = 2026 + G.
    """
    rng = np.random.default_rng(seed)
    pos_idx = np.flatnonzero(y_train == 1)  # thứ tự của tập huấn luyện
    neg_idx = np.flatnonzero(y_train != 1)
    p = rng.choice(pos_idx, 3, replace=False)
    n = rng.choice(neg_idx, 3, replace=False)
    return [p[0], n[0], p[1], n[1], p[2], n[2]]  # thứ tự duyệt


def run(seed: int, final: bool = False) -> None:
    raise NotImplementedError("B7: hand_calc")
