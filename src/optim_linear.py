"""B3 – GD theo lô, SGD, mini-batch, momentum cho HỒI QUY TUYẾN TÍNH (MSE + L2).

Khối chấm: B3.1–B3.4, câu hỏi nghiên cứu (3).
TỰ CÀI ĐẶT bằng NumPy; KHÔNG dùng sklearn/autograd cho phần lõi (đề mục 2.4).
Mã do thành viên tự cài đặt hoặc có sự hỗ trợ của AI theo luật tại TEAM.md mục 8.

Quy ước:
  X là ma trận đã mở rộng X̃ = [X, 1] (cột 1 ở cuối); w có d+1 phần tử, hệ số tự do là phần tử cuối.
  J(w) = 1/(2n) * ||X̃ w - y||^2 + (lam/2) * ||w[:-1]||^2        (KHÔNG phạt hệ số tự do)
  grad = 1/n * X̃ᵀ(X̃ w - y) + lam * [w[:-1], 0]

Giao diện:
  mse_l2_loss(w, X, y, lam) -> float
  mse_l2_grad(w, X, y, lam) -> ndarray
  gd(X, y, lam, eta, n_iter, w0=None) -> (w, loss_history)
  sgd(X, y, lam, eta, n_epochs, seed) -> (w, loss_history)
  minibatch_gd(X, y, lam, eta, n_epochs, batch_size, seed) -> (w, loss_history)
  momentum_gd(X, y, lam, eta, beta, n_iter, w0=None) -> (w, loss_history)
  ridge_closed_form(X, y, lam) -> w
  finite_diff_check(loss_fn, grad_fn, w, eps=1e-6) -> float
"""
from __future__ import annotations

import numpy as np

from . import config


def mse_l2_loss(w: np.ndarray, X: np.ndarray, y: np.ndarray, lam: float) -> float:
    """Hàm mất mát MSE có chính quy hóa L2 (Ridge).

    J(w) = 1/(2n) * ||X̃ w - y||^2 + (lam/2) * ||w[:-1]||^2
    Lưu ý: Không phạt hệ số tự do w[-1] (phần tử cuối cùng).
    """
    w = np.asarray(w, dtype=np.float64)
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n = X.shape[0]
    if n == 0:
        return 0.0
    res = X @ w - y
    l2 = float(lam) * np.sum(w[:-1] ** 2)
    return float(0.5 / n * np.dot(res, res) + 0.5 * l2)


