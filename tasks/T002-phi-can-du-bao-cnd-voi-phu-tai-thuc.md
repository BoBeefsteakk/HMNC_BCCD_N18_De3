---
id: T002
title: Căn dự báo CND với phụ tải thực
phase: P1
checklist: B1.4,R2
owner: phi
status: todo
due: 22/11/2026
files: src/data_prep.py,tests/test_data_prep.py
depends: T001
---
# T002 — Căn dự báo CND với phụ tải thực

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Nạp `data/raw/forecast_cnd.csv`, kiểm tra nhãn thời gian có lệch 1 giờ so với tệp phụ tải không (thử dịch −1/0/+1 giờ, chọn theo MAPE trên tập kiểm định), viết `align_cnd`, và ghi kết luận vào mục UNKNOWN ở `docs/CONVENTIONS.md` mục 1.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/data_prep.py`, `src/config.py`
- `docs/CONVENTIONS.md` mục 1 (UNKNOWN) và mục 4 (MAPE)
- Kết quả T001 (đã merge)


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Bảng MAPE trên tập kiểm định cho ba độ dịch −1/0/+1 giờ; chọn độ dịch bằng số liệu này.
- KHÔNG dùng tập kiểm tra (test_a, test_b) để chọn độ dịch.
- `align_cnd` có test trong `tests/test_data_prep.py`, xanh không SKIP.
- Mục UNKNOWN trong `docs/CONVENTIONS.md` mục 1 được thay bằng kết luận kèm số liệu.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
