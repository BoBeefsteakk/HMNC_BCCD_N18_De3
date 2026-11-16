---
id: T007
title: Tự cài đặt Fisher score và PCA
phase: P2
checklist: B6.1,B6.3
owner: viet
status: todo
due: 27/11/2026
files: src/features.py
depends: -
---
# T007 — Tự cài đặt Fisher score và PCA

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `fisher_score` và `pca` (trị riêng ma trận hiệp phương sai chia n−1, hoặc SVD) trên dữ liệu tổng hợp.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/features.py` (docstring)
- `docs/CONVENTIONS.md` mục 2
- `tests/test_interfaces.py` (các test_b6_*; KHÔNG sửa)
- `docs/VIET.md`


## Không được làm
- Không để AI viết thay phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA).
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b6_pca_*` xanh, KHÔNG SKIP.
- Trị riêng khớp `sklearn.decomposition.PCA` đến 1e-6 (sklearn chỉ dùng để đối chứng).
- `fisher_score` có kiểm tra trên dữ liệu tổng hợp mà bạn tự tính tay được.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
