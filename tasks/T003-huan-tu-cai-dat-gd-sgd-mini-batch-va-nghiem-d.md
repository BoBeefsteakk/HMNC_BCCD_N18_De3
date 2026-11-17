---
id: T003
title: Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge
phase: P2
checklist: B3.1,B3.2
owner: huan
status: todo
due: 25/11/2026
files: src/optim_linear.py
depends: -
---
# T003 — Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `mse_l2_loss`, `mse_l2_grad`, `gd`, `ridge_closed_form`, `finite_diff_check`, `sgd`, `minibatch_gd`, `momentum_gd` theo docstring `src/optim_linear.py`; thử trên dữ liệu tổng hợp rồi dữ liệu thật sau khi T001 merge.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/optim_linear.py` (docstring: công thức J, grad, chữ ký hàm)
- `docs/CONVENTIONS.md` mục 2, 3
- `tests/test_interfaces.py` (các test_b3_*; KHÔNG sửa file này)
- `docs/HUAN.md`


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b3_*` trong `tests/test_interfaces.py` xanh, KHÔNG SKIP.
- `finite_diff_check` ≤ 1e-6 (float64) cho `mse_l2_loss`/`mse_l2_grad`.
- `ridge_closed_form` khớp nghiệm của `gd` hội tụ trên dữ liệu tổng hợp (ghi sai số trong Kết quả).
- Chạy thử trên dữ liệu thật sau khi T001 merge; ghi kết quả vào Kết quả.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
