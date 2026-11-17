# Dàn ý báo cáo đầy đủ (Đề 3, nhóm 18)

Đây là **dàn ý đầy đủ** từ bìa đến phụ lục, không phải văn bản báo cáo. Mỗi người tự viết đoạn văn trên Google Docs cho phần của mình (đề mục 7 cấm AI sinh nguyên đoạn báo cáo; AI chỉ được sửa chính tả, diễn đạt, đối chiếu số liệu). Cấu trúc và số trang theo Bảng 3 của đề (mục 5); mã chấm theo mục 3.3. Số liệu chưa có thì ghi `[results/...]`, **không điền số trước khi mã chạy ra**. Chỗ chưa kiểm chứng ghi UNKNOWN.

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

## Chương 3. Xây dựng đặc trưng và giảm chiều (5–6 trang, khối B6, tổng 1,5 điểm)

Chủ trì: Việt. Mọi thống kê dùng để tạo đặc trưng, PCA, LDA, chọn đặc trưng **chỉ tính trên tập huấn luyện**; mọi so sánh trong chương này báo trên **tập kiểm định** (tập kiểm tra chỉ mở một lần ở Chương 6).

| Mục | Mã chấm | Người viết | Trang |
|---|---|---|---|
| 3.1 Phân tích đặc trưng gốc | B6.1 (0,25) | Việt | ~1 |
| 3.2 Đặc trưng mới | B6.2 (0,5) | Việt | ~1,5 |
| 3.3 PCA | B6.3 (0,25) | Việt | ~1 |
| 3.4 LDA và chọn đặc trưng | B6.4 (0,25) | Việt | ~1 |
| 3.5 Bảng so sánh các cách biểu diễn | B6.5 (0,25) | Việt | ~1 |

### 3.1 Phân tích đặc trưng gốc (B6.1)
Điều kiện được điểm: bảng xếp hạng đặc trưng; nhận xét ≥ 3 đặc trưng mạnh hoặc yếu **bằng ý nghĩa nghiệp vụ**.
- Thang đo từng nhóm biến: định danh, thứ bậc, khoảng, tỉ lệ (phụ tải, 12 biến thời tiết, `Holiday_ID`, `holiday`, `school`).
- Tiêu chí Fisher cho từng đặc trưng với nhãn "giờ cao điểm" (hai lớp), tính trên train (`features.fisher_score`); bảng xếp hạng (Bảng 3.1).
- Ma trận tương quan, các nhóm đặc trưng dư thừa (ví dụ cùng một biến ở ba thành phố; **chỉ viết sau khi kiểm bằng dữ liệu**).
- Nhận xét ≥ 3 đặc trưng mạnh hoặc yếu và vì sao có nghĩa về nghiệp vụ.

### 3.2 Đặc trưng mới (B6.2)
Điều kiện được điểm: ≥ 5 đặc trưng có cơ sở nghiệp vụ; bảng gồm tên, công thức, ý nghĩa, Fisher trước và sau; **không dùng thông tin của tương lai**.
- Họ trễ phụ tải hợp lệ: L(h−336), L(h−504), L(h−672) (trễ ≥ 240 giờ; 168 không dùng).
- Trung bình và độ lệch chuẩn trượt theo tuần (chỉ từ phụ tải đã biết).
- Lịch: giờ trong ngày và ngày trong tuần mã hóa sin/cos hoặc one-hot, cuối tuần, lễ, kỳ học.
- Thời tiết: nhiệt độ trung bình ba thành phố, độ nóng CDH = max(0, T − Tref), tương tác giờ × nhiệt độ.
- Bảng 3.2: tên, công thức, ý nghĩa, **độ trễ nhỏ nhất**, Fisher trước/sau (độ trễ nhỏ nhất cũng là nguồn cho bảng R1 ở Chương 6).
- **Đã chốt (17/11/2026, `config.py`, `CONVENTIONS` mục 7):** Tref chọn từ lưới phân vị `TREF_QUANTILES` của nhiệt độ trung bình ba thành phố trên train, bằng MAPE trên kiểm định; cửa sổ trượt dùng ba trễ `FEATURE_LAGS_HOURS` = (336, 504, 672).

