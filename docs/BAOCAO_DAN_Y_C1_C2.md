# Dàn ý báo cáo: Chương 1 và Chương 2

Đây là **dàn ý**, không phải văn bản báo cáo. Mỗi người tự viết đoạn văn trên Google Docs cho phần của mình (đề mục 7 cấm AI sinh nguyên đoạn báo cáo; AI chỉ được sửa chính tả, diễn đạt, đối chiếu số liệu). Cấu trúc và số trang theo Bảng 3 của đề (mục 5); mã chấm theo mục 3.3. Số liệu chưa có thì ghi `[results/...]`, **không điền số trước khi mã chạy ra**. Chỗ chưa kiểm chứng ghi UNKNOWN.

## Quy tắc chung cho mọi mục (đề mục 2.3 và 3.1)
- Mỗi hình/bảng: đánh số theo chương (Hình 1.2, Bảng 1.1), có chú thích, nhắc đến trong văn bản, đồ thị có tên trục và đơn vị, ghi nguồn nếu không do nhóm tạo. Tệp: `results/figures/<chương>_<số>_<mô_tả>.png`, ghi truy vết vào `docs/trace_<tên>.md`.
- Mỗi kết quả phải có **nhận xét, giải thích ý nghĩa**; chỉ dán kết quả thì tối đa nửa số điểm của ý.
- Công thức đánh số theo chương, ví dụ (2.1); ký hiệu đúng `docs/CONVENTIONS.md`; liệt kê trong bảng ký hiệu. Dấu phẩy thập phân trong văn bản (0,875).
- Không chép nguyên văn quá 3 dòng liên tiếp từ tài liệu. Trích dẫn ghi đến trang, ví dụ [2, tr. 158–173]. Không đưa vào tài liệu nào chưa đọc.
- Trích mã trong thân chỉ ≤ 15 dòng mỗi đoạn, tổng ≤ 3 trang cho cả báo cáo.

---

## Chương 1. Tổng quan bài toán và dữ liệu (4–5 trang, khối B1, tổng 1,0 điểm)

| Mục | Mã chấm | Người viết | Trang |
|---|---|---|---|
| 1.1 Bối cảnh, bài toán nghiệp vụ | B1.1 (0,25) | Huấn | ~1 |
| 1.2 Chỉ số đánh giá | B1.1 | Huấn | ~0,5 |
| 1.3 Dữ liệu và từ điển dữ liệu | B1.2 (0,25) | Huấn | ~0,75 |
| 1.4 Phân tích khám phá (EDA) | B1.3 (0,25) | Huấn | ~1,25 |
| 1.5 Tiền xử lý và chia dữ liệu | B1.4 (0,25) | Phi | ~1 |

### 1.1 Bối cảnh và phát biểu bài toán (B1.1)
Điều kiện được điểm: chỉ số chính phù hợp bài toán; nêu **chi phí của từng loại sai bằng ví dụ cụ thể**.
- Ai dùng kết quả: đơn vị điều độ (CND Panama) lập kế hoạch huy động nguồn cho tuần tới.
- Quyết định nào dựa trên dự báo: huy động nguồn với chi phí thấp nhất và bảo đảm an ninh hệ thống (đề mục 4.4a).
- Biến mục tiêu: `nat_demand` (MWh), 168 giờ của tuần Thứ Bảy → Thứ Sáu, dự báo trước theo quy tắc 72 giờ.
- Chi phí sai: dự báo thấp (thiếu nguồn, rủi ro an ninh) so với dự báo cao (huy động dư, tốn chi phí). Ví dụ cụ thể nên tính từ dữ liệu (ví dụ sai 1% tại giờ đỉnh tuần tương ứng bao nhiêu MWh); **không bịa đơn giá điện**, không có nguồn thì chỉ nêu định tính.
- So sánh được với dự báo chính thức của CND vì bộ dữ liệu kèm chính dự báo đó.
- Dẫn bài báo [7] (bắt buộc) cho bài toán và hệ số tham chiếu.

