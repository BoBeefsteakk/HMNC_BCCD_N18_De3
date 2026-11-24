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
    """Thí nghiệm B4: hiện có phần lỗi theo epoch của B4.3 (T011). Khả tách bằng LP (B4.2) và vùng quyết định (B4.4) chưa làm.

    Dữ liệu: chỉ train, bỏ tuần khởi động; nhãn ±1 "giờ cao điểm" (ngưỡng từ train); 12 biến thời tiết.
    Không đọc val/test nên `final` không đổi gì. `seed` không dùng: thí nghiệm lặp lấy hạt giống từ config.get_run_seeds().
    """
    from . import config, data_prep

    raw_path = data_prep.RAW_CONTINUOUS
    if not raw_path.exists():
        print("B4: chưa có tệp dữ liệu, bỏ qua thí nghiệm lỗi theo epoch.")
        return

    train = data_prep.split_weeks(data_prep.load_raw(raw_path))["train"]
    # Ngưỡng cao điểm tính trên cả 209 tuần train (như data_prep.run in ra), rồi mới bỏ tuần khởi động khi học.
    y_all = data_prep.peak_label(train[config.TARGET_COL].to_numpy(), np.ones(len(train), dtype=bool))
    learn = (train["week_idx"] >= config.WARMUP_WEEKS).to_numpy()
    X = train.loc[learn, config.WEATHER_COLS].to_numpy(dtype=np.float64)
    y = y_all[learn]

    seeds = config.get_run_seeds()
    max_epochs = config.PERCEPTRON_MAX_EPOCHS
    print(f"B4.3: train {len(y)} giờ, {int(np.sum(y == 1))} giờ cao điểm (+1); {X.shape[1]} biến thời tiết; "
          f"tối đa {max_epochs} epoch; hạt giống khi xáo: {seeds}")
    runs = epoch_error_runs(X, y, seeds, max_epochs)

    config.TABLE_DIR.mkdir(parents=True, exist_ok=True)
    config.FIG_DIR.mkdir(parents=True, exist_ok=True)
    table = epoch_error_table(runs, len(y))
    table_path = config.TABLE_DIR / "4_1_pla_pocket_epoch_error.csv"
    fig_path = config.FIG_DIR / "4_1_pla_pocket_epoch_error.png"
    table.to_csv(table_path, index=False, float_format="%.2f")
    plot_epoch_errors(runs, len(y), fig_path)
    print(table.to_string(index=False))
    print(f"đã ghi {table_path.relative_to(config.ROOT)} và {fig_path.relative_to(config.ROOT)}")


# --- B4.3 (T011): lỗi theo epoch ---------------------------------------------------------------------
DATA_VARIANTS = ("goc", "zscore")  # dữ liệu gốc / z-score khớp trên train
ORDERS = ("co_dinh", "xao")  # duyệt 0..n-1 mỗi epoch / hoán vị mới mỗi epoch
_LABELS = {"goc": "Dữ liệu gốc", "zscore": "Z-score (thống kê của train)", "co_dinh": "duyệt cố định", "xao": "xáo mỗi epoch"}


def _zscore_fit(X):
    """Trung bình và độ lệch chuẩn (chia n) theo cột của X; cột hằng thì lấy std = 1 để khỏi chia cho 0."""
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std[std == 0.0] = 1.0
    return mean, std


def _pad_last(curve, length):
    """PLA/Pocket dừng sớm khi đạt 0 lỗi; kéo dài bằng giá trị cuối để các lần chạy cùng độ dài khi lấy trung bình."""
    curve = np.asarray(curve)
    return np.r_[curve, np.full(length - len(curve), curve[-1])]


