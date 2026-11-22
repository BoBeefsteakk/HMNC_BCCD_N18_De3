"""Test bổ sung cho B4 (T006): đếm lỗi ĐỘC LẬP với pc.count_errors.

test_interfaces.py so Pocket với PLA bằng chính pc.count_errors; nếu hàm đó đếm sai (ví dụ bỏ sót g = 0)
thì Pocket có thể trả w = 0 mà test vẫn xanh. Ở đây đếm lại bằng biểu thức viết thẳng.
"""
import numpy as np

from src import perceptron as pc


def _errors(w, X, y):
    return int(np.sum(y * (X @ w) <= 0))


def _nonseparable(n=80, seed=0):
    rng = np.random.default_rng(seed)
    X = np.r_[rng.normal(1.0, 1.0, size=(n // 2, 2)), rng.normal(-1.0, 1.0, size=(n // 2, 2))]
    y = np.r_[np.ones(n // 2), -np.ones(n // 2)]
    y[rng.choice(n, size=n // 10, replace=False)] *= -1  # lật nhãn -> không khả tách
    return np.c_[X, np.ones(n)], y


def test_count_errors_treats_zero_margin_as_error():
    X, y = _nonseparable()
    assert pc.count_errors(np.zeros(X.shape[1]), X, y) == len(y)


def test_pocket_reports_true_error_and_beats_zero_vector():
    X, y = _nonseparable()
    w_best, errs = pc.pocket(X, y, max_epochs=30)
    assert errs[-1] == _errors(w_best, X, y)
    assert _errors(w_best, X, y) < len(y)  # w = 0 sai hết n mẫu, Pocket phải tốt hơn
    assert np.all(np.diff(errs) <= 0)
