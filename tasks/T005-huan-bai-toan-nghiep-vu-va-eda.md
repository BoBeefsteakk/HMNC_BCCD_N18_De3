---
id: T005
title: Bài toán nghiệp vụ và EDA
phase: P2
checklist: B1.1,B1.3
owner: huan
status: todo
due: 26/11/2026
files: notebooks/huan_eda.ipynb,results/figures,docs/trace_huan.md
depends: T001
---
# T005 — Bài toán nghiệp vụ và EDA

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Phát biểu bài toán nghiệp vụ (ai dùng, quyết định gì, chi phí sai), chọn chỉ số chính MAPE và nêu lý do, làm EDA ≥ 4 hình mỗi hình ≥ 1 nhận xét định lượng, phát hiện ≥ 1 vấn đề dữ liệu và cách xử lý.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `docs/DE3.md` (B1.1, B1.3), `docs/CONVENTIONS.md` mục 4, 5
- `src/data_prep.py` sau khi T001 merge; `docs/DATA_DICTIONARY.md` (T004)
- `docs/HUAN.md`


## Không được làm
- Không để AI viết thay phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA).
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `notebooks/huan_eda.ipynb` chạy từ đầu đến cuối, chỉ gọi hàm trong `src/`, đã XÓA output trước khi commit.
- ≥ 4 hình đặt tên `results/figures/1_<số>_*.png`, có tên trục và đơn vị, mỗi hình ≥ 1 nhận xét có con số.
- ≥ 1 vấn đề dữ liệu được nêu cùng cách xử lý.
- Mỗi hình có một dòng trong `docs/trace_huan.md`.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
