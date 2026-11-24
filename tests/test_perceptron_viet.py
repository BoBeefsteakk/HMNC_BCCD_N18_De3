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


# --- T011: thí nghiệm lỗi theo epoch (B4.3) ------------------------------------------------------------
def _separable(n=60, seed=1):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, 2))
    y = np.where(X @ np.array([1.0, -2.0]) + 0.3 > 0, 1.0, -1.0)
    return X, y


def test_zscore_fit_uses_given_data_and_handles_constant_column():
    X = np.c_[np.arange(5.0), np.full(5, 7.0)]
    mean, std = pc._zscore_fit(X)
    Z = (X - mean) / std
    assert np.allclose(Z[:, 0].mean(), 0.0) and np.isclose(Z[:, 0].std(), 1.0)
    assert np.all(Z[:, 1] == 0.0)  # cột hằng: std = 1, không chia cho 0


def test_epoch_error_runs_shapes_and_seed_wiring():
    X, y = _nonseparable()
    X = X[:, :-1]  # epoch_error_runs tự thêm cột 1
    seeds, E = [3, 4, 5], 7
    runs = pc.epoch_error_runs(X, y, seeds, E)
    assert set(runs) == {(v, o) for v in pc.DATA_VARIANTS for o in pc.ORDERS}
    for (variant, order), r in runs.items():
        k = len(seeds) if order == "xao" else 1
        assert r["pla"].shape == (k, E) and r["pocket"].shape == (k, E)
    # Mỗi hàng "xáo" phải đúng là pla/pocket chạy với hạt giống tương ứng (không dùng nhầm một hạt giống)
    Xa = np.c_[X, np.ones(len(X))]
    for i, s in enumerate(seeds):
        assert np.array_equal(runs[("goc", "xao")]["pla"][i], pc._pad_last(pc.pla(Xa, y, E, True, s)[1], E))
        assert np.array_equal(runs[("goc", "xao")]["pocket"][i], pc._pad_last(pc.pocket(Xa, y, E, True, s)[1], E))
    # Nhánh z-score dùng thống kê của chính X truyền vào
    mean, std = X.mean(axis=0), X.std(axis=0)
    Za = np.c_[(X - mean) / std, np.ones(len(X))]
    assert np.array_equal(runs[("zscore", "co_dinh")]["pla"][0], pc._pad_last(pc.pla(Za, y, E)[1], E))


def test_epoch_error_runs_pads_after_pla_converges():
    X, y = _separable()
    runs = pc.epoch_error_runs(X, y, [0, 1], 200)
    r = runs[("goc", "co_dinh")]
    assert r["pla_epochs"][0] < 200  # khả tách: PLA dừng sớm
    assert r["pla"][0, -1] == 0 and r["pocket"][0, -1] == 0
    assert np.all(r["pla"][0, r["pla_epochs"][0] - 1:] == 0)


def test_epoch_error_table_matches_runs():
    X, y = _nonseparable()
    runs = pc.epoch_error_runs(X[:, :-1], y, [0, 1, 2], 5)
    table = pc.epoch_error_table(runs, len(y))
    assert len(table) == 4
    row = table[(table["du_lieu"] == "zscore") & (table["thu_tu"] == "xao")].iloc[0]
    last = runs[("zscore", "xao")]["pocket"][:, -1]
    assert row["so_lan_chay"] == 3
    assert np.isclose(row["pocket_loi_cuoi_tb"], last.mean()) and np.isclose(row["pocket_loi_cuoi_dlc"], last.std(ddof=1))
    fixed = table[table["thu_tu"] == "co_dinh"]
    assert (fixed["so_lan_chay"] == 1).all() and (fixed["pla_loi_cuoi_dlc"] == 0).all()


def test_run_std_divides_by_n_minus_1_and_single_run_is_zero():
    a = np.array([[1.0, 4.0], [3.0, 8.0], [5.0, 6.0]])
    assert np.allclose(pc._run_std(a), [2.0, 2.0])  # chia n - 1 = 2, không phải n = 3
    assert np.all(pc._run_std(a[:1]) == 0.0)  # một lần chạy (duyệt cố định, tất định): 0, không NaN


def test_plot_epoch_errors_writes_png(tmp_path):
    X, y = _nonseparable()
    runs = pc.epoch_error_runs(X[:, :-1], y, [0, 1], 4)
    path = tmp_path / "fig.png"
    pc.plot_epoch_errors(runs, len(y), path)
    assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
