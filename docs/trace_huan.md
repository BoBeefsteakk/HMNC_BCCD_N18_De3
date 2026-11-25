# Bảng truy vết kết quả thực nghiệm — Đỗ Minh Huấn

Mỗi hình ảnh hoặc bảng số liệu sinh ra từ mã thực nghiệm phục vụ báo cáo hoặc tài liệu nộp phải được ghi nhận tại đây theo quy ước tại `docs/CONVENTIONS.md` mục 5.
Cuối kỳ trưởng nhóm (Phi) sẽ tổng hợp các bảng truy vết cá nhân thành Phụ lục D của Báo cáo chuyên đề.

| Số Hình / Bảng | Tệp kết quả sinh ra | Hàm / Ô notebook sinh ra | Mã Task | Mô tả tóm tắt |
|---|---|---|---|---|
| Bảng 1.1 | `docs/DATA_DICTIONARY.md` | Thống kê từ `continuous.csv` & `forecast_cnd.csv` | T004 | Từ điển dữ liệu 17 biến phụ tải, thời tiết, lịch và tệp CND |
| Bảng 1.2 | `results/tables/1_2_eda_summary.csv` | `notebooks/huan_eda.ipynb` (Ô 2) | T005 | Thống kê mô tả (n, thiếu, TB, ĐLC, phân vị, tương quan với `nat_demand`) của 16 biến trên train |
| Hình 1.1 | `results/figures/1_1_load_timeseries_anomalies.png` | `notebooks/huan_eda.ipynb` (Ô 3) | T005 | Chuỗi phụ tải trung bình/cực tiểu theo tuần (`train` & `val`), 4 tuần khởi động và 8 giờ tải thấp bất thường |
| Hình 1.2 | `results/figures/1_2_load_distribution_peak.png` | `notebooks/huan_eda.ipynb` (Ô 4) | T005 | Phân bố `nat_demand` trên `train`, ngưỡng cao điểm 90% (1.450,75 MWh) và tỷ lệ nhãn +1/-1 (`train` vs `val`) |
| Hình 1.3 | `results/figures/1_3_diurnal_weekly_profile.png` | `notebooks/huan_eda.ipynb` (Ô 5) | T005 | Hồ sơ phụ tải trung bình ± 1 ĐLC theo 24 giờ (ngày làm việc/cuối tuần/lễ) và theo 7 thứ trong tuần trên `train` |
| Hình 1.4 | `results/figures/1_4_load_vs_temperature.png` | `notebooks/huan_eda.ipynb` (Ô 6) | T005 | Mật độ và trung bình phụ tải theo nhiệt độ trung bình 3 thành phố (`T2M_mean`), tách ngày làm việc và cuối tuần/lễ |
| Hình 1.5 | `results/figures/1_5_correlation_heatmap.png` | `notebooks/huan_eda.ipynb` (Ô 7) | T005 | Ma trận tương quan Pearson giữa `nat_demand`, 12 biến thời tiết tại 3 thành phố và 2 biến lịch trên `train` |
| Hình 4.2 | `results/figures/4_2_gd_momentum_loss.png` | `src/optim_linear.py` (`run` → `plot_gd_momentum_loss`) | T003 | Đường mất mát (MSE + L2) theo số lần cập nhật của GD, Momentum, Mini-batch và SGD, cùng w₀ = 0 và cùng η |
| Bảng 4.2 | `results/tables/4_2_gd_vs_closed_form.csv` | `src/optim_linear.py` (`run` → `save_gd_vs_closed_form_table`) | T003 | Val/train loss (MSE + L2) của nghiệm đóng, GD, Momentum, Mini-batch, SGD; số lần cập nhật đạt đích và sai số finite-diff |