### 3.3 PCA (B6.3)
Điều kiện được điểm: chuẩn hóa trước PCA khi các biến khác đơn vị (hoặc giải thích vì sao không); trị riêng khớp thư viện đến 1e-6.
- PCA tự cài đặt trên 12 biến thời tiết (trị riêng hoặc SVD); đối chiếu `sklearn.decomposition.PCA`.
- Biểu đồ phương sai giải thích và tích lũy; **chọn k có lý do** (ngưỡng nào, vì sao).
- Sai số tái tạo theo k; diễn giải ≥ 2 thành phần chính qua hệ số tải (loadings).
- (PCA trên đồ thị phụ tải ngày là R4, ở Chương 6.)

### 3.4 LDA và chọn đặc trưng (B6.4)
Điều kiện được điểm: chọn đặc trưng bên trong vòng kiểm định hoặc chỉ trên train; liệt kê đặc trưng được giữ lại.
- LDA tự cài đặt (S_W, S_B, bài toán trị riêng tổng quát) cho phân loại loại ngày (ngày làm việc, cuối tuần, lễ); kết quả đầy đủ ở R4.
- Chọn đặc trưng ≥ 2 họ: lọc (Fisher, tương quan), bọc (SFS), nhúng (L1). Bảng: họ, cách chạy, đặc trưng được giữ (Bảng 3.3).
- Nói rõ vòng kiểm định dùng để chọn: **kiểm định trượt theo thời gian**, không k-fold thường.

### 3.5 Bảng so sánh các cách biểu diễn (B6.5)
Điều kiện được điểm: cùng cách chia dữ liệu, cùng chỉ số; có khoảng tin cậy hoặc độ lệch chuẩn.
- Cùng một mô hình (tuyến tính ở B3 và MLP ở B5) với: (i) đặc trưng gốc; (ii) gốc + đặc trưng mới; (iii) k thành phần chính; (iv) sau chọn đặc trưng (Bảng 3.4, MAPE trên kiểm định).
- Nhận xét theo hiện tượng Hughes và đường cong học.
- Mục này **chỉ hoàn tất sau khi MLP chạy được** (Phase 4).

---

## Chương 4. Mô hình tuyến tính: tối ưu GD và perceptron (5–6 trang, khối B3 + B4, tổng 2,25 điểm)

| Mục | Mã chấm | Người viết | Trang |
|---|---|---|---|
| 4.1 Hồi quy tuyến tính, GD, SGD, mini-batch | B3.1 (0,5) | Huấn | ~1 |
| 4.2 Momentum | B3.2 (0,25) | Huấn | ~0,5 |
| 4.3 Thí nghiệm tốc độ học | B3.3 (0,25) | Huấn | ~1 |
| 4.4 Kiểm tra tính đúng | B3.4 (0,25) | Huấn | ~0,5 |
| 4.5 PLA và Pocket | B4.1 (0,25) | Việt | ~0,75 |
| 4.6 Khả tách tuyến tính | B4.2 (0,25) | Việt | ~0,5 |
| 4.7 Thực nghiệm perceptron | B4.3 (0,25) | Việt | ~0,75 |
| 4.8 So sánh với tuyến tính và MLP | B4.4 (0,25) | Việt | ~0,75 |

### 4.1 Hồi quy tuyến tính và GD, SGD, mini-batch (B3.1)
Điều kiện được điểm: mã NumPy tự viết; công thức trong báo cáo khớp mã; đường mất mát giảm và ổn định.
- Hàm mất mát có chính quy hóa L2 và gradient, đúng CONVENTIONS mục 3 (không phạt hệ số tự do).
- Ba biến thể: khác nhau về kích thước lô, chi phí, độ nhiễu; hình mất mát theo lần cập nhật (Hình 4.1).

### 4.2 Momentum (B3.2)
Điều kiện được điểm: cùng điểm khởi tạo, cùng η; nêu số lần cập nhật để đạt cùng một mức mất mát.
- So với GD thường trên cùng một hình mất mát theo số lần cập nhật (Hình 4.2) và bảng số lần cập nhật.
- Khuyến khích thêm Nesterov hoặc Adam (cũng là điểm khuyến khích 6.5, tối đa 0,25).

