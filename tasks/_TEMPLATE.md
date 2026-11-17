---
id: T000
title: Tiêu đề ngắn của task
phase: P1
checklist: B1.1
owner: phi
status: todo
due: 01/01/2026
files: src/ten_file.py
depends: -
---
# T000 — Tiêu đề ngắn của task

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
(1–3 dòng: task này tạo ra cái gì, phục vụ mục checklist nào.)

## Đầu vào cần đọc
- `TEAM.md`, `docs/<TÊN>.md`, `docs/CONVENTIONS.md`, `src/config.py`
- (thêm file/mục cụ thể cho task này)

## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- (tiêu chí kiểm được; ưu tiên: test nào phải xanh KHÔNG SKIP, hình/bảng nào phải có)
- `python -m pytest` không có test đỏ.

## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
Tự kiểm hiểu (model hỏi): (mỗi hàm AI viết một dòng: `<hàm> | qua | <ngày>`; không có hàm AI viết thì ghi "không có")

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