def mse_l2_grad(w: np.ndarray, X: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Gradient giải tích chính xác của hàm mất mát J(w).

    grad = 1/n * X̃ᵀ(X̃ w - y) + lam * [w[:-1], 0]
    """
    w = np.asarray(w, dtype=np.float64)
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n = X.shape[0]
    if n == 0:
        return np.zeros_like(w)
    res = X @ w - y
    g = (X.T @ res) / n
    reg = float(lam) * w.copy()
    reg[-1] = 0.0
    return g + reg


def ridge_closed_form(X: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Nghiệm giải tích (closed-form) của hồi quy Ridge không phạt hệ số tự do.

    (1/n * X̃ᵀX̃ + lam * I_reg) w = 1/n * X̃ᵀy
    với I_reg = diag(1, 1, ..., 1, 0) kích thước (d+1) x (d+1).
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    A = (X.T @ X) / n
    I_reg = np.eye(d, dtype=np.float64)
    I_reg[-1, -1] = 0.0
    A += float(lam) * I_reg
    b = (X.T @ y) / n
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return np.linalg.lstsq(A, b, rcond=None)[0]


def finite_diff_check(loss_fn, grad_fn, w: np.ndarray, eps: float = 1e-6) -> float:
    """Kiểm tra gradient giải tích bằng sai phân hữu hạn trung tâm.

    Sai số tương đối: ||grad_exact - grad_num|| / max(||grad_exact||, 1e-12).
    Yêu cầu đạt chuẩn: <= 1e-6 (trên float64).
    """
    w = np.asarray(w, dtype=np.float64)
    grad_exact = np.asarray(grad_fn(w), dtype=np.float64)
    grad_num = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w)
        e[i] = eps
        loss_plus = loss_fn(w + e)
        loss_minus = loss_fn(w - e)
        grad_num[i] = (loss_plus - loss_minus) / (2.0 * eps)
    denom = max(float(np.linalg.norm(grad_exact)), 1e-12)
    return float(np.linalg.norm(grad_exact - grad_num) / denom)


def gd(
    X: np.ndarray,
    y: np.ndarray,
    lam: float,
    eta: float,
    n_iter: int,
    w0: np.ndarray | None = None,
) -> tuple[np.ndarray, list[float]]:
    """Gradient Descent theo lô (Batch Gradient Descent).

    Cập nhật toàn bộ mẫu cùng lúc ở mỗi bước lặp: w = w - eta * grad.
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    w = np.zeros(X.shape[1], dtype=np.float64) if w0 is None else np.asarray(w0, dtype=np.float64).copy()
    loss_history: list[float] = []

    for _ in range(n_iter):
        loss = mse_l2_loss(w, X, y, lam)
        loss_history.append(loss)
        if np.isnan(loss) or np.isinf(loss):
            break
        g = mse_l2_grad(w, X, y, lam)
        w -= float(eta) * g

    return w, loss_history


def sgd(
    X: np.ndarray,
    y: np.ndarray,
    lam: float,
    eta: float,
    n_epochs: int,
    seed: int,
) -> tuple[np.ndarray, list[float]]:
    """Stochastic Gradient Descent (SGD): mỗi mẫu cập nhật một lần.

    Xáo trộn ngẫu nhiên thứ tự mẫu ở mỗi epoch bằng generator từ seed.
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    w = np.zeros(d, dtype=np.float64)
    rng = np.random.default_rng(seed)
    loss_history: list[float] = []

    for _ in range(n_epochs):
        loss = mse_l2_loss(w, X, y, lam)
        loss_history.append(loss)
        if np.isnan(loss) or np.isinf(loss):
            break
        indices = rng.permutation(n)
        for i in indices:
            xi = X[i]
            yi = y[i]
            res = float(np.dot(xi, w) - yi)
            g = res * xi
            reg = float(lam) * w
            reg[-1] = 0.0
            w -= float(eta) * (g + reg)

    return w, loss_history


def minibatch_gd(
    X: np.ndarray,
    y: np.ndarray,
    lam: float,
    eta: float,
    n_epochs: int,
    batch_size: int,
    seed: int,
) -> tuple[np.ndarray, list[float]]:
    """Mini-batch Gradient Descent: cập nhật theo từng lô mẫu nhỏ (batch)."""
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    w = np.zeros(d, dtype=np.float64)
    rng = np.random.default_rng(seed)
    loss_history: list[float] = []

    for _ in range(n_epochs):
        loss = mse_l2_loss(w, X, y, lam)
        loss_history.append(loss)
        if np.isnan(loss) or np.isinf(loss):
            break
        indices = rng.permutation(n)
        for start_idx in range(0, n, batch_size):
            batch_idx = indices[start_idx : start_idx + batch_size]
            X_b = X[batch_idx]
            y_b = y[batch_idx]
            m = len(batch_idx)
            res = X_b @ w - y_b
            g = (X_b.T @ res) / m
            reg = float(lam) * w
            reg[-1] = 0.0
            w -= float(eta) * (g + reg)

    return w, loss_history


def momentum_gd(
    X: np.ndarray,
    y: np.ndarray,
    lam: float,
    eta: float,
    beta: float,
    n_iter: int,
    w0: np.ndarray | None = None,
) -> tuple[np.ndarray, list[float]]:
    """Gradient Descent với quán tính Momentum (Polyak).

    v = beta * v + eta * grad
    w = w - v
    Với beta = 0, thuật toán trở về GD thông thường.
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    w = np.zeros(X.shape[1], dtype=np.float64) if w0 is None else np.asarray(w0, dtype=np.float64).copy()
    v = np.zeros_like(w)
    loss_history: list[float] = []

    for _ in range(n_iter):
        loss = mse_l2_loss(w, X, y, lam)
        loss_history.append(loss)
        if np.isnan(loss) or np.isinf(loss):
            break
        g = mse_l2_grad(w, X, y, lam)
        v = float(beta) * v + float(eta) * g
        w -= v

    return w, loss_history


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B3.2–B3.4: kiểm tra gradient, so sánh GD/Momentum và nghiệm đóng."""
    from . import data_prep

    raw_path = config.RAW_DIR / config.DATA_FILES["continuous"]["local_name"]
    if not raw_path.exists():
        print("B3: Chưa có tệp dữ liệu, bỏ qua chạy thực nghiệm trên dữ liệu thật.")
        return

    df = data_prep.load_raw(raw_path)
    splits = data_prep.split_weeks(df)
    train_df = splits["train"]
    val_df = splits["val"]

    # Sử dụng 12 biến thời tiết từ config
    cols = config.WEATHER_COLS
    X_train_raw = train_df[cols].to_numpy(dtype=np.float64)
    y_train = train_df[config.TARGET_COL].to_numpy(dtype=np.float64)
    X_val_raw = val_df[cols].to_numpy(dtype=np.float64)
    y_val = val_df[config.TARGET_COL].to_numpy(dtype=np.float64)

    # Chuẩn hóa z-score KHỚP TRÊN TRAIN (không rò rỉ vào val)
    mean = np.mean(X_train_raw, axis=0)
    std = np.std(X_train_raw, axis=0)
    std[std == 0.0] = 1.0

    X_train = np.c_[(X_train_raw - mean) / std, np.ones(len(X_train_raw))]
    X_val = np.c_[(X_val_raw - mean) / std, np.ones(len(X_val_raw))]

    lam = 0.1
    # 1. Kiểm tra gradient sai phân hữu hạn trên mẫu con
    w_test = np.zeros(X_train.shape[1], dtype=np.float64)
    w_test[0] = 1.0
    fd_err = finite_diff_check(
        lambda w: mse_l2_loss(w, X_train[:100], y_train[:100], lam),
        lambda w: mse_l2_grad(w, X_train[:100], y_train[:100], lam),
        w_test,
    )
    print(f"B3.4(a): Sai số kiểm tra gradient (finite_diff_check): {fd_err:.2e} (<= 1e-6 là ĐẠT)")

    # 2. Nghiệm đóng Ridge
    w_cf = ridge_closed_form(X_train, y_train, lam)
    loss_cf_val = mse_l2_loss(w_cf, X_val, y_val, lam)
    print(f"B3.4(b): Nghiệm đóng Ridge - Loss trên val: {loss_cf_val:.4f}")

    # 3. GD và Momentum GD
    eta = 0.05
    n_iter = 500
    beta = 0.85
    w_gd, hist_gd = gd(X_train, y_train, lam, eta=eta, n_iter=n_iter)
    w_mom, hist_mom = momentum_gd(X_train, y_train, lam, eta=eta, beta=beta, n_iter=n_iter)

    loss_gd_val = mse_l2_loss(w_gd, X_val, y_val, lam)
    loss_mom_val = mse_l2_loss(w_mom, X_val, y_val, lam)
    print(f"B3.1: GD ({n_iter} iter) - Loss val: {loss_gd_val:.4f}")
    print(f"B3.2: Momentum GD (beta={beta}, {n_iter} iter) - Loss val: {loss_mom_val:.4f}")