### 4.3 Thí nghiệm tốc độ học (B3.3)
Điều kiện được điểm: có hình và bảng; giải thích bằng độ cong của hàm mất mát (số điều kiện); liên hệ chương 1 và [3, chương 9].
- ≥ 4 giá trị η theo thang log (ví dụ 1e-3, 1e-2, 1e-1, 1), chỉ ra trường hợp hội tụ chậm, dao động, phân kỳ.
- Ảnh hưởng của chuẩn hóa z-score đến tốc độ hội tụ (có và không z-score). Đây là số liệu trả lời **câu hỏi nghiên cứu 3**.

### 4.4 Kiểm tra tính đúng (B3.4)
Điều kiện được điểm: (a) gradient so với sai phân hữu hạn, sai số tương đối ≤ 1e-6 (float64); (b) chỉ số trên kiểm định chênh nghiệm giải tích không quá 0,005, hoặc giải thích được nguyên nhân.
- (a) Kiểm tra gradient trên một mẫu con nhỏ (bảng sai số).
- (b) Đối chiếu với nghiệm giải tích ridge của bài toán bình phương tối thiểu có chính quy hóa; nêu chênh lệch.

### 4.5 PLA và Pocket (B4.1)
Điều kiện được điểm: mã tự viết đúng quy ước.
- Bài toán phụ "giờ cao điểm": nhãn ±1, ngưỡng là phân vị 90% của train.
- Quy ước: `x̃ = (x, 1)`, `w̃(0) = 0`, mẫu có `y·g ≤ 0` là sai (kể cả g = 0), thứ tự duyệt, điều kiện dừng; Pocket giữ nghiệm tốt nhất.

### 4.6 Khả tách tuyến tính (B4.2)
Điều kiện được điểm: kết luận có căn cứ định lượng.
- Kiểm tra bằng bài toán quy hoạch tuyến tính khả thi [3, §8.6.1] với `scipy.optimize.linprog` (trạng thái nghiệm), hoặc bằng việc PLA không hội tụ sau số epoch đủ lớn (số lỗi theo epoch).
- Kết luận: khả tách hay không, và hệ quả cho PLA so với Pocket.

### 4.7 Thực nghiệm perceptron (B4.3)
Điều kiện được điểm: có hình số lỗi theo epoch; bảng trung bình ± độ lệch chuẩn qua các lần chạy.
- Số lỗi theo epoch của PLA và Pocket (Hình 4.3); ảnh hưởng của chuẩn hóa và thứ tự duyệt.
- ≥ 5 hạt giống; kiểm chứng tính bất biến theo η khi `w̃(0) = 0`.
- **Đã chốt:** 5 hạt giống = SEED..SEED+4 (2044–2048), `config.get_run_seeds()`.

### 4.8 So sánh perceptron với tuyến tính và MLP (B4.4)
Điều kiện được điểm: giải thích khác biệt qua hàm mất mát.
- So sánh với mô hình ở B3 và MLP ở B5 trên cùng tập kiểm định.
- Vùng quyết định trên mặt phẳng hai đặc trưng (hoặc hai thành phần chính) của perceptron và MLP (Hình 4.4).
- Vì sao J_P không phạt mẫu đúng sát biên; giới hạn của biên tuyến tính (liên hệ XOR).
- Hoàn tất sau khi MLP có kết quả (Phase 4).

---

## Chương 5. Mạng neural nhiều lớp (5–6 trang, khối B5, tổng 2,0 điểm)

Chủ trì: Phi. Mọi siêu tham số chọn trên **tập kiểm định** (hoặc kiểm định trượt theo thời gian trên train), không chọn trên tập kiểm tra.

| Mục | Mã chấm | Người viết | Trang |
|---|---|---|---|
| 5.1 Cài đặt MLP | B5.1 (0,5) | Phi | ~1,25 |
| 5.2 Kiểm tra gradient | B5.2 (0,25) | Phi | ~0,75 |
| 5.3 Kiến trúc và khởi tạo | B5.3 (0,5) | Phi | ~1,25 |
| 5.4 Tối ưu và chính quy hóa | B5.4 (0,5) | Phi | ~1,25 |
| 5.5 Đối chứng thư viện | B5.5 (0,25) | Phi | ~0,5 |

