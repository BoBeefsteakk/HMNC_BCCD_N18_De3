"""Cấu hình trung tâm (Đề 3 – dự báo phụ tải điện Panama theo giờ cho tuần tới).

Mọi hằng số lấy từ đề bài đặt ở đây, kèm mục trích dẫn trong đề. Không rải số "ma thuật" ở nơi khác.
Đổi một hằng số ở đây = đổi quyết định của nhóm → ghi vào docs/decisions/.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RESULTS_DIR = ROOT / "results"
FIG_DIR = RESULTS_DIR / "figures"
TABLE_DIR = RESULTS_DIR / "tables"

# --- Mã nhóm và hạt giống (đề mục 2.1) ------------------------------------------------------------
# Mã nhóm G = 18 (cột "Nhóm" trên sheet đăng ký đề của lớp, xem ngày 17/11/2026) -> SEED = 2044.
# Biến môi trường BCCD_G chỉ để thử nghiệm; KHÔNG dùng cho kết quả báo cáo.
GROUP_ID: int | None = int(os.environ["BCCD_G"]) if os.environ.get("BCCD_G") else 18


def seed_for(group_id: int) -> int:
    """SEED = 2026 + G (đề mục 2.1; ví dụ nhóm 07 -> 2033)."""
    return 2026 + group_id


def get_seed() -> int:
    if GROUP_ID is None:
        raise RuntimeError("Chưa điền mã nhóm G: đặt biến môi trường BCCD_G hoặc sửa src/config.py (GROUP_ID).")
    return seed_for(GROUP_ID)


# --- Dữ liệu (đề mục 4.4b; dataset [8], CC BY 4.0) ------------------------------------------------
MENDELEY_URL = "https://data.mendeley.com/public-files/datasets/byx7sztj59/files/{file_id}/file_downloaded"
DATA_FILES = {
    "continuous": {
        "remote_name": "continuous dataset.csv",
        "local_name": "continuous.csv",
        "file_id": "94ef3285-7ce4-43e2-9fd3-9cb3f592b89c",
        "size": 10524179,
        "sha256": "ef52f68fc8989d02ff2f2565134014eaf9707318a8389d4022cd38d44656fbce",
    },
    "forecast": {
        "remote_name": "weekly pre-dispatch forecast.csv",
        "local_name": "forecast_cnd.csv",
        "file_id": "1339c5ea-adbc-4c6e-8e64-c64c1ba20d54",
        "size": 929119,
        "sha256": "002a40a01b7d7209ae791bb85d7ad2f9c9b5a49754e30e09258e56805b805dac",
    },
    "metadata_pdf": {  # tùy chọn: mô tả cột và 14 cặp tuần huấn luyện/kiểm tra của tác giả
        "remote_name": "Columns' metadata and train-test splits details.pdf",
        "local_name": "columns_metadata.pdf",
        "file_id": "6952a984-f474-437f-8640-67d773caea93",
        "size": 2493045,
        "sha256": "72ff24ce15096b51b86985f1abd9b78e6bacbf4211d1638de308c2c4a66281ae",
    },
}

TARGET_COL = "nat_demand"  # phụ tải toàn quốc theo giờ (MWh)
TIME_COL = "datetime"
WEATHER_COLS = [  # 4 biến x 3 thành phố = 12 biến thời tiết (đề mục 4.4d, B6)
    f"{v}_{c}" for c in ("toc", "san", "dav") for v in ("T2M", "QV2M", "TQL", "W2M")
]
CALENDAR_COLS = ["Holiday_ID", "holiday", "school"]

# --- Chia dữ liệu theo tuần Thứ Bảy -> Thứ Sáu (đề mục 4.4d, B1.4) -------------------------------
SPLITS = {
    "train": ("2015-01-03", "2019-01-04"),
    "val": ("2019-01-05", "2019-07-05"),
    "test_a": ("2019-07-06", "2020-03-20"),  # trước phong tỏa
    "test_b": ("2020-03-21", "2020-06-26"),  # trong phong tỏa (bắt đầu 25/03/2020 theo [7])
}
EXPECTED_WEEKS = {"train": 209, "val": 26, "test_a": 37, "test_b": 14}

HOURS_PER_WEEK = 168
PEAK_QUANTILE = 0.90  # bài toán phụ "giờ cao điểm cần cảnh báo": y=+1 nếu tải > phân vị 90% của TẬP HUẤN LUYỆN
BASELINE_LAG_HOURS = 336  # mô hình cơ sở: phụ tải cùng giờ cách đây 2 tuần

# --- Quyết định của nhóm (docs/decisions/, 17/11/2026) ---------------------------------------------
N_RUN_SEEDS = 5  # B4.3 (>= 5 hạt giống): SEED, SEED+1, ..., SEED+4 (xem get_run_seeds)
PERCEPTRON_MAX_EPOCHS = 50  # B4.3: số epoch tối đa của PLA/Pocket trong thí nghiệm (như slide Chương 2, hình 50 epoch)
BOOTSTRAP_ITERS = 2000  # B9.1 (>= 1.000 lần); lấy lại mẫu THEO TUẦN vì các giờ liền nhau tương quan
BOOTSTRAP_CI = 0.95  # khoảng tin cậy kiểu phân vị (2,5% và 97,5%)
TREF_QUANTILES = (0.10, 0.25, 0.50, 0.75, 0.90)  # lưới Tref cho CDH: phân vị của T trung bình 3 thành phố trên TRAIN
FEATURE_LAGS_HOURS = (336, 504, 672)  # trễ phụ tải và cửa sổ trượt: cùng giờ của tuần 2, 3, 4 trước (đều >= 240 giờ)
# Khởi động (18/11/2026): trễ xa nhất cần ngần ấy tuần lịch sử, nên các tuần đầu của train chỉ làm lịch sử, không huấn luyện.
WARMUP_WEEKS = -(-max(FEATURE_LAGS_HOURS) // HOURS_PER_WEEK)  # = 4, làm tròn lên


def get_run_seeds() -> list[int]:
    """N_RUN_SEEDS hạt giống liên tiếp bắt đầu từ SEED (nhóm 18: 2044..2048), cho thí nghiệm lặp (B4.3)."""
    base = get_seed()
    return [base + i for i in range(N_RUN_SEEDS)]

# --- Phát hiện khi làm T001 (18/11/2026) ----------------------------------------------------------
# continuous.csv có 48.048 dòng = 286 tuần x 168 giờ đúng từng giờ, nhưng dòng đầu là 2015-01-03 01:00 và dòng
# cuối là 2020-06-27 00:00 -> nhãn thời gian là GIỜ KẾT THÚC. Lùi 1 giờ để về giờ bắt đầu thì mọi tuần tròn
# Thứ Bảy 00:00 -> Thứ Sáu 23:00 và khớp 209/26/37/14. T002 vẫn phải đối chiếu với tệp dự báo CND.
TIMESTAMP_SHIFT_HOURS = -1
LOW_LOAD_FRACTION = 0.5  # giờ phụ tải thấp bất thường: < 50% trung vị (CONVENTIONS mục 4)

# --- T002 (18/11/2026): căn dự báo CND với phụ tải thực -------------------------------------------------
# Tệp CND dùng định dạng ngày M/D/YYYY (vd "1/2/2016 0:00" = Thứ Bảy 02/01/2016). Dịch nhãn CND để khớp nhãn giờ bắt đầu
# của phụ tải (đã lùi TIMESTAMP_SHIFT_HOURS): thử CND_SHIFT_CANDIDATES trên tập KIỂM ĐỊNH, chọn theo MAPE nhỏ nhất.
# Kết quả (T002): -1 giờ, tức nhãn CND trùng nhãn gốc (giờ kết thúc) của tệp phụ tải.
CND_TIME_FORMAT = "%m/%d/%Y %H:%M"
CND_SHIFT_CANDIDATES = (-1, 0, 1)
CND_SHIFT_HOURS = -1

# --- B3: Hồi quy tuyến tính và tối ưu hóa (B3.1–B3.4) --------------------------------------------
B3_LAMBDA: float = 0.1          # Hệ số chính quy hóa L2 (Ridge)
B3_ETA: float = 0.05            # Tốc độ học (learning rate) cho GD và Momentum GD
B3_N_ITER: int = 500            # Số bước lặp tối đa
B3_MOMENTUM_BETA: float = 0.85  # Hệ số quán tính Polyak momentum