### 1.2 Chỉ số đánh giá (B1.1)
- Chỉ số chính: MAPE theo giờ của từng tuần, rồi trung bình các tuần kiểm tra; báo riêng (a) 37 tuần và (b) 14 tuần.
- Chỉ số phụ: MAE, RMSE (MWh), sai số đỉnh/đáy/năng lượng tuần như [7]; chỉ số kỹ năng = 1 − MAPE(mô hình)/MAPE(cơ sở).
- Mô hình cơ sở: trễ 336 giờ; trung bình cùng giờ các tuần 2–4 trước; dự báo CND.
- Lý do chọn MAPE và hạn chế: nhạy với giờ phụ tải thấp (đánh dấu giờ < 50% trung vị và nêu cách xử lý). Đề cấm dùng accuracy cho dữ liệu mất cân bằng; ở đây là hồi quy, nên chỉ cần một câu nói rằng bài toán phụ "giờ cao điểm" (lệch lớp, 10% dương) dùng độ đo riêng ở Chương 4.

### 1.3 Dữ liệu (B1.2)
Điều kiện được điểm: đủ thông tin; **từ điển dữ liệu bao phủ mọi biến được dùng**.
- Nguồn: Mendeley Data, doi:10.17632/byx7sztj59.1, giấy phép CC BY 4.0, trích dẫn bài [7] và bộ dữ liệu [8] (bắt buộc).
- Ngày tải và kích thước tệp: lấy từ README (`continuous dataset.csv` 10.524.179 byte; `weekly pre-dispatch forecast.csv` 929.119 byte). **Ngày tải: điền khi tải lần đầu.**
- Quy mô: 48.048 bản ghi theo giờ, 03/01/2015 – 27/06/2020 (kiểm lại bằng mã).
- Từ điển dữ liệu (Bảng 1.1, Huấn làm ở T004, tệp `docs/DATA_DICTIONARY.md`): tên biến, ý nghĩa, đơn vị, kiểu, thang đo cho `nat_demand`, 12 biến thời tiết `{T2M,QV2M,TQL,W2M}_{toc,san,dav}`, `Holiday_ID`, `holiday`, `school`, và các cột của tệp dự báo CND.
- Hạn chế cần nêu: thời tiết là số liệu đã xảy ra (tái phân tích), không phải dự báo thời tiết, tương đương giả định dự báo thời tiết hoàn hảo (đề mục 4.4g).
- **UNKNOWN:** nhãn thời gian của tệp phụ tải có lệch 1 giờ so với tệp dự báo hay không (T002). Chưa kết luận thì không viết khẳng định.

### 1.4 EDA (B1.3)
Điều kiện được điểm: **ít nhất 4 hình**, mỗi hình có ít nhất một nhận xét **định lượng**; phát hiện **ít nhất một vấn đề của dữ liệu và nêu cách xử lý**.
- Thống kê mô tả (Bảng 1.2): `nat_demand` và các biến thời tiết, giá trị thiếu theo cột.
- Hình gợi ý (chọn sau khi xem dữ liệu, tên tệp `results/figures/1_<số>_*.png`): (1) chuỗi phụ tải theo thời gian toàn kỳ; (2) hồ sơ trung bình theo giờ trong ngày, tách ngày làm việc, cuối tuần, lễ; (3) phụ tải theo nhiệt độ; (4) ma trận tương quan; (5) thay đổi giai đoạn phong tỏa 2020 so với trước.
- Vấn đề dữ liệu: **các ứng viên dưới đây chỉ là giả thuyết, phải kiểm bằng dữ liệu rồi mới viết**: giá trị thiếu hoặc bất thường, giờ phụ tải thấp bất thường, thay đổi cấu trúc do phong tỏa, lệch nhãn thời gian (T002).
- Mỗi hình kèm 1–2 câu nhận xét có con số lấy từ `results/tables/`.