### 5.1 Cài đặt MLP (B5.1)
Điều kiện được điểm: công thức trong báo cáo khớp mã; mạng huấn luyện được (mất mát giảm).
- Lan truyền thuận dạng lô (ma trận); lan truyền ngược theo δ(l) (BP1–BP4); cập nhật mini-batch.
- ≥ 2 hàm kích hoạt ẩn (sigmoid, tanh, ReLU); tầng ra tuyến tính + MSE (hồi quy).
- Biến mục tiêu chuẩn hóa theo train; mỗi giờ cần dự báo là một mẫu; chỉ số báo cáo trên thang MWh gốc.
- Hình đường mất mát theo epoch (Hình 5.1).

### 5.2 Kiểm tra gradient (B5.2)
Điều kiện được điểm: sai số tương đối ≤ 1e-6 (float64); bảng sai số theo từng ma trận trọng số.
- ≥ 2 kiến trúc, trong đó một kiến trúc có ≥ 2 tầng ẩn (Bảng 5.1).

### 5.3 Kiến trúc và khởi tạo (B5.3)
Điều kiện được điểm: bảng kết quả trên kiểm định; giải thích đối xứng khi khởi tạo hằng số, bão hòa và gradient biến mất khi dùng sigmoid nhiều tầng.
- ≥ 3 cấu hình độ rộng/độ sâu; khởi tạo bằng 0 hoặc hằng số so với Xavier/He; ≥ 2 hàm kích hoạt ẩn (Bảng 5.2).
- Giải thích bằng số liệu (chuẩn gradient theo tầng) chứ không chỉ lý thuyết.

### 5.4 Tối ưu và chính quy hóa (B5.4)
Điều kiện được điểm: siêu tham số chọn trên kiểm định; **không** chọn trên kiểm tra.
- So sánh ≥ SGD mini-batch và momentum (tự cài đặt); L2 và dừng sớm (dropout khuyến khích).
- Đường cong học huấn luyện – kiểm định (Hình 5.2); chẩn đoán quá khớp, thiếu khớp.
- Chia dữ liệu theo thời gian, **không dùng k-fold thường**.

### 5.5 Đối chứng thư viện (B5.5)
Điều kiện được điểm: chênh lệch chỉ số chính được giải thích (khởi tạo, bộ tối ưu, điều kiện dừng).
- Cùng kiến trúc và siêu tham số với `MLPRegressor` của scikit-learn (hoặc PyTorch); bảng đối chiếu (Bảng 5.3).
- Số liệu cho **câu hỏi nghiên cứu 4** (MLP vs tuyến tính, theo giờ và loại ngày) chuẩn bị ở đây, kết luận ở Chương 6.

---

## Chương 6. Đánh giá tổng hợp và yêu cầu riêng của đề (4–5 trang, khối B8 + B9, tổng 1,5 điểm)

Chương này dùng tập kiểm tra **đúng một lần** (`python run_all.py --final` do Phi chạy). Số liệu chỉ lấy từ tệp do lần chạy đó sinh ra. Mỗi mục R viết cô đọng (~0,5 trang).

| Mục | Mã chấm | Người viết | Trang |
|---|---|---|---|
| 6.1 Kết quả trên tập kiểm tra | B9.1 (0,25) | Phi | ~1 |
| 6.2 R1: giao thức không rò rỉ | R1 (0,25) | Phi | ~0,5 |
| 6.3 R2: so với CND và mô hình cơ sở | R2 (0,25) | Huấn | ~0,75 |
| 6.4 R3: sai số theo bối cảnh | R3 (0,25) | Phi | ~0,75 |
| 6.5 R4: đồ thị ngày, loại ngày, độ nhạy nhiệt độ | R4 (0,25) | Việt | ~0,75 |
| 6.6 Phân tích lỗi | B9.2 (0,25, phần phân tích lỗi) | Phi | ~0,75 |

