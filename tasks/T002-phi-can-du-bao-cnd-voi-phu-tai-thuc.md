---
id: T002
title: Căn dự báo CND với phụ tải thực
phase: P1
checklist: B1.4,R2
owner: phi
status: review
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
- ☑ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã làm (18/11/2026): `src/data_prep.py` thêm `load_cnd`, `align_cnd`, `cnd_mape`, `select_cnd_shift`; `tests/test_data_prep.py` thêm 10 test (CND giả có nhãn lệch biết trước nên kiểm được hàm chọn đúng độ dịch; 1 test dữ liệu thật tự SKIP khi thiếu tệp); `src/config.py` thêm `CND_TIME_FORMAT`, `CND_SHIFT_CANDIDATES`, `CND_SHIFT_HOURS`.
- Lệnh: `python -m pytest` → 92 passed, 10 skipped (stub của T003, T006, T007 và MLP); `python -c "from src import data_prep; data_prep.run(2044)"`.
- **Bảng MAPE của CND trên tập kiểm định (26 tuần, 4.368 giờ, chỉ dùng val):**

| Độ dịch nhãn CND | MAPE |
|---|---|
| −1 giờ | **4,70%** |
| 0 giờ | 5,77% |
| +1 giờ | 8,31% |

  Thử rộng −3…+3 (chỉ chẩn đoán trên val): −3 8,70%; −2 6,21%; −1 4,70%; 0 5,77%; +1 8,31%; +2 10,92%; +3 13,38% → đáy rõ ở −1, không phải đáy giả ở biên. Chọn **−1** (`CND_SHIFT_HOURS`). Tập kiểm tra (test_a, test_b) không dùng để chọn; `select_cnd_shift` còn chặn dữ liệu ngoài val bằng `ValueError`.
- Ý nghĩa: nhãn CND trùng nhãn gốc (giờ kết thúc) của tệp phụ tải. Bằng chứng độc lập: PDF của tác giả ghi điểm chia tuần lúc Thứ Bảy 01:00. Đã thay UNKNOWN ở `docs/CONVENTIONS.md` mục 1 và ghi `docs/decisions/README.md`.
- Tệp CND: 40.152 giờ, 239 tuần đủ giờ, không trùng, không thiếu; phủ trọn val, test_a, test_b. **72 giờ CND bằng 0** (nhãn 12/02/2016 đến 20/11/2016, theo giờ bắt đầu), toàn bộ trong train, không nằm trong val hay test. Cách xử lý: giữ nguyên trong tệp, không dùng CND để huấn luyện; CND chỉ là mô hình so sánh trên val/test nên không ảnh hưởng MAPE báo cáo.
- Lưu ý cho R2: MAPE của CND trên val gồm tuần có sự cố 20/01/2019 (tuần thứ 3 của val, phụ tải thấp nhất 85 MWh). Bỏ tuần đó thì MAPE của CND là 4,06% (thay vì 4,70%); mô hình của nhóm cũng phải báo cả hai cách để so công bằng.
- UNKNOWN: vì sao tệp CND bắt đầu ở Thứ Bảy 00:00 chứ không phải 01:00 (giả thuyết chưa kiểm: giờ 24 của Thứ Sáu trước trong báo cáo CND). Không ảnh hưởng độ dịch chọn.
- Sửa ngoài `files:` của T002 (do Phi sở hữu): `src/config.py`, `docs/CONVENTIONS.md`, `docs/decisions/README.md`, docstring `src/guards.py`.
- Tự kiểm hiểu (model hỏi): select_cnd_shift, align_cnd | qua | 18/11/2026
- Chưa làm: mục "Tôi giải thích được" do Phi tự tick.

## Ghi chú AI đã dùng
Nếu dùng AI (kể cả hỏi khái niệm): thêm MỘT dòng vào `docs/ai_usage_log.md` (ngày | công cụ | việc | tệp/phần báo cáo | người). Không dùng AI thì ghi "không".
Đã dùng: Claude Code viết `load_cnd`, `align_cnd`, `cnd_mape`, `select_cnd_shift` và test (loại M); ghi ở `docs/ai_usage_log.md`.