### 1.5 Tiền xử lý và chia dữ liệu (B1.4)
Điều kiện được điểm: dùng SEED = 2026 + G = 2044; không mẫu nào thuộc hai tập; **mọi phép biến đổi chỉ khớp (fit) trên tập huấn luyện**.
- Xử lý thiếu, ngoại lai, mã hóa (theo kết quả EDA); z-score khớp trên train, áp cho val/test bằng cùng tham số.
- Chia theo thời gian, theo tuần: train 209 tuần, val 26, test (a) 37, test (b) 14, kèm ngày bắt đầu/kết thúc (lấy từ `config.SPLITS`). Không xáo trộn, không k-fold thường, kiểm định trượt theo thời gian.
- Bảng kích thước các tập (số tuần, số giờ) và tỉ lệ nhãn "giờ cao điểm" của từng tập; ngưỡng là phân vị 90% **của tập huấn luyện** (Bảng 1.3, `[results/tables/1_*_split_sizes.csv]`).
- Hộp nhắc quy tắc 72 giờ: chỉ dùng phụ tải đến hết Thứ Ba trước tuần dự báo; trễ cố định ≥ 240 giờ. Trỏ sang R1 ở Chương 6.
- Tập kiểm tra chỉ dùng một lần ở cuối (nêu rõ trong văn bản).

---

## Chương 2. Cơ sở lý thuyết (5–6 trang, khối B2, tổng 0,75 điểm)

Điều kiện được điểm B2.1 (0,5): trình bày ngắn gọn, **ký hiệu thống nhất**; bám tài liệu theo chỉ dẫn của đề cương; mỗi mục có trích dẫn. Phân trang gợi ý bên dưới là của nhóm; ánh xạ chương → trang tài liệu lấy từ B2.1 của đề.

| Mục | Nội dung | Tài liệu (theo đề) | Người viết | Trang |
|---|---|---|---|---|
| 2.1 | GD, SGD, mini-batch, momentum, L2 | [2, tr. 158–173]; [3, chương 9] | Huấn | ~1,25 |
| 2.2 | Perceptron, hàm mất mát perceptron, PLA, Pocket | [2, tr. 175–183] | Việt | ~1 |
| 2.3 | MLP, hàm kích hoạt, hàm mất mát, lan truyền ngược BP1–BP4 | [1, tr. 115–146]; [2, tr. 214–232] | Phi | ~1,5 |
| 2.4 | Đặc trưng, PCA, LDA, chọn đặc trưng; suy dẫn tự viết (d) | [1, tr. 88–99, 521–567] | Việt | ~1,25 |
| 2.5 | Các chỉ số đánh giá dùng trong báo cáo | [7] và CONVENTIONS mục 4 | Phi | ~0,5 |

### 2.1 Tối ưu bằng Gradient Descent (Huấn)
- Hàm mục tiêu: J(w) = 1/(2n)·‖X̃w − y‖² + (λ/2)·‖w[:-1]‖² (không phạt hệ số tự do), gradient tương ứng, `X̃ = [X, 1]` (xem CONVENTIONS mục 3).
- GD theo lô, SGD, mini-batch: công thức cập nhật, khác nhau về chi phí và độ nhiễu.
- Momentum: công thức cập nhật, ý nghĩa hệ số, khi nào giúp hội tụ nhanh hơn.
- Tốc độ học η, điều kiện hội tụ, vai trò của chuẩn hóa (điều kiện của bài toán). Nghiệm giải tích ridge dùng để đối chiếu.
- Kiểm tra gradient bằng sai phân hữu hạn (ngưỡng sai số tương đối ≤ 1e-6, float64) chỉ nêu ở đây, kết quả ở Chương 4.

