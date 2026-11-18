# CONVENTIONS — quy ước chung (chỉ Phi sửa)

Mục tiêu: ba người, ba AI vẫn cho ra cùng một định nghĩa, cùng một con số. Thông số số học ở `src/config.py`; file này giữ **định nghĩa và quy ước**. Thấy chỗ mơ hồ → ghi vào task, báo Phi, không tự chọn.

## 1. Thời gian và tuần
- Một tuần dự báo = Thứ Bảy 00:00 → Thứ Sáu 23:00 (168 giờ). `hour_in_week` ∈ [0, 167], 0 = Thứ Bảy 00:00.
- Chia tập theo `config.SPLITS` (209/26/37/14 tuần). Không xáo trộn, không k-fold thường; chỉ kiểm định trượt theo thời gian.
- Quy tắc 72 giờ: chỉ dùng phụ tải đến hết Thứ Ba trước tuần dự báo. Đặc trưng trễ cố định phải có trễ ≥ `guards.min_safe_lag()` = **240 giờ** (336, 504, 672 hợp lệ; 168 chỉ hợp lệ cho 96/168 giờ nên **không dùng**).
- UNKNOWN (cần dữ liệu, Phi kiểm trong T002): nhãn thời gian trong tệp có phải "giờ kết thúc" (lệch 1 giờ so với tệp dự báo CND) hay không. **T001 (18/11/2026) đã có bằng chứng cấu trúc:** `continuous.csv` có 48.048 dòng = 286 tuần × 168 giờ, dòng đầu là 2015-01-03 01:00, dòng cuối là 2020-06-27 00:00, nên nhãn là **giờ kết thúc**; `config.TIMESTAMP_SHIFT_HOURS = -1` đưa về giờ bắt đầu (không lùi thì chia 209/26/37/14 vỡ). **T002 (18/11/2026) kết luận:** nhãn của tệp CND trùng nhãn gốc (giờ kết thúc) của tệp phụ tải, nên `config.CND_SHIFT_HOURS = -1`. MAPE của CND trên tập kiểm định (26 tuần, chỉ dùng val): dịch −1 giờ **4,70%**, dịch 0 giờ 5,77%, dịch +1 giờ 8,31% (thử rộng −3…+3 vẫn có đáy ở −1). Độ dịch chọn bằng `data_prep.select_cnd_shift`, hàm này từ chối dữ liệu ngoài val. Bằng chứng độc lập: PDF mô tả của tác giả ghi các điểm chia tuần lúc Thứ Bảy `01:00`, khớp với "tuần = nhãn Thứ Bảy 01:00 đến Thứ Bảy 00:00". Còn UNKNOWN: vì sao tệp CND bắt đầu ở Thứ Bảy 00:00 chứ không phải 01:00 (giả thuyết, chưa kiểm: giờ 24 của Thứ Sáu trước trong báo cáo CND); không ảnh hưởng kết quả vì độ dịch chọn bằng MAPE.

## 2. Dữ liệu và ký hiệu
- Đích: `nat_demand` (MWh). Thời tiết 12 biến: `{T2M,QV2M,TQL,W2M}_{toc,san,dav}`; lịch: `Holiday_ID, holiday, school`. Đúng tên cột trong `config.py`.
- `X̃ = [X, 1]` (cột 1 ở **cuối**), `w` có d+1 phần tử, hệ số tự do là phần tử cuối. Mọi hàm nhận `X` đã mở rộng trừ khi docstring ghi khác.
- Float64 ở mọi nơi. NumPy thuần cho phần tự cài đặt; không autograd; scikit-learn chỉ để chia/chuẩn hóa/chỉ số/đối chứng.
- Chuẩn hóa: z-score, **khớp trên tập huấn luyện**, áp dụng cho val/test bằng cùng tham số. Biến đích của MLP cũng chuẩn hóa theo train; mọi chỉ số báo cáo trên thang MWh gốc.

## 3. Hàm mất mát, nhãn
- Hồi quy tuyến tính (B3): `J(w) = 1/(2n)·‖X̃w − y‖² + (λ/2)·‖w[:-1]‖²` (không phạt hệ số tự do); `grad = 1/n·X̃ᵀ(X̃w − y) + λ·[w[:-1], 0]`.
- MLP (B5): tầng ra tuyến tính, MSE; kích hoạt ẩn ≥ 2 loại; giao diện như docstring `src/mlp.py`.
- Bài toán phụ "giờ cao điểm": nhãn `+1` nếu `nat_demand` > phân vị 90% **của tập huấn luyện** (`config.PEAK_QUANTILE`), ngược lại `−1`. PLA/Pocket dùng ±1; hồi quy logistic ở B7.1 và mạng 2–2–1 (sigmoid + BCE) ở B7.2 đều dùng {0, 1} (đổi bằng `(y+1)/2`; mẫu thứ nhất là mẫu lớp +1 nên y = 1).
- PLA: `x̃ = (x, 1)`, `w̃(0) = 0`, mẫu có `y·g ≤ 0` là sai (kể cả g = 0).

