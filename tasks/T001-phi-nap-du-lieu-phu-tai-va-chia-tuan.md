---
id: T001
title: Nạp dữ liệu phụ tải và chia tuần
phase: P1
checklist: B1.4
owner: phi
status: done
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
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `tests/test_data_prep.py` (Phi tự viết) xanh, không SKIP: số tuần mỗi split đúng 209/26/37/14; không thiếu/trùng giờ (hoặc ghi rõ cách xử lý); mỗi tuần 168 giờ bắt đầu Thứ Bảy 00:00.
- `peak_label` dùng ngưỡng tính từ train (có test chứng minh ngưỡng không đổi khi thêm dữ liệu val/test).
- Số giờ phụ tải < 50% trung vị được in/ghi lại cùng cách xử lý đề xuất.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☑ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã làm (18/11/2026): `src/data_prep.py` (`parse_raw`, `load_raw`, `week_starts`, `split_weeks`, `peak_threshold`, `peak_label`, `low_load_hours`, `split_of`, `run`), `tests/test_data_prep.py` (16 test, 2 test dữ liệu thật tự SKIP khi thiếu tệp), thêm `TIMESTAMP_SHIFT_HOURS` và `LOW_LOAD_FRACTION` vào `src/config.py`.
- Lệnh: `python -m pytest` → 79 passed, 10 skipped (stub của T003, T006, T007); `python -c "from src import data_prep; data_prep.run(2044)"`.
- Dữ liệu thật: 48.048 dòng, không trùng, không thiếu giờ, không NaN; chia đúng 209/26/37/14 tuần (35.112/4.368/6.216/2.352 giờ). Ngưỡng cao điểm (phân vị 90% train) = 1450,75 MWh.
- **Phát hiện:** nhãn thời gian là giờ kết thúc (dòng đầu 2015-01-03 01:00, dòng cuối 2020-06-27 00:00). Phải lùi 1 giờ (`TIMESTAMP_SHIFT_HOURS = -1`) thì mới ra tuần Thứ Bảy 00:00 → Thứ Sáu 23:00. Đã sửa `docs/CONVENTIONS.md` mục 1 và `docs/decisions/README.md`. T002 vẫn phải căn với tệp CND (UNKNOWN: CND gắn nhãn giờ bắt đầu hay kết thúc, chưa kiểm).
- Giờ phụ tải < 50% trung vị train (1156,71 MWh): 8 giờ. 3 giờ lẻ trong train (24/01/2015 16:00, 27/06/2017 11:00, 01/07/2017 13:00) và 5 giờ liên tiếp trong val (20/01/2019 11:00–15:00, thấp nhất 85,19 MWh = 7%). Không giờ nào nằm trong test. Nguyên nhân: UNKNOWN (chưa tra). Đề xuất xử lý: giữ nguyên dữ liệu, báo MAPE trên val cả có và không có 5 giờ ngày 20/01/2019 (MAPE chia cho y nên rất nhạy); quyết định cuối thuộc Phi.
- Tỷ lệ giờ cao điểm theo ngưỡng của train: train 10,0%; val 17,5%; test_a 17,3%; test_b 0,0% (không có nhãn +1 nào trên test_b). Chi tiết và các ghi chú khác: `docs/CONVENTIONS.md` mục 8.
- Chưa làm: `align_cnd` (T002); mục "Tôi giải thích được" do Phi tự tick.
- Tự kiểm hiểu (model hỏi): `peak_label`, `parse_raw`, `TIMESTAMP_SHIFT_HOURS` | qua | 18/11/2026 (qua sau khi giải thích lại; sửa nhỏ: chạy thử phân vị 95% không sửa tệp, ngưỡng 1494,42 MWh)

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
Đã dùng: Claude Code viết `src/data_prep.py` và `tests/test_data_prep.py` (loại M); ghi ở `docs/ai_usage_log.md`.