### 6.1 Kết quả trên tập kiểm tra (B9.1)
Điều kiện được điểm: không chọn lại mô hình sau khi đã xem kết quả trên tập kiểm tra.
- Bảng tổng hợp mọi mô hình trên tập kiểm tra (dùng một lần), kèm 3 mô hình cơ sở của đề (trễ 336 giờ; trung bình cùng giờ các tuần 2–4; dự báo CND). Báo riêng (a) 37 tuần và (b) 14 tuần.
- Khoảng tin cậy 95% bằng bootstrap (≥ 1.000 lần lặp) cho chỉ số chính; kết luận chênh lệch có ý nghĩa hay không.
- **Đã chốt:** bootstrap lấy lại mẫu theo tuần, 2000 lần, khoảng tin cậy 95% kiểu phân vị (`config.BOOTSTRAP_ITERS`, `BOOTSTRAP_CI`).
- Điểm khuyến khích: kiểm định ghép cặp giữa hai mô hình tốt nhất (0,25).

### 6.2 R1: giao thức dự báo không rò rỉ
Điều kiện được điểm: bảng kiểm tra độ trễ; thí nghiệm có và không rò rỉ trên kiểm định.
- Bảng "đặc trưng – độ trễ nhỏ nhất so với giờ cần dự báo – vì sao hợp lệ" (nguồn: Bảng 3.2); chứng minh mọi đặc trưng chỉ dùng phụ tải đến hết Thứ Ba trước tuần dự báo.
- Thí nghiệm sai số "ảo" khi dùng nhầm L(h−24) hoặc L(h−168); nêu L(h−168) hợp lệ cho bao nhiêu giờ trong tuần.

### 6.3 R2: so với dự báo CND và mô hình cơ sở
Điều kiện được điểm: căn đúng thời điểm giữa dự báo chính thức và số liệu thực; mọi mô hình dùng cùng các tuần kiểm tra.
- MAPE, RMSE, sai số đỉnh/đáy/năng lượng theo từng tuần kiểm tra và trung bình; chỉ số kỹ năng = 1 − MAPE(mô hình)/MAPE(cơ sở); số tuần mô hình của nhóm tốt hơn CND.
- Số liệu cho **câu hỏi nghiên cứu 1**.
- **UNKNOWN:** nhãn thời gian tệp phụ tải có lệch 1 giờ so với tệp CND hay không (T002); chưa kết luận thì chưa viết mục này.

### 6.4 R3: sai số theo bối cảnh
Điều kiện được điểm: bảng MAPE theo từng nhóm; giải thích bằng số liệu.
- MAPE theo giờ trong ngày; ngày làm việc, cuối tuần, ngày lễ; giai đoạn (a) và (b).
- Nhận diện thời điểm thay đổi cấu trúc từ dữ liệu; đề xuất và thử ≥ 1 cách thích nghi (huấn luyện lại cửa sổ trượt, tăng trọng số mẫu gần), chỉ dùng dữ liệu đã biết theo quy tắc 72 giờ.

### 6.5 R4: đồ thị phụ tải ngày, loại ngày, độ nhạy nhiệt độ
Điều kiện được điểm: hình các thành phần chính và ma trận nhầm lẫn; nhận xét dựa trên số liệu.
- PCA trên véc tơ 24 giờ đã chia cho trung bình ngày, diễn giải 2–3 thành phần đầu (vẽ dạng đường 24 giờ).
- LDA phân loại 3 loại ngày (ngày làm việc, cuối tuần, ngày lễ), ma trận nhầm lẫn.
- Độ nhạy phụ tải theo nhiệt độ ở từng giờ (MWh/°C), so sánh với hệ số khoảng 74,8 MWh/°C nêu trong [7].
- Số liệu cho **câu hỏi nghiên cứu 2** (đặc trưng quan trọng nhất) cùng với kết quả chọn đặc trưng ở 3.4.

### 6.6 Phân tích lỗi (một phần B9.2)
Điều kiện được điểm: câu trả lời dựa trên số liệu của chính nhóm.
- ≥ 10 mẫu dự đoán sai (giờ-tuần có sai số lớn), phân nhóm nguyên nhân. Nhóm nguyên nhân chỉ ghi **sau khi nhìn dữ liệu** (ví dụ ngày lễ, giai đoạn phong tỏa, giờ phụ tải thấp là giả thuyết cần kiểm).

---

