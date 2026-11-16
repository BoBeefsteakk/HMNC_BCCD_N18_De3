"""B1 – đọc, làm sạch, chia dữ liệu theo tuần Thứ Bảy -> Thứ Sáu.

Khối chấm: B1.2, B1.4 (+ nền cho mọi khối khác).
Đầu vào: data/raw/continuous.csv, data/raw/forecast_cnd.csv  (python data/download_data.py)
Quy định (đề mục 4.4d): chia theo thời gian, KHÔNG xáo trộn; số tuần phải khớp config.EXPECTED_WEEKS.

Hàm cần có:
  load_raw()          đọc CSV, parse datetime, kiểm tra thiếu/trùng giờ, cảnh báo giờ bất thường (< 50% trung vị)
  week_starts(split)  các thời điểm Thứ Bảy 00:00 của từng tuần trong một split (đối chiếu config.SPLITS)
  split_weeks(df)     {train, val, test_a, test_b} -> DataFrame; assert số tuần
  peak_label(y, train_mask)  nhãn +1/-1 "giờ cao điểm": ngưỡng = phân vị 90% TÍNH TRÊN TẬP HUẤN LUYỆN
  align_cnd(...)      căn dự báo CND với phụ tải thực (kiểm tra nhãn thời gian có lệch 1 giờ không)
Lưu ý rò rỉ: mọi phép "học" (ngưỡng phân vị, chuẩn hóa) chỉ khớp trên train (đề mục 3.1d).
"""
from __future__ import annotations


def run(seed: int, final: bool = False) -> None:
    raise NotImplementedError("B1: data_prep")