## 4. Chỉ số
- **MAPE** của một tuần = trung bình theo 168 giờ của `|y − ŷ| / y`; chỉ số chính = trung bình MAPE các tuần kiểm tra. Báo cáo riêng (a) 37 tuần và (b) 14 tuần.
- Phụ: MAE, RMSE (MWh), sai số đỉnh/đáy/năng lượng tuần. Chỉ số kỹ năng = `1 − MAPE_mô_hình / MAPE_cơ_sở`.
- Mô hình cơ sở: trễ 336 giờ; trung bình cùng giờ các tuần thứ 2, 3, 4 trước; dự báo CND.
- Giờ phụ tải thấp bất thường (< 50% trung vị): đánh dấu và nêu cách xử lý (MAPE nhạy với chúng).

## 5. Đặt tên và nơi lưu
- Hình: `results/figures/<chương>_<số>_<mô_tả>.png`, ví dụ `4_2_lr_sweep.png`. Bảng: `results/tables/<chương>_<số>_<mô_tả>.csv`. Chương: 1 tổng quan/dữ liệu, 2 lý thuyết, 3 đặc trưng, 4 tuyến tính + perceptron, 5 MLP, 6 đánh giá. Số hình/bảng khớp số trong báo cáo; đồ thị có tên trục và đơn vị.
- Mỗi hình/bảng ghi 1 dòng vào file truy vết **của mình** `docs/trace_<tên>.md` (huan | viet | phi): số hình/bảng | tệp | hàm hoặc ô notebook | mã task. Cuối kỳ Phi ghép thành Phụ lục D.
- Mã quan trọng nằm trong `src/`; notebook chỉ gọi hàm trong `src/`, xóa output trước khi commit, đặt tên `notebooks/<tên>_*.ipynb`.
- Ngẫu nhiên: mọi `rng` lấy từ `config.get_seed()` (SEED = 2044).
- Mã tham khảo ngoài (sách, GitHub, Kaggle) phải ghi nguồn ngay tại chỗ bằng chú thích; phần tự cài đặt không lấy từ nguồn ngoài.

## 6. Văn bản và báo cáo
- Báo cáo viết trên Google Docs (không để trong git). Số liệu chỉ lấy từ tệp trong `results/`. Dấu phẩy thập phân trong văn bản (0,875).
- Công thức đánh số theo chương, ký hiệu thống nhất như file này. Tài liệu tham khảo: IEEE hoặc APA, nhất quán; bắt buộc [1], [2], [3], [7], [8] (xem `docs/DE3.md`).

## 7. Quyết định đã chốt (17/11/2026; hằng số ở `src/config.py`)
- **Hạt giống lặp (B4.3):** 5 hạt giống = SEED, SEED+1, …, SEED+4 (nhóm 18: 2044–2048), lấy bằng `config.get_run_seeds()`. Báo cáo trung bình ± độ lệch chuẩn.
- **Bootstrap (B9.1):** lấy lại mẫu **theo tuần** (các giờ trong tuần và các tuần liền nhau tương quan), `BOOTSTRAP_ITERS` = 2000 lần, khoảng tin cậy 95% kiểu phân vị, `rng` từ `get_seed()`.
- **Tref của CDH (R3, B6.2):** không giả định đơn vị hay giá trị cố định. Lưới Tref = các phân vị `TREF_QUANTILES` của nhiệt độ trung bình ba thành phố **trên train**; chọn Tref bằng MAPE trên tập **kiểm định**.
- **Trễ và cửa sổ trượt (B6.2):** `FEATURE_LAGS_HOURS` = (336, 504, 672). Trung bình và độ lệch chuẩn trượt tính trên ba trễ này (cùng giờ trong tuần của tuần 2, 3, 4 trước), nên mọi trễ đều ≥ 240 giờ.
- **Nhãn B7.2:** {0, 1} như B7.1 (BCE cần nhãn {0, 1}).
- **Tuần khởi động (18/11/2026):** trễ xa nhất là 672 giờ nên `config.WARMUP_WEEKS` = 4 tuần đầu của train chỉ làm lịch sử, KHÔNG dùng để huấn luyện (`data_prep.drop_warmup`). Train huấn luyện còn 205 tuần; val và test không bị ảnh hưởng; cách chia 209/26/37/14 giữ nguyên. Không điền khuyết. Báo cáo ghi rõ một dòng.