## Kết luận và hướng phát triển (1 trang, khối B9.2)
- Trả lời đủ **4 câu hỏi nghiên cứu** của đề, mỗi câu 2–3 câu, **dẫn mục và số liệu** làm căn cứ (không viết kết luận trước khi có kết quả):
  1. Tốt hơn CND ở giai đoạn bình thường? Giai đoạn phong tỏa? (6.1, 6.3)
  2. Đặc trưng nào quan trọng nhất? (3.4, 6.5)
  3. Chuẩn hóa và momentum ảnh hưởng thế nào đến tốc độ hội tụ? (4.2, 4.3)
  4. MLP có lợi thế ở những giờ hoặc loại ngày nào? (5.5, 6.4)
- Hạn chế: thời tiết là số liệu đã xảy ra (giả định dự báo thời tiết hoàn hảo, đề mục 4.4g); phạm vi một hệ thống điện; **các hạn chế khác ghi sau khi có kết quả**.
- Khuyến nghị triển khai và giám sát: trôi dữ liệu, tần suất cập nhật mô hình; (tùy chọn) chỉ số PSI.
- Hướng phát triển.

## Tài liệu tham khảo
- Chuẩn IEEE **hoặc** APA, nhất quán một chuẩn cho cả báo cáo. Bắt buộc có [1], [2], [3] (đề cương), [7] (bài báo gốc) và [8] (bộ dữ liệu). Trích dẫn ghi đến chương, mục hoặc trang.
- Mọi tài liệu trong danh sách phải được **trích dẫn trong văn bản**, và mọi tài liệu được trích phải có trong danh sách (thiếu thì Phần I tối đa 3,0).
- Chỉ đưa tài liệu cả nhóm đã đọc và kiểm tra tồn tại thật. Tài liệu bắt buộc theo đề:
  - [1] Đinh Mạnh Tường (2015). *Học máy: các kỹ thuật cơ bản và hiện đại.* NXB Đại học Quốc gia Hà Nội.
  - [2] Fukunaga, K. (1990). *Introduction to Statistical Pattern Recognition* (2nd ed.). Academic Press.
  - [3] Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization.* Cambridge University Press.
  - [7] Aguilar Madrid, E., & Antonio, N. (2021). Short-term electricity load forecasting with machine learning. *Information*, 12(2), 50. https://doi.org/10.3390/info12020050
  - [8] Aguilar Madrid, E. (2021). Short-term electricity load forecasting (Panama case study) [Dataset]. Mendeley Data, V1. https://doi.org/10.17632/byx7sztj59.1
- Mã tham khảo từ ngoài (Kaggle, GitHub, sách, bài giảng): ghi nguồn ngay trong chú thích mã và trong danh sách này.

---

## Phụ lục (không quá 15 trang)

### Phụ lục A. Tính tay đối chiếu với mã (tối đa 4 trang, khối B7, tổng 0,75 điểm)
- Mẫu: 3 mẫu +1 và 3 mẫu −1 từ train theo đoạn mã của đề (`hand_calc.select_six_samples(y_train, seed)`), thứ tự duyệt +, −, +, −, +, −; hai đặc trưng Fisher lớn nhất, z-score theo train; làm tròn 4 chữ số; logistic dùng nhãn {0, 1}, PLA dùng ±1.
- **A.1 (B7.1, 0,25):** (a) một bước GD theo lô cho hồi quy logistic, `w̃(0) = 0`, η = 0,1, J là trung bình BCE không chính quy hóa: ŷ, J, ∇J, `w̃(1)`, J sau cập nhật (**Huấn**). (b) một epoch PLA trên 6 mẫu: từng bước g, y·g, có cập nhật không, `w̃` sau mỗi bước (**Việt**). Sai khác với mã ≤ 1e-4; mỗi bước trình bày rõ.
- **A.2 (B7.2, 0,25, Phi):** một bước lan truyền thuận và ngược mạng 2–2–1 (sigmoid, BCE) trên mẫu thứ nhất, khởi tạo theo đề, η = 0,5: z(1), a(1), ŷ, J, δ(2), δ(1), gradient, tham số mới, J sau cập nhật; kiểm chứng ≥ 1 đạo hàm bằng sai phân hữu hạn.
- **A.3 (B7.3, 0,25, Việt):** PCA trên 6 mẫu × 2 đặc trưng (trung bình, hiệp phương sai chia n − 1, hai trị riêng, hai véc tơ riêng đơn vị với quy ước dấu, tỉ lệ phương sai, tọa độ chiếu mẫu thứ nhất) và LDA hai lớp (m+, m−, S_W, w ∝ S_W⁻¹(m+ − m−) chuẩn hóa ‖w‖ = 1, giá trị chiếu 6 mẫu); nếu S_W suy biến thì cộng 1e-3·I và nêu rõ.
- Kèm đoạn mã in kết quả đối chiếu (`hand_calc.py`). **Tính tay do từng người tự làm**, không để AI làm thay.

