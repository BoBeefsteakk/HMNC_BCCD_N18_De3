"""Chỉ số đánh giá và tập kiểm tra (B1.1, B9, R2).

Chỉ số chính: MAPE theo giờ của từng tuần kiểm tra, lấy trung bình các tuần. Phụ: MAE, RMSE (MWh);
sai số đỉnh tuần, đáy tuần, năng lượng tuần [7]. Chỉ số kỹ năng = 1 - MAPE_mô_hình / MAPE_cơ_sở.
Được dùng scikit-learn để tính chỉ số (đề mục 2.4).

Hàm cần có:
  mape / mae / rmse (theo từng tuần, rồi trung bình tuần)
  skill_score(mape_model, mape_baseline)
  bootstrap_ci(per_week_errors, n_boot=config.BOOTSTRAP_ITERS, seed)  # CI 95% (config.BOOTSTRAP_CI), lấy lại mẫu THEO TUẦN (B9.1)
Tập kiểm tra: BẮT BUỘC đi qua src.guards.open_test_set(final) — chỉ mở một lần, ở cuối (đề mục 3.1d, 6.4).
"""
from __future__ import annotations


def run(seed: int, final: bool = False) -> None:
    raise NotImplementedError("B9: evaluate")
