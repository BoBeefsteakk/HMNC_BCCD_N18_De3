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

## Checklist (cố định theo phase)
Tóm tắt từ [`docs/CHECKLIST.md`](docs/CHECKLIST.md) (nguồn đầy đủ, có điều kiện được điểm; chỉ Phi sửa, Phi đổi ☐ → ☑ khi có bằng chứng). Mã khớp mã chấm của đề, tổng Phần I = 10,0. Task hằng ngày nằm ở [`tasks/`](tasks/README.md).

| Phase | Hạn |
|---|---|
| P1 Dữ liệu | 22/11/2026 |
| P2 Tiến độ (nộp báo cáo 2–3 trang) | 30/11/2026 |
| P3 Lõi | 14/12/2026 |
| P4 Đánh giá (`run_all.py --final`, một lần) | 20/12/2026 |
| P5 Nộp hồ sơ | 25/12/2026 (vấn đáp 30/12) |

| Phase | Mã | Việc | Người | Điểm | ☐ |
|---|---|---|---|---|---|
| P1 | B1.1 | Bài toán nghiệp vụ, chỉ số chính (MAPE) | Huấn | 0,25 | ☐ |
| P1 | B1.2 | Mô tả dữ liệu, từ điển dữ liệu | Huấn | 0,25 | ☐ |
| P1 | B1.4 | Tiền xử lý, chia 209/26/37/14 tuần | Phi | 0,25 | ☐ |
| P2 | TĐ | Báo cáo tiến độ 2–3 trang (không nộp: −0,5) | Phi tổng hợp | − | ☐ |
| P2 | B1.3 | EDA ≥ 4 hình có nhận xét | Huấn | 0,25 | ☐ |
| P2 | B3.1 | GD, SGD, mini-batch tự cài đặt | Huấn | 0,5 | ☐ |
| P2 | B3.2 | Momentum, so với GD | Huấn | 0,25 | ☐ |
| P2 | B3.4 | Kiểm tra gradient ≤ 1e-6, đối chiếu nghiệm giải tích | Huấn | 0,25 | ☐ |
| P2 | B4.1 | PLA, Pocket tự cài đặt | Việt | 0,25 | ☐ |
| P3 | B2.1 | Lý thuyết (mỗi người viết phần khối mình) | cả nhóm | 0,5 | ☐ |
| P3 | B2.2 | Suy dẫn LDA hai lớp tự viết | Việt | 0,25 | ☐ |
| P3 | B3.3 | Thí nghiệm η (≥ 4 giá trị), z-score | Huấn | 0,25 | ☐ |
| P3 | B4.2 | Kiểm tra khả tách tuyến tính (LP) | Việt | 0,25 | ☐ |
| P3 | B4.3 | Lỗi theo epoch, ≥ 5 hạt giống | Việt | 0,25 | ☐ |
| P3 | B5.1 | MLP forward/backward tự cài đặt | Phi | 0,5 | ☐ |
| P3 | B5.2 | Kiểm tra gradient MLP ≤ 1e-6, ≥ 2 kiến trúc | Phi | 0,25 | ☐ |
| P3 | B5.3 | Kiến trúc, khởi tạo, kích hoạt | Phi | 0,5 | ☐ |
| P3 | B5.4 | SGD vs momentum, L2, dừng sớm | Phi | 0,5 | ☐ |
| P3 | B5.5 | Đối chứng scikit-learn | Phi | 0,25 | ☐ |
| P3 | B6.1 | Phân tích đặc trưng gốc, Fisher | Việt | 0,25 | ☐ |
| P3 | B6.2 | ≥ 5 đặc trưng mới (trễ ≥ 240 giờ) | Việt | 0,5 | ☐ |
| P3 | B6.3 | PCA tự cài đặt, khớp sklearn 1e-6 | Việt | 0,25 | ☐ |
| P3 | B6.4 | LDA tự cài đặt, chọn đặc trưng ≥ 2 họ | Việt | 0,25 | ☐ |
| P3 | B7.1 | Tính tay GD logistic (a: Huấn) và PLA (b: Việt) | Huấn, Việt | 0,25 | ☐ |
| P3 | B7.2 | Tính tay forward/backward mạng 2–2–1 | Phi | 0,25 | ☐ |
| P3 | B7.3 | Tính tay PCA và LDA | Việt | 0,25 | ☐ |
| P3 | R1 | Giao thức không rò rỉ (bảng độ trễ, thí nghiệm L(h−24), L(h−168)) | Phi | 0,25 | ☐ |
| P3 | R4 | PCA đồ thị ngày, LDA 3 loại ngày, độ nhạy nhiệt độ | Việt | 0,25 | ☐ |
| P4 | B4.4 | So perceptron với tuyến tính và MLP, vùng quyết định | Việt | 0,25 | ☐ |
| P4 | B6.5 | Bảng so sánh gốc / + mới / PCA / chọn đặc trưng | Việt | 0,25 | ☐ |
| P4 | R2 | So với dự báo CND và mô hình cơ sở | Huấn | 0,25 | ☐ |
| P4 | R3 | Sai số theo ngữ cảnh, phong tỏa, thích nghi | Phi | 0,25 | ☐ |
| P4 | B9.1 | Chạy tập kiểm tra một lần, bootstrap ≥ 1.000 lần | Phi | 0,25 | ☐ |
| P5 | B9.2 | Phân tích lỗi, 4 câu hỏi nghiên cứu, khuyến nghị | Phi | 0,25 | ☐ |
| P5 | B10.1 | Cấu trúc, chạy lại ≤ 60 phút, bảng truy vết | Phi | 0,25 | ☐ |
| P5 | HS | Hồ sơ cuối: báo cáo .docx/.pdf, mã, README, slide ≤ 15 trang | Phi tổng hợp | − | ☐ |

Điểm khuyến khích (tối đa 0,5): Adam/Nesterov (Huấn), kiểm định ghép cặp (Phi), tái lập bảng của bài báo [7] (Phi), ứng dụng Streamlit + PSI (tùy chọn).

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
