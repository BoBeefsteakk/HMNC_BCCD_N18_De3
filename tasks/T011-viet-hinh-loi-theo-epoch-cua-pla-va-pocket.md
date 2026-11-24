---
id: T011
title: Hình lỗi theo epoch của PLA và Pocket
phase: P2
checklist: B4.3
owner: viet
status: done
due: 26/11/2026
files: src/perceptron.py,tests/test_perceptron_viet.py
depends: T006
---
# T011 — Hình lỗi theo epoch của PLA và Pocket

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Chạy `pla` và `pocket` (T006, đã có) trên bài toán phụ "giờ cao điểm" bằng dữ liệu thật của train, ghi số lỗi theo epoch vào `results/` và vẽ hình. Phục vụ B4.3 và đoạn "kết quả perceptron ban đầu" của báo cáo tiến độ (T008, Huấn cần trước 28/11). Làm trong hàm `run` của `src/perceptron.py` (phần lỗi theo epoch; kiểm khả tách bằng LP và vùng quyết định chưa giao).

## Đầu vào cần đọc
- `TEAM.md`, `docs/VIET.md`, `docs/CONVENTIONS.md` (mục 3 nhãn ±1, mục 5 tên và nơi lưu hình/bảng, mục 7 hạt giống), `src/config.py`
- Slide Chương 2 (2.4), slide 21 và 22: hình mẫu PLA dao động và Pocket
- `src/data_prep.py` (`peak_label`, `drop_warmup`), `src/perceptron.py`
- Đề `docs/DE3.md` mục B4.3

## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Dữ liệu: chỉ train (sau `drop_warmup`), nhãn ±1 từ `peak_label`, 12 biến thời tiết; không đọc val/test. Nếu chọn bộ đặc trưng khác thì ghi lý do vào Kết quả và báo Phi.
- Chạy 4 cấu hình: dữ liệu gốc và z-score (thống kê tính trên train), mỗi loại duyệt cố định và xáo mỗi epoch. Xáo thì dùng 5 hạt giống từ `config.get_run_seeds()`; `max_epochs` = `config.PERCEPTRON_MAX_EPOCHS` (50, Phi vừa thêm).
- Hình `results/figures/4_1_pla_pocket_epoch_error.png`: số lỗi theo epoch của PLA và Pocket (đường trung bình và dải ±1 độ lệch chuẩn qua hạt giống khi xáo), trục có tên và đơn vị.
- Bảng `results/tables/4_1_pla_pocket_epoch_error.csv`: mỗi cấu hình, số lỗi cuối của PLA và Pocket, trung bình ± độ lệch chuẩn.
- Có test (trong `tests/test_perceptron_viet.py`) cho phần mới, xanh KHÔNG SKIP. Trong Kết quả nêu: PLA dừng ở 0 lỗi hay hết epoch, có phải dữ liệu không khả tách không (chỉ kết luận nếu có căn cứ; chưa có thì ghi UNKNOWN).
- Số liệu trong Kết quả lấy từ `results/`, không từ lần chạy thử.
- `python -m pytest` không có test đỏ.