def epoch_error_runs(X, y, seeds, max_epochs):
    """Chạy PLA và Pocket cho 4 cấu hình: {dữ liệu gốc, z-score} x {duyệt cố định, xáo mỗi epoch}.

    X: đặc trưng CHƯA mở rộng của tập học; z-score khớp trên chính X này (chỉ truyền train vào).
    Duyệt cố định không dùng hạt giống nên chạy một lần; xáo thì chạy một lần cho mỗi hạt giống trong `seeds`.
    Trả về {(du_lieu, thu_tu): {"pla": mảng (số lần chạy, max_epochs), "pocket": như trên, "pla_epochs": số epoch PLA đã chạy}}.
    """
    X = np.asarray(X, dtype=np.float64)
    mean, std = _zscore_fit(X)
    inputs = {"goc": X, "zscore": (X - mean) / std}
    runs = {}
    for variant in DATA_VARIANTS:
        Xa = np.c_[inputs[variant], np.ones(len(X))]  # x̃ = (x, 1), hệ số tự do ở cuối
        for order in ORDERS:
            shuffle = order == "xao"
            pla_rows, pocket_rows, pla_epochs = [], [], []
            for s in (seeds if shuffle else seeds[:1]):
                _, e_pla = pla(Xa, y, max_epochs=max_epochs, shuffle=shuffle, seed=s)
                _, e_pocket = pocket(Xa, y, max_epochs=max_epochs, shuffle=shuffle, seed=s)
                pla_epochs.append(len(e_pla))
                pla_rows.append(_pad_last(e_pla, max_epochs))
                pocket_rows.append(_pad_last(e_pocket, max_epochs))
            runs[(variant, order)] = {"pla": np.array(pla_rows), "pocket": np.array(pocket_rows),
                                      "pla_epochs": np.array(pla_epochs)}
    return runs


def epoch_error_table(runs, n):
    """Bảng 4.1: mỗi cấu hình một dòng, số lỗi cuối (epoch cuối) của PLA và Pocket, trung bình ± độ lệch chuẩn (chia số lần chạy)."""
    import pandas as pd

    rows = []
    for (variant, order), r in runs.items():
        pla_last, pocket_last = r["pla"][:, -1], r["pocket"][:, -1]
        rows.append({
            "du_lieu": variant,
            "thu_tu": order,
            "so_lan_chay": len(pla_last),
            "n_mau": n,
            "pla_loi_cuoi_tb": pla_last.mean(),
            "pla_loi_cuoi_dlc": pla_last.std(),
            "pocket_loi_cuoi_tb": pocket_last.mean(),
            "pocket_loi_cuoi_dlc": pocket_last.std(),
            "pocket_ti_le_loi_tb_pct": 100.0 * pocket_last.mean() / n,
            "pla_so_lan_ve_0_loi": int(np.sum(pla_last == 0)),
            "pla_so_epoch_da_chay_tb": r["pla_epochs"].mean(),
        })
    return pd.DataFrame(rows)


def plot_epoch_errors(runs, n, path):
    """Hình 4.1: số lỗi theo epoch, mỗi kiểu dữ liệu một ô; khi xáo vẽ trung bình và dải ±1 độ lệch chuẩn qua hạt giống."""
    from matplotlib.figure import Figure  # không qua pyplot nên không phụ thuộc backend màn hình

    fig = Figure(figsize=(11, 4.2), layout="constrained")
    axes = fig.subplots(1, len(DATA_VARIANTS), sharey=True)
    colors = {"pla": "tab:red", "pocket": "tab:blue"}
    for ax, variant in zip(axes, DATA_VARIANTS):
        for algo in ("pla", "pocket"):
            for order in ORDERS:
                curves = runs[(variant, order)][algo]
                epochs = np.arange(1, curves.shape[1] + 1)
                mean, sd = curves.mean(axis=0), curves.std(axis=0)
                label = f"{algo.upper() if algo == 'pla' else 'Pocket'}, {_LABELS[order]}"
                if order == "xao":
                    label += f" (TB ± 1 ĐLC, {curves.shape[0]} hạt giống)"
                    ax.fill_between(epochs, mean - sd, mean + sd, color=colors[algo], alpha=0.2, linewidth=0)
                ax.plot(epochs, mean, color=colors[algo], linestyle="-" if order == "xao" else "--", label=label)
        ax.set_title(_LABELS[variant])
        ax.set_xlabel("Epoch (một lượt duyệt hết train)")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel(f"Số lỗi trên train (giờ phân loại sai, n = {n})")
    axes[-1].legend(fontsize=8, loc="upper right")
    fig.savefig(path, dpi=120)
