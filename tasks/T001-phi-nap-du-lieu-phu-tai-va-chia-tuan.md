---
id: T001
title: Nạp dữ liệu phụ tải và chia tuần
phase: P1
checklist: B1.4
owner: phi
status: todo
due: 20/11/2026
files: src/data_prep.py,tests/test_data_prep.py
depends: -
---
# T001 — Nạp dữ liệu phụ tải và chia tuần

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Nạp `data/raw/continuous.csv` (parse datetime, kiểm thiếu/trùng giờ); `week_starts`/`split_weeks` chia đúng `config.SPLITS` và assert 209/26/37/14 tuần; `peak_label` với ngưỡng phân vị 90% tính trên train; cảnh báo giờ phụ tải < 50% trung vị.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/data_prep.py` (docstring nêu hàm cần có), `src/config.py` (SPLITS, EXPECTED_WEEKS, PEAK_QUANTILE, TARGET_COL, TIME_COL)
- `docs/CONVENTIONS.md` mục 1, 3, 4; `tests/test_split_spec.py`
- Dữ liệu: `python data\download_data.py`


## Không được làm
- Không để AI viết thay phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA).
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `tests/test_data_prep.py` (Phi tự viết) xanh, không SKIP: số tuần mỗi split đúng 209/26/37/14; không thiếu/trùng giờ (hoặc ghi rõ cách xử lý); mỗi tuần 168 giờ bắt đầu Thứ Bảy 00:00.
- `peak_label` dùng ngưỡng tính từ train (có test chứng minh ngưỡng không đổi khi thêm dữ liệu val/test).
- Số giờ phụ tải < 50% trung vị được in/ghi lại cùng cách xử lý đề xuất.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