### Phụ lục B. Bảng phân công và tỉ lệ đóng góp (1 trang)
- Theo mẫu Phụ lục 3a của đề: STT, họ tên, mã SV, nhiệm vụ chính (mục báo cáo, tệp mã), đóng góp (%), ký tên; tổng 100%.
- Phi lập bảng từ bảng sở hữu file (`TEAM.md` mục 3) và `docs/CHECKLIST.md`; cả ba người ký.

### Phụ lục C. Khai báo sử dụng công cụ AI (1 trang)
- Theo mẫu Phụ lục 3b: STT, công cụ (tên, phiên bản), mục đích, phần báo cáo hoặc tệp mã liên quan, nội dung yêu cầu chính, người dùng; kèm câu cam kết trung thực.
- Sinh bảng từ nhật ký bằng `python scripts\ai_log.py appendix`, rồi Phi rà lại.

### Phụ lục D. Hướng dẫn chạy mã và bảng truy vết (1–2 trang)
- Lệnh chạy lại toàn bộ (`python run_all.py`), thời gian chạy ước tính (≤ 60 phút), môi trường (Python, `requirements.txt`).
- Bảng truy vết: mỗi hình và bảng của báo cáo ↔ tệp trong `results/` ↔ hàm hoặc ô notebook ↔ mã task. Nguồn: `docs/trace_phi.md`, `docs/trace_huan.md`, `docs/trace_viet.md` và mục ánh xạ trong README.

---

## Phần mở đầu của báo cáo (không tính số trang)
- **Bìa** theo Phụ lục 1 của đề: tên trường, khoa, "BÁO CÁO CHUYÊN ĐỀ", học phần Học máy nâng cao, Đề số 3 và tên đề, giảng viên hướng dẫn (**UNKNOWN: chưa biết tên**), lớp học phần, mã nhóm G = 18, SEED = 2044, danh sách sinh viên (họ tên, MSSV).
- Lời cam đoan; mục lục; danh mục hình và bảng; bảng ký hiệu và chữ viết tắt (ký hiệu thống nhất theo `docs/CONVENTIONS.md`).
- Định dạng: A4, Times New Roman 13, giãn dòng 1,3; lề trên 2 cm, dưới 2 cm, trái 3 cm, phải 2 cm; số trang giữa chân trang. Tên tệp: `HMNC_BCCD_N18_De3.docx` và `.pdf`.

## Ngân sách số trang (phần thân 25–35 trang, khuyến nghị khoảng 30)
| Phần | Trang (đề gợi ý) | Khối chấm |
|---|---|---|
| Chương 1 | 4–5 | B1 |
| Chương 2 | 5–6 | B2 |
| Chương 3 | 5–6 | B6 |
| Chương 4 | 5–6 | B3, B4 |
| Chương 5 | 5–6 | B5 |
| Chương 6 | 4–5 | B8, B9 |
| Kết luận và hướng phát triển | 1 | B9 |
| Cộng | 29–35 | |
| Phụ lục (≤ 15): A tối đa 4, B 1, C 1, D 1–2 | không tính vào thân | B7, B10 |

Thân ngoài 25–35 trang bị trừ điểm (mục 6.4; bảng trừ điểm trong PDF bị vỡ chữ nên mức 0,5 điểm cho ngoài 25–35 trang và 1,0 điểm cho ngoài 20–40 trang là cách ghép của mình, NOT VERIFIED, đối chiếu trang 24 của đề). Phần thân gồm cả hình, bảng; trích mã tổng ≤ 3 trang.