## 8. Ghi chú từ T001 (18/11/2026; số liệu chạy trên dữ liệu thật bằng `src/data_prep.py`)
**Nguồn và tệp**
- Dữ liệu đúng nguồn của đề (Mendeley, doi:10.17632/byx7sztj59.1, CC BY 4.0); ba tệp khớp kích thước và SHA-256 trong `config.DATA_FILES`. Tải tay bằng trình duyệt (script bị HTTP 403) thì tệp mang tên gốc (`continuous dataset.csv`, `weekly pre-dispatch forecast.csv`, `Columns' metadata and train-test splits details.pdf`): **phải đổi tên** thành `continuous.csv`, `forecast_cnd.csv`, `columns_metadata.pdf` trong `data/raw/` rồi chạy `python data\download_data.py --with-pdf` để kiểm.
- `continuous.csv`: 48.048 dòng, không trùng, không thiếu giờ, không NaN. `forecast_cnd.csv`: 40.152 dòng, nhãn thời gian dạng `1/2/2016 0:00` (tháng/ngày/năm), chưa căn với phụ tải (T002).

**Nhãn thời gian**
- Nhãn của `continuous.csv` là **giờ kết thúc** (xem mục 1): 48.048 dòng = 286 tuần × 168 giờ, dòng đầu 2015-01-03 01:00, dòng cuối 2020-06-27 00:00. `config.TIMESTAMP_SHIFT_HOURS = -1` đưa về giờ bắt đầu; không lùi thì `split_weeks` báo `AssertionError` (train còn 35.111 giờ thay vì 35.112).

**Bài toán phụ "giờ cao điểm" và rò rỉ**
- Ngưỡng chỉ tìm từ các giờ của **train** (35.112 giờ → phân vị 90% = **1.450,75 MWh**); sau đó áp dụng một ngưỡng đó để gán nhãn +1/−1 cho mọi giờ (train, val, test). Tính ngưỡng trên cả ba phần là rò rỉ (đề mục 3.1d): ngưỡng sẽ thành 1.460,91 và nhãn của giờ trong quá khứ đổi theo số liệu tương lai.
- Tỷ lệ giờ cao điểm theo ngưỡng của train: train 10,0%; val 17,5%; test_a 17,3%; **test_b 0,0%**. Nghĩa là bài phân loại cao điểm trên test_b không có nhãn +1 nào để chấm; báo cáo phải nêu rõ, không được bỏ qua. Nguyên nhân: tải điện tăng theo năm (val, test_a cao hơn train) và giai đoạn phong tỏa (test_b) thấp hơn ngưỡng.
- Quy tắc chung: mọi thứ "học từ dữ liệu" (ngưỡng, trung vị tham chiếu, chuẩn hóa, trọng số, siêu tham số) chỉ học từ train hoặc chọn bằng val; test chỉ chấm một lần.

**Giờ phụ tải thấp bất thường (< 50% trung vị train = 1.156,71 MWh): 8 giờ**
- 24/01/2015 16:00 (509,84; 44%); 27/06/2017 11:00 (380,59; 33%); 01/07/2017 13:00 (560,70; 48%) — đều trong train.
- 20/01/2019 11:00 đến 15:00, năm giờ liền (85,19; 135,76; 263,62; 417,45; 475,80; từ 7% đến 41%) — trong val.
- Không giờ nào nằm trong test. **UNKNOWN:** nguyên nhân (chưa tra). **Đề xuất, chưa chốt:** giữ nguyên dữ liệu, báo MAPE trên val cả khi có và không có năm giờ ngày 20/01/2019 (MAPE chia cho giá trị thật nên rất nhạy với giờ này).

**Giới hạn của dữ liệu (nêu trong báo cáo)**
- Số mẫu độc lập là số tuần (209 train, 26 val, 37 + 14 test), không phải 48.048 giờ vì các giờ liền nhau tương quan; test_b chỉ 14 tuần nên kết quả dao động mạnh, khoảng tin cậy bootstrap sẽ rộng.

**Kỹ thuật**
- pandas đã ghim 3.1.1: dùng `day_of_week`, không dùng `dayofweek` (đã deprecated, sinh `Pandas4Warning`).
- Console Windows (cp1252) lỗi khi in tiếng Việt: chạy với `PYTHONUTF8=1` (script `run_all.py` đã tự đặt UTF-8).
