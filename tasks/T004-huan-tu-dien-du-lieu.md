---
id: T004
title: Từ điển dữ liệu
phase: P1
checklist: B1.2
owner: huan
status: review
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
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `docs/DATA_DICTIONARY.md` có đủ mọi cột trong config (12 biến thời tiết, 3 cột lịch, `datetime`, `nat_demand`), mỗi cột đủ 5 trường: tên, ý nghĩa, đơn vị, kiểu, thang đo.
- Mỗi dòng ghi nguồn (trang PDF hoặc quan sát dữ liệu); chỗ không biết ghi `UNKNOWN: hỏi Phi`.
- `docs/trace_huan.md` có dòng truy vết nếu có hình/bảng.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- [x] Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã khảo sát và lập từ điển dữ liệu đầy đủ cho 17 biến trong `continuous.csv` (phụ tải nat_demand, 12 biến thời tiết ở 3 trạm Tocumen, Santiago, David, và 3 biến lịch) cùng 2 biến trong tệp dự báo `forecast_cnd.csv`.
- Mỗi biến đều có đủ 5 tiêu chí bắt buộc: tên cột, ý nghĩa nghiệp vụ/vật lý, đơn vị đo, kiểu dữ liệu, thang đo đo lường, kèm nguồn trích dẫn từ `columns_metadata.pdf` (trang 1 và 2) và quan sát trực tiếp dữ liệu thật.
- Bổ sung bảng tra cứu chi tiết 22 ngày lễ cho mã `Holiday_ID` (1..22) theo tài liệu của tác giả.
- Bổ sung bảng thống kê mô tả định lượng (min, mean, std, max, null count) tính từ toàn bộ 48.048 dòng dữ liệu `continuous.csv` và 40.152 dòng `forecast_cnd.csv`.
- Phân tích dải số thực nghiệm biến `QV2M` (gắn nhãn suy luận nhóm từ thực nghiệm dải 0,010–0,023) và khảo sát chi tiết 72 giờ CND bằng 0 (chia làm 2 đoạn 24 giờ và 48 giờ đều trong tập train năm 2016, val/test bằng 0 nên không ảnh hưởng R2); 8 giờ phụ tải thấp bất thường (ghi nhận hiện tượng, nguyên nhân UNKNOWN).
- Khởi tạo bảng truy vết `docs/trace_huan.md` cho Bảng 1.1.
- Chạy `pytest` đạt 92 passed, 0 failed; `scripts/tasks.py check` đạt 10 task, 0 lỗi; `scripts/ai_log.py check` đạt 17 dòng hợp lệ.

## Ghi chú AI đã dùng
Đã thêm 1 dòng vào `docs/ai_usage_log.md` (loại D: đối chiếu số liệu và trích xuất siêu dữ liệu).
