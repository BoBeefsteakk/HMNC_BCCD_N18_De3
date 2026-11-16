# HMNC_BCCD_N18_De3 — Đề 3: Dự báo phụ tải điện hệ thống theo giờ cho tuần tới

Báo cáo chuyên đề học phần **Học máy nâng cao (004295)**, Trường Đại học Điện Lực. Dữ liệu: Panama, 48.048 bản ghi theo giờ
(03/01/2015 – 27/06/2020), so sánh với dự báo chính thức của CND.

> **Làm việc nhóm: đọc `TEAM.md` trước.** Trạng thái: khung ban đầu. Mã nhóm G = 18, SEED = 2044 (`src/config.py`). Phần lõi trong `src/` còn là stub.

## Môi trường
Python 3.12 (phát triển trên 3.12.10), thư viện trong `requirements.txt`.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows;  Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## Tải dữ liệu
Nguồn: Mendeley Data, doi:10.17632/byx7sztj59.1 (CC BY 4.0), không cần đăng nhập. Dữ liệu không nộp kèm; chỉ nộp script tải.

```bash
python data/download_data.py
```

Mendeley có thể trả HTTP 403 cho client Python. Khi đó script không tải tự động mà in sẵn đường dẫn: tải tay bằng trình duyệt
hoặc `curl -L -o <đích> <url>` vào `data/raw/` (tên tệp đích: `continuous.csv`, `forecast_cnd.csv`), rồi chạy lại
`python data/download_data.py` để kiểm tra kích thước và SHA-256.

| Tệp | Kích thước (byte) | SHA-256 |
|---|---|---|
| `continuous dataset.csv` | 10.524.179 | `ef52f68fc8989d02ff2f2565134014eaf9707318a8389d4022cd38d44656fbce` |
| `weekly pre-dispatch forecast.csv` | 929.119 | `002a40a01b7d7209ae791bb85d7ad2f9c9b5a49754e30e09258e56805b805dac` |

Ngày tải: _điền khi chạy lần đầu_.

## Chạy lại toàn bộ kết quả
```bash
# G = 18 đã đặt sẵn trong src/config.py (SEED = 2044)
python run_all.py               # phát triển (train/val)
python run_all.py --final       # chạy cuối, mở tập kiểm tra đúng một lần
python -m pytest                # kiểm tra cấu trúc, quy tắc 72 giờ, hành vi các phần tự cài đặt
```
Thời gian chạy ước tính: _điền sau_ (giới hạn của đề: 60 phút).

## Cấu trúc
```
run_all.py            chạy lại mọi kết quả
data/download_data.py tải dữ liệu, in kích thước + SHA-256
src/config.py         hằng số của đề (chia tuần, SEED, tệp dữ liệu)
src/guards.py         quy tắc 72 giờ + khóa "tập kiểm tra chỉ dùng một lần"
src/data_prep.py      B1   src/optim_linear.py B3   src/perceptron.py B4   src/mlp.py B5
src/features.py       B6 (PCA, LDA)   src/evaluate.py B9   src/hand_calc.py B7
tests/                pytest; phần tự cài đặt còn stub thì SKIP
results/figures|tables  hình, bảng sinh từ mã (tên theo số hình/bảng trong báo cáo)
```

## Ánh xạ tệp kết quả với hình, bảng trong báo cáo
_Điền dần khi có kết quả (nguồn cho Phụ lục D)._

| Hình / Bảng | Tệp sinh ra | Hàm / ô notebook |
|---|---|---|
