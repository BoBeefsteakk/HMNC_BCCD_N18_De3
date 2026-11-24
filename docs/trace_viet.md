# Bảng truy vết kết quả thực nghiệm — Nguyễn Serov Trọng Việt

Mỗi hình hoặc bảng sinh ra từ mã thực nghiệm được ghi một dòng tại đây theo `docs/CONVENTIONS.md` mục 5.
Cuối kỳ Phi tổng hợp các bảng truy vết cá nhân thành Phụ lục D.

| Số Hình / Bảng | Tệp kết quả sinh ra | Hàm / Ô notebook sinh ra | Mã Task | Mô tả tóm tắt |
|---|---|---|---|---|
| Hình 4.1 | `results/figures/4_1_pla_pocket_epoch_error.png` | `src/perceptron.py` (`run` → `plot_epoch_errors`) | T011 | Số lỗi theo epoch của PLA và Pocket trên train, 4 cấu hình (gốc/z-score × duyệt cố định/xáo, 5 hạt giống) |
| Bảng 4.1 | `results/tables/4_1_pla_pocket_epoch_error.csv` | `src/perceptron.py` (`run` → `epoch_error_table`) | T011 | Số lỗi cuối của PLA và Pocket theo cấu hình, trung bình ± độ lệch chuẩn qua các lần chạy |
