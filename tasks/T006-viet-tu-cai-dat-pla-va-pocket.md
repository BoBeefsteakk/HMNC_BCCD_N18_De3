---
id: T006
title: Tự cài đặt PLA và Pocket
phase: P2
checklist: B4.1
owner: viet
status: todo
due: 25/11/2026
files: src/perceptron.py
depends: -
---
# T006 — Tự cài đặt PLA và Pocket

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `count_errors`, `pla`, `pocket` theo docstring `src/perceptron.py` với quy ước nhãn ±1, x̃ = (x, 1), w̃(0) = 0 và mẫu có y·g ≤ 0 là sai (kể cả g = 0).


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/perceptron.py` (docstring)
- `docs/CONVENTIONS.md` mục 3
- `tests/test_interfaces.py` (các test_b4_*; KHÔNG sửa)
- `docs/VIET.md`


## Không được làm
- Không để AI viết thay phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA).
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b4_*` trong `tests/test_interfaces.py` xanh, KHÔNG SKIP.
- Nêu rõ thứ tự duyệt và điều kiện dừng trong Kết quả (cần cho báo cáo B4.1).
- `pocket` trả về w có số lỗi trên tập huấn luyện không lớn hơn `pla` trên dữ liệu thử.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