### 2.2 Perceptron, PLA, Pocket (Việt)
- Bài toán phụ "giờ cao điểm" nhãn ±1; hàm mất mát perceptron J_P và vì sao không phạt mẫu đúng.
- PLA: `x̃ = (x, 1)`, `w̃(0) = 0`, mẫu có `y·g ≤ 0` là sai (kể cả g = 0); điều kiện hội tụ khi tách tuyến tính.
- Pocket: giữ nghiệm tốt nhất, dùng khi không tách được; so sánh với PLA.
- Kiểm tra khả tách tuyến tính bằng quy hoạch tuyến tính (nêu ý, kết quả ở Chương 4); liên hệ bài toán XOR như giới hạn của biên tuyến tính.

### 2.3 MLP và lan truyền ngược (Phi)
- Kiến trúc: tầng ra tuyến tính, MSE (hồi quy); ít nhất 2 hàm kích hoạt ẩn (ví dụ sigmoid, tanh, ReLU) và đạo hàm.
- Lan truyền thuận; lan truyền ngược với BP1–BP4 (đạo hàm tầng ra, truyền sai số qua tầng, gradient trọng số và độ lệch), ký hiệu thống nhất.
- Khởi tạo trọng số (Xavier/He), chính quy hóa L2, dừng sớm; SGD và momentum cho MLP.
- Kiểm tra gradient bằng sai phân hữu hạn trên ít nhất 2 kiến trúc (ý nêu ở đây, kết quả ở Chương 5).

### 2.4 Đặc trưng, PCA, LDA, chọn đặc trưng (Việt)
- Điểm Fisher cho từng đặc trưng; vai trò đặc trưng trễ, lịch, thời tiết (liên hệ Chương 3).
- PCA: trên ma trận hiệp phương sai (chia n − 1) hoặc SVD; phương sai giải thích; chọn k.
- LDA: ma trận phân tán trong lớp S_W và giữa các lớp S_B, bài toán trị riêng tổng quát; trường hợp hai lớp w ∝ S_W⁻¹(m1 − m0).
- **Suy dẫn tự viết từng bước (B2.2, 0,25, Việt chọn (d))**: nghiệm LDA hai lớp từ tiêu chí Fisher. Điều kiện: đúng, đủ bước, ký hiệu khớp với mã trong `src/features.py`. Phần này **do Việt tự suy dẫn**, không để AI làm thay.
- Chọn đặc trưng theo ít nhất 2 họ: lọc, bọc, nhúng (ý nêu ở đây, kết quả ở Chương 3).

### 2.5 Chỉ số đánh giá (Phi)
- MAPE (theo giờ, theo tuần, trung bình tuần), MAE, RMSE, sai số đỉnh/đáy/năng lượng tuần, chỉ số kỹ năng.
- Đoạn ngắn về bài toán phân lớp phụ: ma trận nhầm lẫn, precision, recall, F1 (nếu dùng ở Chương 4).
- Khoảng tin cậy bootstrap (≥ 1.000 lần) ở Chương 6, chỉ nêu phương pháp tại đây.

---

## Việc cần làm trước khi viết (theo thứ tự)
1. Huấn: xong từ điển dữ liệu (T004) và EDA (T005) thì viết 1.1–1.4; số liệu và hình lấy từ `results/`.
2. Phi: xong `data_prep` (T001) và kiểm nhãn thời gian (T002) thì viết 1.5.
3. Mỗi người đọc tài liệu [1], [2], [3] ở trang được chỉ rồi mới viết mục lý thuyết của mình.
4. Phi ghép, đối chiếu ký hiệu và số công thức toàn Chương 2; đối chiếu từng con số Chương 1 với `results/`.

## Chưa biết / chưa kiểm chứng (UNKNOWN)
- Nhãn thời gian có lệch 1 giờ so với dự báo CND hay không (T002).
- Các vấn đề dữ liệu thực sự có trong EDA (thiếu, bất thường): chưa chạy.
- Ngày tải dữ liệu.
- Ánh xạ trang tài liệu → mục (cột "Tài liệu" ở Chương 2) lấy từ chữ của B2.1; nên mở đối chiếu với sách.
