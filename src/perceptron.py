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

import numpy as np


def _check_inputs(X, y):
    """X là ma trận đã mở rộng X̃ (cột 1 ở cuối, do người gọi thêm); y chỉ gồm ±1."""
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64).ravel()
    if X.ndim != 2 or X.shape[0] != y.shape[0]:
        raise ValueError(f"X phải có dạng (n, d) và khớp len(y); nhận {X.shape} và {y.shape}")
    if not np.all(np.isin(y, (-1.0, 1.0))):
        raise ValueError("PLA/Pocket cần nhãn ±1 (nhãn {0, 1} thì đổi bằng 2*y - 1)")
    return X, y


def _epoch_order(n, shuffle, rng):
    # Không xáo: duyệt 0, 1, ..., n-1 mỗi epoch. Có xáo: hoán vị mới mỗi epoch, lấy từ rng theo seed.
    return rng.permutation(n) if shuffle else np.arange(n)


def count_errors(w, X, y):
    """Số mẫu phân loại sai: y·g <= 0 với g = x̃·w (g = 0 cũng tính là sai)."""
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64).ravel()
    return int(np.sum(y * (X @ w) <= 0))


def pla(X, y, max_epochs=100, shuffle=False, seed=0):
    """PLA: w̃(0) = 0, gặp mẫu sai thì w̃ <- w̃ + y_i·x̃_i (η = 1; vì w̃(0) = 0 nên η nào cũng ra cùng ranh giới).

    Một epoch = duyệt hết n mẫu một lượt; sau mỗi epoch ghi số lỗi trên toàn tập.
    Dừng khi một epoch kết thúc với 0 lỗi, hoặc hết max_epochs.
    Trả về (w cuối cùng, mảng số lỗi theo epoch).
    """
    X, y = _check_inputs(X, y)
    n, d = X.shape
    rng = np.random.default_rng(seed)
    w = np.zeros(d)
    errors_per_epoch = []
    for _ in range(max_epochs):
        for i in _epoch_order(n, shuffle, rng):
            if y[i] * (X[i] @ w) <= 0:
                w = w + y[i] * X[i]
        errors_per_epoch.append(count_errors(w, X, y))
        if errors_per_epoch[-1] == 0:
            break
    return w, np.array(errors_per_epoch)


def pocket(X, y, max_epochs=100, shuffle=False, seed=0):
    """Pocket: chạy đúng các bước cập nhật như PLA, nhưng giữ lại ("bỏ túi") w có ít lỗi nhất trên toàn tập.

    Sau MỖI lần cập nhật thì đếm lại lỗi; ít hơn w đang giữ thì thay. Ban đầu túi chứa w̃(0) = 0 (n lỗi, vì g = 0).
    Ghi số lỗi của w trong túi sau mỗi epoch, nên mảng này không tăng. Điều kiện dừng giống PLA.
    Trả về (w tốt nhất, mảng số lỗi theo epoch).
    """
    X, y = _check_inputs(X, y)
    n, d = X.shape
    rng = np.random.default_rng(seed)
    w = np.zeros(d)
    w_best, best_err = w.copy(), count_errors(w, X, y)
    errors_per_epoch = []
    for _ in range(max_epochs):
        for i in _epoch_order(n, shuffle, rng):
            if y[i] * (X[i] @ w) <= 0:
                w = w + y[i] * X[i]
                err = count_errors(w, X, y)
                if err < best_err:
                    w_best, best_err = w.copy(), err
        errors_per_epoch.append(best_err)
        if best_err == 0:
            break
    return w_best, np.array(errors_per_epoch)


def check_separable_lp(X, y):
    raise NotImplementedError("B4: check_separable_lp")


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B4.2–B4.4: khả tách (LP), lỗi theo epoch, >= 5 hạt giống, vùng quyết định 2 đặc trưng."""
    raise NotImplementedError("B4: perceptron")