## Báo cáo tiến độ (mốc 2, 30/11/2026, 2–3 trang, không chấm điểm; không nộp bị trừ 0,5)
Nội dung đề yêu cầu: kết quả EDA, cách chia dữ liệu, kết quả GD và perceptron ban đầu, kế hoạch phần còn lại. Gợi ý bố cục: (1) bài toán và dữ liệu (nửa trang); (2) EDA, ít nhất 2 hình chính (Huấn); (3) cách chia 209/26/37/14 tuần và quy tắc 72 giờ (Phi); (4) kết quả GD, SGD, momentum ban đầu (Huấn) và PLA, Pocket ban đầu (Việt); (5) kế hoạch và rủi ro còn lại. Phi tổng hợp. Mỗi người viết phần của mình; AI chỉ sửa chữ.

---

## Thứ tự viết (theo phase của `docs/CHECKLIST.md`)
| Phase | Hạn | Viết được phần |
|---|---|---|
| P1 | 22/11 | 1.1–1.3 (Huấn), 1.5 (Phi, sau T001–T002) |
| P2 | 30/11 | 1.4 EDA (Huấn), báo cáo tiến độ; mục lý thuyết 2.1, 2.2 (sau khi đọc tài liệu) |
| P3 | 14/12 | Chương 2 đủ, Chương 3, 4, 5, Phụ lục A |
| P4 | 20/12 | Chương 6 (sau `--final`), 3.5 và 4.8 (cần MLP), Kết luận |
| P5 | 25/12 | Ghép, đối chiếu số liệu và ký hiệu, Phụ lục B, C, D, slide, đóng gói |

## Kiểm trước khi nộp (từ mục 6.1 và 6.4 của đề)
- [ ] Thân 25–35 trang; phụ lục ≤ 15; hình và bảng đánh số theo chương, có chú thích, ghi nguồn, **được nhắc trong văn bản**.
- [ ] Mọi tài liệu tham khảo được trích trong văn bản và ngược lại; có [1], [2], [3], [7], [8].
- [ ] Mọi con số khớp kết quả chạy lại (chỉ lệch do làm tròn); mọi hình, bảng có dòng truy vết.
- [ ] Không dùng tập kiểm tra để chọn mô hình, siêu tham số, ngưỡng hay đặc trưng; chạy `--final` đúng một lần.
- [ ] Mọi kết quả chạy lại được từ mã nộp kèm (≤ 60 phút).
- [ ] Hồ sơ đủ: báo cáo `.docx` và `.pdf`, mã nguồn, README, slide ≤ 15 trang, Phụ lục B và C nằm trong báo cáo.
- [ ] **Nộp mã qua GitHub thì đề yêu cầu kho "riêng tư có mời giảng viên" (mục 2.2).** Repo hiện đang **public**; nếu chọn cách nộp này thì phải chuyển sang private trước hạn, hoặc nộp bằng `.zip`.
- [ ] Nộp đúng hạn (muộn bị trừ 1,0 điểm mỗi ngày; quá 3 ngày không nhận).

## Chưa biết / chưa kiểm chứng (UNKNOWN)
**Đã chốt ngày 17/11/2026** (xem `docs/CONVENTIONS.md` mục 7): hạt giống lặp, đơn vị và số lần bootstrap, lưới Tref, ba trễ cho cửa sổ trượt, nhãn B7.2.

**Còn UNKNOWN (cần dữ liệu hoặc nguồn ngoài, không chốt bằng quyết định được):**
- Nhãn thời gian tệp phụ tải có lệch 1 giờ so với tệp dự báo CND hay không: cần dữ liệu; T002 thử dịch −1/0/+1 giờ. Mặc định cho đến lúc đó: độ dịch 0.
- Các vấn đề dữ liệu thực sự có trong EDA, các nhóm nguyên nhân lỗi, kết quả mọi chương: chưa chạy.
- Tên giảng viên; ngày tải dữ liệu (dữ liệu chưa được tải về máy).
- Ánh xạ trang tài liệu → mục lý thuyết lấy từ chữ của B2.1; cần mở sách đối chiếu.
- Bảng trong PDF đề bị vỡ chữ ở vài chỗ (B6.3, B6.4, mục 6.4); các điều kiện chấm ở đó mình đã đối chiếu với tổng điểm khối, chưa với bản gốc từng ô.
