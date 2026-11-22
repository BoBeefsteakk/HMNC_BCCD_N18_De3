---
id: T011
title: Hình lỗi theo epoch của PLA và Pocket
phase: P2
checklist: B4.3
owner: viet
status: todo
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
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
Tự kiểm hiểu (model hỏi): (mỗi hàm AI viết một dòng: `<hàm> | qua | <ngày>`; không có hàm AI viết thì ghi "không có")

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