## Tôi giải thích được
- ☑ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
**Đã làm (24/11/2026).** Trong `src/perceptron.py`: `run` (phần lỗi theo epoch) và các hàm phụ `epoch_error_runs`, `epoch_error_table`, `plot_epoch_errors`, `_zscore_fit`, `_pad_last`, `_run_std`. Không đổi `pla`, `pocket`, `count_errors` của T006.
- Dữ liệu: train, bỏ `WARMUP_WEEKS` tuần đầu (cùng điều kiện `week_idx >= WARMUP_WEEKS` như `drop_warmup`) → n = 34.440 giờ, 3.507 giờ nhãn +1; 12 biến `WEATHER_COLS`; x̃ = (x, 1). Không đọc val/test.
- Nhãn: `peak_label` với ngưỡng tính trên **cả 209 tuần train** (giống ngưỡng `data_prep.run` in ra), sau đó mới bỏ tuần khởi động. Phi chốt 24/11/2026: giữ 209 tuần.
- Z-score: trung bình và độ lệch chuẩn (chia n) tính trên chính 34.440 giờ này.
- 4 cấu hình: {gốc, z-score} × {duyệt cố định, xáo mỗi epoch}. Khi xáo, chạy 5 hạt giống `config.get_run_seeds()` = 2044..2048. Duyệt cố định không dùng hạt giống nên chỉ chạy 1 lần. `max_epochs = config.PERCEPTRON_MAX_EPOCHS` = 50.
- **ĐLC qua các lần chạy chia n − 1** (ddof = 1, Phi chốt 24/11/2026), áp dụng cho cả bảng và dải ±1 ĐLC trong hình (`_run_std`). Duyệt cố định chỉ có 1 lần chạy nên n − 1 = 0, công thức không xác định; cấu hình này tất định (hạt giống nào cũng ra cùng kết quả) nên ghi ĐLC = 0 thay vì NaN.
- Lệnh: `python run_all.py --only perceptron` (≈ 480 s, chủ yếu do Pocket đếm lại lỗi trên toàn tập sau mỗi lần cập nhật).
- Đầu ra: `results/figures/4_1_pla_pocket_epoch_error.png`, `results/tables/4_1_pla_pocket_epoch_error.csv`; truy vết ở `docs/trace_viet.md`.

**Số liệu** (từ `results/tables/4_1_pla_pocket_epoch_error.csv`, số lỗi ở epoch 50 trên n = 34.440):

| Dữ liệu | Thứ tự | Số lần chạy | PLA (TB ± ĐLC) | Pocket (TB ± ĐLC) | Pocket (% lỗi) |
|---|---|---|---|---|---|
| gốc | cố định | 1 | 4105 ± 0 | 3506 ± 0 | 10,18 |
| gốc | xáo | 5 | 5742,4 ± 2522,09 | 3500,2 ± 3,03 | 10,16 |
| z-score | cố định | 1 | 5776 ± 0 | 3341 ± 0 | 9,70 |
| z-score | xáo | 5 | 4492,4 ± 1143,12 | 3248,2 ± 6,69 | 9,43 |

- PLA **hết 50 epoch** ở cả 12 lần chạy (`pla_so_lan_ve_0_loi` = 0) và số lỗi dao động mạnh giữa các epoch; Pocket không tăng và chững lại sau vài epoch.
- Nhận xét để Phi/Huấn cân nhắc: luôn đoán −1 thì sai đúng 3.507 giờ, nên Pocket trên dữ liệu gốc (3.506; 3.500,2) gần như không hơn cách đoán đó. Z-score giúp Pocket giảm còn khoảng 3.250–3.340 lỗi.
- Khả tách: **UNKNOWN**. PLA không về 0 lỗi sau 50 epoch, nhưng 50 epoch chưa chắc "đủ lớn" để kết luận. Kết luận cần bài toán LP (`check_separable_lp`, B4.2, chưa giao).
- Test: thêm 6 test vào `tests/test_perceptron_viet.py` (z-score, cách nối hạt giống với pla/pocket, kéo dài khi PLA dừng sớm, bảng khớp dữ liệu chạy, ĐLC chia n − 1, ghi PNG). `python -m pytest`: 117 passed, 3 skipped (MLP, `lda_two_class`, không thuộc task này), 0 đỏ.

Tự kiểm hiểu (model hỏi): epoch_error_runs | qua | 24/11/2026
Tự kiểm hiểu (model hỏi): epoch_error_table | qua | 24/11/2026
Tự kiểm hiểu (model hỏi): plot_epoch_errors | qua | 24/11/2026
Tự kiểm hiểu (model hỏi): run | qua | 24/11/2026
(Đã hỏi 3 câu: duyệt cố định với xáo và ĐLC, `_pad_last`, z-score/rò rỉ và vì sao PLA dao động còn Pocket không tăng. Sửa nhỏ: đổi test còn 2 hạt giống, E = 3, dự đoán shape (2, 3) và (1, 3), chạy pytest xanh, chỉ đúng dòng `np.array(pla_rows)` quyết định mảng 2D, rồi trả test về như cũ.)

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
