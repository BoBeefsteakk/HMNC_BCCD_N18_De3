---
id: T004
title: Từ điển dữ liệu
phase: P1
checklist: B1.2
owner: huan
status: todo
due: 21/11/2026
files: docs/DATA_DICTIONARY.md,docs/trace_huan.md
depends: -
---
# T004 — Từ điển dữ liệu

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Từ điển dữ liệu đủ mọi cột trong `src/config.py`: tên, ý nghĩa, đơn vị, kiểu, thang đo; ghi nguồn.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/config.py` (TARGET_COL, WEATHER_COLS, CALENDAR_COLS, TIME_COL)
- `data/raw/columns_metadata.pdf` (tải: `python data\download_data.py --with-pdf`)
- Quan sát trực tiếp `data/raw/continuous.csv`


## Không được làm
- Không để AI viết thay phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA).
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `docs/DATA_DICTIONARY.md` có đủ mọi cột trong config (12 biến thời tiết, 3 cột lịch, `datetime`, `nat_demand`), mỗi cột đủ 5 trường: tên, ý nghĩa, đơn vị, kiểu, thang đo.
- Mỗi dòng ghi nguồn (trang PDF hoặc quan sát dữ liệu); chỗ không biết ghi `UNKNOWN: hỏi Phi`.
- `docs/trace_huan.md` có dòng truy vết nếu có hình/bảng.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
