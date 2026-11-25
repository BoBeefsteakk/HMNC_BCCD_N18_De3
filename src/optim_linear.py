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

from pathlib import Path
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
    w0: np.ndarray | None = None,
    max_updates: int | None = None,
    record_per_update: bool = False,
) -> tuple[np.ndarray, list[float]]:
    """Stochastic Gradient Descent (SGD): mỗi mẫu cập nhật một lần.

    Xáo trộn ngẫu nhiên thứ tự mẫu ở mỗi epoch bằng generator từ seed.
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    w = np.zeros(d, dtype=np.float64) if w0 is None else np.asarray(w0, dtype=np.float64).copy()
    rng = np.random.default_rng(seed)
    loss_history: list[float] = []
    updates = 0

    for _ in range(n_epochs):
        if not record_per_update:
            loss = mse_l2_loss(w, X, y, lam)
            loss_history.append(loss)
            if np.isnan(loss) or np.isinf(loss):
                break
        indices = rng.permutation(n)
        for i in indices:
            if max_updates is not None and updates >= max_updates:
                return w, loss_history
            if record_per_update:
                loss = mse_l2_loss(w, X, y, lam)
                loss_history.append(loss)
                if np.isnan(loss) or np.isinf(loss):
                    return w, loss_history
            xi = X[i]
            yi = y[i]
            res = float(np.dot(xi, w) - yi)
            g = res * xi
            reg = float(lam) * w
            reg[-1] = 0.0
            w -= float(eta) * (g + reg)
            updates += 1

    return w, loss_history


def minibatch_gd(
    X: np.ndarray,
    y: np.ndarray,
    lam: float,
    eta: float,
    n_epochs: int,
    batch_size: int,
    seed: int,
    w0: np.ndarray | None = None,
    max_updates: int | None = None,
    record_per_update: bool = False,
) -> tuple[np.ndarray, list[float]]:
    """Mini-batch Gradient Descent: cập nhật theo từng lô mẫu nhỏ (batch)."""
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    w = np.zeros(d, dtype=np.float64) if w0 is None else np.asarray(w0, dtype=np.float64).copy()
    rng = np.random.default_rng(seed)
    loss_history: list[float] = []
    updates = 0

    for _ in range(n_epochs):
        if not record_per_update:
            loss = mse_l2_loss(w, X, y, lam)
            loss_history.append(loss)
            if np.isnan(loss) or np.isinf(loss):
                break
        indices = rng.permutation(n)
        for start_idx in range(0, n, batch_size):
            if max_updates is not None and updates >= max_updates:
                return w, loss_history
            if record_per_update:
                loss = mse_l2_loss(w, X, y, lam)
                loss_history.append(loss)
                if np.isnan(loss) or np.isinf(loss):
                    return w, loss_history
            batch_idx = indices[start_idx : start_idx + batch_size]
            X_b = X[batch_idx]
            y_b = y[batch_idx]
            m = len(batch_idx)
            res = X_b @ w - y_b
            g = (X_b.T @ res) / m
            reg = float(lam) * w
            reg[-1] = 0.0
            w -= float(eta) * (g + reg)
            updates += 1

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


def updates_to_reach(loss_history: list[float], target_loss: float) -> int | None:
    """Số lần cập nhật nhỏ nhất để mất mát huấn luyện <= target_loss (None nếu chưa đạt)."""
    for step, loss in enumerate(loss_history):
        if loss <= target_loss:
            return step
    return None


def plot_gd_momentum_loss(
    hist_gd: list[float],
    hist_mom: list[float],
    path: Path | str,
    hist_mb: list[float] | None = None,
    hist_sgd: list[float] | None = None,
    loss_cf_train: float | None = None,
) -> None:
    """Hình 4.2: đường mất mát của GD, Momentum, Mini-batch và SGD theo số lần cập nhật (B3.1–B3.2)."""
    from matplotlib.figure import Figure

    fig = Figure(figsize=(12, 4.8), layout="constrained")
    axes = fig.subplots(1, 2)
    iters = np.arange(len(hist_gd))

    eta = config.B3_ETA
    beta = config.B3_MOMENTUM_BETA
    bs = config.B3_BATCH_SIZE
    n_zoom = min(60, len(hist_gd))

    for ax, lim, log_y, title in (
        (axes[0], len(hist_gd), True, f"Toàn bộ {len(hist_gd)} lần cập nhật (thang log y)"),
        (axes[1], n_zoom, False, f"{n_zoom} lần cập nhật đầu tiên (thang tuyến tính)"),
    ):
        if hist_sgd is not None:
            ax.plot(
                iters[:lim], hist_sgd[:lim],
                label=f"SGD (η = {eta}, batch = 1)",
                color="tab:orange", alpha=0.65, linewidth=1.0,
            )
        ax.plot(
            iters[:lim], hist_gd[:lim],
            label=f"GD theo lô (η = {eta})",
            color="tab:blue", linewidth=2.2, alpha=0.85,
        )
        if hist_mb is not None:
            ax.plot(
                iters[:lim], hist_mb[:lim],
                label=f"Mini-batch GD (η = {eta}, batch = {bs})",
                color="tab:green", linestyle="-.", linewidth=1.4,
            )
        ax.plot(
            iters[:lim], hist_mom[:lim],
            label=f"Momentum GD (η = {eta}, β = {beta})",
            color="tab:red", linestyle="--", linewidth=1.8,
        )
        if loss_cf_train is not None:
            ax.axhline(
                loss_cf_train,
                label=f"Nghiệm đóng Ridge (J* = {loss_cf_train:.2f})",
                color="black", linestyle=":", linewidth=1.2,
            )
        if log_y:
            ax.set_yscale("log")
            ax.set_ylabel("Hàm mất mát J(w) (MSE + L2, MWh², thang log)")
            ax.grid(True, alpha=0.3, which="both")
        else:
            ax.set_ylabel("Hàm mất mát J(w) (MSE + L2, MWh²)")
            ax.grid(True, alpha=0.3)
        ax.set_title(title)
        ax.set_xlabel("Số lần cập nhật trọng số (cùng w₀ = 0, cùng η)")
        ax.legend(fontsize=8.5, loc="upper right")

    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)


def save_gd_vs_closed_form_table(
    rows: list[dict],
    path: Path | str,
):
    """Bảng 4.2: val loss (MSE + L2), số lần cập nhật đạt đích và sai số finite-diff (B3.1–B3.4)."""
    import pandas as pd

    df_res = pd.DataFrame(rows)
    if "so_cap_nhat_dat_dich" in df_res.columns:
        df_res["so_cap_nhat_dat_dich"] = df_res["so_cap_nhat_dat_dich"].astype("Int64")
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_res.to_csv(out_path, index=False)
    return df_res


def run(seed: int, final: bool = False) -> None:
    """Thí nghiệm B3.1–B3.4: kiểm tra gradient, so sánh GD/SGD/mini-batch/Momentum và nghiệm đóng."""
    from . import data_prep

    raw_path = config.RAW_DIR / config.DATA_FILES["continuous"]["local_name"]
    if not raw_path.exists():
        print("B3: Chưa có tệp dữ liệu, bỏ qua chạy thực nghiệm trên dữ liệu thật.")
        return

    df = data_prep.load_raw(raw_path)
    splits = data_prep.split_weeks(df)
    train_df = data_prep.drop_warmup(splits["train"])
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

    lam = config.B3_LAMBDA
    eta = config.B3_ETA
    n_iter = config.B3_N_ITER
    beta = config.B3_MOMENTUM_BETA
    batch_size = config.B3_BATCH_SIZE
    loss_tol = config.B3_LOSS_TOL
    n_train = len(X_train)
    w0 = np.zeros(X_train.shape[1], dtype=np.float64)

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
    loss_cf_train = mse_l2_loss(w_cf, X_train, y_train, lam)
    loss_cf_val = mse_l2_loss(w_cf, X_val, y_val, lam)
    target_loss = loss_cf_train + loss_tol
    print(f"B3.4(b): Nghiệm đóng Ridge - val_loss (MSE+L2): {loss_cf_val:.4f} (train: {loss_cf_train:.4f})")

    # 3. GD, Momentum GD, Mini-batch GD và SGD — cùng điểm khởi tạo w0 = 0 và cùng eta
    w_gd, hist_gd = gd(X_train, y_train, lam, eta=eta, n_iter=n_iter, w0=w0)
    w_mom, hist_mom = momentum_gd(X_train, y_train, lam, eta=eta, beta=beta, n_iter=n_iter, w0=w0)

    batches_per_epoch = -(-n_train // batch_size)
    n_epochs_mb = -(-n_iter // batches_per_epoch)
    w_mb, hist_mb = minibatch_gd(
        X_train, y_train, lam, eta=eta, n_epochs=n_epochs_mb, batch_size=batch_size,
        seed=seed, w0=w0, max_updates=n_iter, record_per_update=True,
    )

    n_epochs_sgd = -(-n_iter // n_train)
    w_sgd, hist_sgd = sgd(
        X_train, y_train, lam, eta=eta, n_epochs=n_epochs_sgd,
        seed=seed, w0=w0, max_updates=n_iter, record_per_update=True,
    )

    loss_gd_train = mse_l2_loss(w_gd, X_train, y_train, lam)
    loss_gd_val = mse_l2_loss(w_gd, X_val, y_val, lam)
    loss_mom_train = mse_l2_loss(w_mom, X_train, y_train, lam)
    loss_mom_val = mse_l2_loss(w_mom, X_val, y_val, lam)
    loss_mb_train = mse_l2_loss(w_mb, X_train, y_train, lam)
    loss_mb_val = mse_l2_loss(w_mb, X_val, y_val, lam)
    loss_sgd_train = mse_l2_loss(w_sgd, X_train, y_train, lam)
    loss_sgd_val = mse_l2_loss(w_sgd, X_val, y_val, lam)

    upd_gd = updates_to_reach(hist_gd, target_loss)
    upd_mom = updates_to_reach(hist_mom, target_loss)
    upd_mb = updates_to_reach(hist_mb, target_loss)
    upd_sgd = updates_to_reach(hist_sgd, target_loss)

    print(f"B3.1: GD ({n_iter} cập nhật) - val_loss (MSE+L2): {loss_gd_val:.4f} (train: {loss_gd_train:.4f}, đạt đích sau {upd_gd} cập nhật)")
    print(f"B3.2: Momentum GD (beta={beta}, {n_iter} cập nhật) - val_loss (MSE+L2): {loss_mom_val:.4f} (train: {loss_mom_train:.4f}, đạt đích sau {upd_mom} cập nhật)")
    print(f"B3.1: Mini-batch GD (bs={batch_size}, {n_iter} cập nhật) - val_loss (MSE+L2): {loss_mb_val:.4f} (train: {loss_mb_train:.4f}, đạt đích sau {upd_mb} cập nhật)")
    print(f"B3.1: SGD (bs=1, {n_iter} cập nhật) - val_loss (MSE+L2): {loss_sgd_val:.4f} (train: {loss_sgd_train:.4f}, đạt đích sau {upd_sgd} cập nhật)")

    # 4. Lưu đồ thị và bảng kết quả theo CONVENTIONS.md mục 5
    fig_path = config.FIG_DIR / "4_2_gd_momentum_loss.png"
    plot_gd_momentum_loss(
        hist_gd, hist_mom, fig_path,
        hist_mb=hist_mb, hist_sgd=hist_sgd, loss_cf_train=loss_cf_train,
    )
    print(f"B3: Đã lưu hình {fig_path}")

    table_rows = [
        {
            "phuong_phap": "nghiem_dong",
            "so_lan_cap_nhat": 0,
            "batch_size": n_train,
            "eta": np.nan,
            "beta": np.nan,
            "lambda": lam,
            "train_loss_mse_l2": round(float(loss_cf_train), 4),
            "val_loss_mse_l2": round(float(loss_cf_val), 4),
            "chenh_val_loss_vs_nghiem_dong": 0.0,
            "muc_mat_mat_dich": round(float(target_loss), 4),
            "so_cap_nhat_dat_dich": 0,
            "sai_so_finite_diff": f"{fd_err:.2e}",
        },
        {
            "phuong_phap": "gd",
            "so_lan_cap_nhat": n_iter,
            "batch_size": n_train,
            "eta": eta,
            "beta": 0.0,
            "lambda": lam,
            "train_loss_mse_l2": round(float(loss_gd_train), 4),
            "val_loss_mse_l2": round(float(loss_gd_val), 4),
            "chenh_val_loss_vs_nghiem_dong": round(float(loss_gd_val - loss_cf_val), 4),
            "muc_mat_mat_dich": round(float(target_loss), 4),
            "so_cap_nhat_dat_dich": upd_gd,
            "sai_so_finite_diff": f"{fd_err:.2e}",
        },
        {
            "phuong_phap": "momentum_gd",
            "so_lan_cap_nhat": n_iter,
            "batch_size": n_train,
            "eta": eta,
            "beta": beta,
            "lambda": lam,
            "train_loss_mse_l2": round(float(loss_mom_train), 4),
            "val_loss_mse_l2": round(float(loss_mom_val), 4),
            "chenh_val_loss_vs_nghiem_dong": round(float(loss_mom_val - loss_cf_val), 4),
            "muc_mat_mat_dich": round(float(target_loss), 4),
            "so_cap_nhat_dat_dich": upd_mom,
            "sai_so_finite_diff": f"{fd_err:.2e}",
        },
        {
            "phuong_phap": "minibatch_gd",
            "so_lan_cap_nhat": n_iter,
            "batch_size": batch_size,
            "eta": eta,
            "beta": 0.0,
            "lambda": lam,
            "train_loss_mse_l2": round(float(loss_mb_train), 4),
            "val_loss_mse_l2": round(float(loss_mb_val), 4),
            "chenh_val_loss_vs_nghiem_dong": round(float(loss_mb_val - loss_cf_val), 4),
            "muc_mat_mat_dich": round(float(target_loss), 4),
            "so_cap_nhat_dat_dich": upd_mb,
            "sai_so_finite_diff": f"{fd_err:.2e}",
        },
        {
            "phuong_phap": "sgd",
            "so_lan_cap_nhat": n_iter,
            "batch_size": 1,
            "eta": eta,
            "beta": 0.0,
            "lambda": lam,
            "train_loss_mse_l2": round(float(loss_sgd_train), 4),
            "val_loss_mse_l2": round(float(loss_sgd_val), 4),
            "chenh_val_loss_vs_nghiem_dong": round(float(loss_sgd_val - loss_cf_val), 4),
            "muc_mat_mat_dich": round(float(target_loss), 4),
            "so_cap_nhat_dat_dich": upd_sgd,
            "sai_so_finite_diff": f"{fd_err:.2e}",
        },
    ]

    tbl_path = config.TABLE_DIR / "4_2_gd_vs_closed_form.csv"
    save_gd_vs_closed_form_table(table_rows, path=tbl_path)
    print(f"B3: Đã lưu bảng {tbl_path}")
