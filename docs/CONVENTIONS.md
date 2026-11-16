# CONVENTIONS — quy ước chung (chỉ Phi sửa)

Mục tiêu: ba người, ba AI vẫn cho ra cùng một định nghĩa, cùng một con số. Thông số số học ở `src/config.py`; file này giữ **định nghĩa và quy ước**. Thấy chỗ mơ hồ → ghi vào task, báo Phi, không tự chọn.

## 1. Thời gian và tuần
- Một tuần dự báo = Thứ Bảy 00:00 → Thứ Sáu 23:00 (168 giờ). `hour_in_week` ∈ [0, 167], 0 = Thứ Bảy 00:00.
- Chia tập theo `config.SPLITS` (209/26/37/14 tuần). Không xáo trộn, không k-fold thường; chỉ kiểm định trượt theo thời gian.
- Quy tắc 72 giờ: chỉ dùng phụ tải đến hết Thứ Ba trước tuần dự báo. Đặc trưng trễ cố định phải có trễ ≥ `guards.min_safe_lag()` = **240 giờ** (336, 504, 672 hợp lệ; 168 chỉ hợp lệ cho 96/168 giờ nên **không dùng**).
- UNKNOWN (Phi kiểm trong T002): nhãn thời gian trong tệp có phải "giờ kết thúc" (lệch 1 giờ so với tệp dự báo CND) hay không. Chưa kết luận thì chưa căn dự báo CND.

## 2. Dữ liệu và ký hiệu
- Đích: `nat_demand` (MWh). Thời tiết 12 biến: `{T2M,QV2M,TQL,W2M}_{toc,san,dav}`; lịch: `Holiday_ID, holiday, school`. Đúng tên cột trong `config.py`.
- `X̃ = [X, 1]` (cột 1 ở **cuối**), `w` có d+1 phần tử, hệ số tự do là phần tử cuối. Mọi hàm nhận `X` đã mở rộng trừ khi docstring ghi khác.
- Float64 ở mọi nơi. NumPy thuần cho phần tự cài đặt; không autograd; scikit-learn chỉ để chia/chuẩn hóa/chỉ số/đối chứng.
- Chuẩn hóa: z-score, **khớp trên tập huấn luyện**, áp dụng cho val/test bằng cùng tham số. Biến đích của MLP cũng chuẩn hóa theo train; mọi chỉ số báo cáo trên thang MWh gốc.

## 3. Hàm mất mát, nhãn
- Hồi quy tuyến tính (B3): `J(w) = 1/(2n)·‖X̃w − y‖² + (λ/2)·‖w[:-1]‖²` (không phạt hệ số tự do); `grad = 1/n·X̃ᵀ(X̃w − y) + λ·[w[:-1], 0]`.
- MLP (B5): tầng ra tuyến tính, MSE; kích hoạt ẩn ≥ 2 loại; giao diện như docstring `src/mlp.py`.
- Bài toán phụ "giờ cao điểm": nhãn `+1` nếu `nat_demand` > phân vị 90% **của tập huấn luyện** (`config.PEAK_QUANTILE`), ngược lại `−1`. PLA/Pocket dùng ±1; hồi quy logistic ở B7 dùng {0, 1} (đổi bằng `(y+1)/2`).
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
