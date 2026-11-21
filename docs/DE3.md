# DE3 — Bản chép yêu cầu của đề (chỉ để tra cứu)

Nguồn: đề "Báo cáo chuyên đề – Học máy nâng cao" (mã học phần 004295, 3 tín chỉ, năm học 2026–2027, ĐH Điện lực, khoa CNTT). Chép lại từ đề, không diễn giải thêm; chỗ không chắc ghi UNKNOWN. Số mục dẫn theo đề. Nhóm 18 → SEED = 2026 + 18 = 2044. Quy ước nhóm đã chốt nằm ở `docs/CONVENTIONS.md` và `src/config.py`.

## 1. Thông tin chung
| Mục | Nội dung |
|---|---|
| Hình thức | Báo cáo chuyên đề: nộp báo cáo viết, mã nguồn và bảo vệ trực tiếp; 70% điểm học phần |
| CLO | CLO1–CLO6; Chương 1 GD, Chương 2 perceptron, Chương 3 MLP + lan truyền ngược, Chương 4 xây dựng đặc trưng |
| Sản phẩm | Báo cáo khoảng 30 trang (thân 25–35 trang), mã nguồn chạy lại được, slide |
| Nhóm | 3 hoặc 4 sinh viên; mã nhóm G; mọi phép ngẫu nhiên dùng SEED = 2026 + G (chia dữ liệu, khởi tạo trọng số, xáo trộn mini-batch, chọn mẫu tính tay) |
| Đổi đề | Chỉ trước mốc nộp báo cáo tiến độ và phải được giảng viên đồng ý |
| Đối chiếu | Các nhóm cùng đề làm độc lập; giảng viên đối chiếu chéo mã nguồn và kết quả |

## 2. Đề 3 (mục 4.4) — Dự báo phụ tải điện hệ thống theo giờ cho tuần tới
### a) Bối cảnh
Đơn vị điều độ cần dự báo phụ tải từng giờ của tuần tới để lập kế hoạch huy động nguồn với chi phí thấp nhất và bảo đảm an ninh hệ thống. Ở Panama, Trung tâm Điều độ Quốc gia (CND) lập dự báo này hằng tuần trong báo cáo tiền điều độ (weekly pre-dispatch). Bộ dữ liệu kèm chính dự báo chính thức đó, nên so sánh được mô hình của nhóm với dự báo của đơn vị vận hành thực tế.

### b) Dữ liệu
| Mục | Nội dung |
|---|---|
| Tên | Short-term electricity load forecasting (Panama case study) – Aguilar Madrid (2021), Mendeley Data, phiên bản 1 [8] |
| Nguồn tải | https://data.mendeley.com/datasets/byx7sztj59/1 (không cần đăng nhập); bản sao trên Kaggle tên "Electricity Load Forecasting" |
| Quy mô | 48.048 bản ghi theo giờ, từ 03/01/2015 đến 27/06/2020 |
| Nội dung | (1) CSV liên tục: phụ tải toàn quốc theo giờ; nhiệt độ, độ ẩm, lượng mưa và tốc độ gió tại ba thành phố (Panama City – trạm Tocumen, Santiago, David); chỉ báo ngày lễ và kỳ học. (2) CSV dự báo tuần chính thức của CND. (3) Hai tệp Excel gợi ý biến hồi quy và 14 cặp tuần huấn luyện/kiểm tra, kèm PDF mô tả |
| Quy ước so sánh với dự báo chính thức | Tuần dự báo bắt đầu từ Thứ Bảy, kết thúc Thứ Sáu; có khoảng trống 72 giờ: dự báo cho tuần tới chỉ được dùng số liệu phụ tải đến hết giờ cuối cùng của Thứ Ba trước đó |
| Trích dẫn bắt buộc | Bài báo [7] và bộ dữ liệu [8] |
| Giấy phép | CC BY 4.0 |

### c) Nhiệm vụ
Dự báo 168 giờ của mỗi tuần kiểm tra theo đúng quy ước trên; so sánh với dự báo chính thức của CND và các mô hình cơ sở. Bài toán phụ cho perceptron và tính tay: phân lớp "giờ cao điểm cần cảnh báo", y = +1 nếu phụ tải của giờ đó lớn hơn phân vị 90% của phụ tải trên tập huấn luyện, ngược lại y = −1.

### d) Áp dụng các khối chung
| Khối | Yêu cầu cụ thể cho đề |
|---|---|
| Chia dữ liệu (B1.4) | Theo thời gian, theo tuần Thứ Bảy → Thứ Sáu: huấn luyện 03/01/2015 – 04/01/2019 (209 tuần); kiểm định 05/01/2019 – 05/07/2019 (26 tuần); kiểm tra (a) 06/07/2019 – 20/03/2020 (37 tuần, trước phong tỏa) và (b) 21/03/2020 – 26/06/2020 (14 tuần; phong tỏa toàn quốc bắt đầu ngày 25/03/2020 theo [7]). Báo cáo riêng (a) và (b). Được phép huấn luyện lại trước mỗi tuần kiểm tra nhưng chỉ với dữ liệu đã biết theo quy ước 72 giờ |
| Chỉ số (B1.1) | Chỉ số chính: MAPE theo giờ của từng tuần kiểm tra, lấy trung bình các tuần. Phụ: MAE, RMSE (MWh); sai số đỉnh tuần, đáy tuần và năng lượng tuần như trong [7]. Mô hình cơ sở: phụ tải cùng giờ cách đây 2 tuần (trễ 336 giờ); trung bình cùng giờ của các tuần thứ 2, 3, 4 trước đó; dự báo chính thức của CND |
| Mô hình tuyến tính (B3) | Hồi quy tuyến tính (MSE + L2) bằng GD, SGD, mini-batch, momentum; đối chiếu với nghiệm giải tích của bài toán bình phương tối thiểu có chính quy hóa |
| Perceptron (B4) | Bài toán phụ "giờ cao điểm cần cảnh báo" |
| MLP (B5) | Hồi quy, tầng ra tuyến tính, MSE; chuẩn hóa biến mục tiêu (khớp trên tập huấn luyện); mỗi giờ cần dự báo là một mẫu |
| Đặc trưng, giảm chiều (B6) | Trễ phụ tải hợp lệ (ví dụ L(h−336), L(h−504), L(h−672)), trung bình và độ lệch chuẩn trượt theo tuần; lịch (giờ trong ngày, ngày trong tuần mã hóa sin/cos hoặc one-hot, cuối tuần, lễ, kỳ học); thời tiết (nhiệt độ trung bình ba thành phố, độ nóng CDH = max(0, T − Tref), tương tác giờ × nhiệt độ). PCA trên 12 biến thời tiết và trên đồ thị phụ tải ngày 24 chiều; LDA cho bài toán phân loại loại ngày (R4); chọn đặc trưng theo ít nhất hai họ |
| Tính tay (B7) | Bài toán hai lớp "giờ cao điểm cần cảnh báo" |

### e) Yêu cầu riêng R1–R4 (khối B8, mỗi yêu cầu 0,25 điểm)
| Mã | Nội dung bắt buộc phải có | Điều kiện được tính điểm |
|---|---|---|
| R1 | Giao thức dự báo không rò rỉ: lập bảng "đặc trưng – độ trễ nhỏ nhất so với giờ cần dự báo – vì sao hợp lệ", chứng minh mọi đặc trưng chỉ dùng phụ tải đã biết đến hết Thứ Ba trước tuần dự báo; làm thí nghiệm cho thấy sai số "ảo" khi dùng nhầm L(h−24) hoặc L(h−168) | Có bảng kiểm tra độ trễ; thí nghiệm có và không rò rỉ trên tập kiểm định |
| R2 | So sánh với dự báo chính thức và mô hình cơ sở: MAPE, RMSE, sai số đỉnh, đáy, năng lượng theo từng tuần kiểm tra và trung bình; chỉ số kỹ năng = 1 − MAPE(mô hình)/MAPE(cơ sở); số tuần mô hình của nhóm tốt hơn dự báo của CND | Căn đúng thời điểm giữa dự báo chính thức và số liệu thực; mọi mô hình dùng cùng các tuần kiểm tra |
| R3 | Phân tích sai số theo bối cảnh: theo giờ trong ngày; ngày làm việc, cuối tuần, ngày lễ; giai đoạn (a) và (b). Nhận diện thời điểm thay đổi cấu trúc từ dữ liệu; đề xuất và thử ít nhất một cách thích nghi (huấn luyện lại theo cửa sổ trượt, tăng trọng số mẫu gần) | Bảng MAPE theo từng nhóm; giải thích bằng số liệu |
| R4 | Đồ thị phụ tải ngày: PCA trên các véc tơ 24 giờ đã chia cho trung bình ngày, diễn giải 2–3 thành phần đầu (vẽ dạng đường 24 giờ); LDA phân loại ba loại ngày (ngày làm việc, cuối tuần, ngày lễ), báo cáo ma trận nhầm lẫn; độ nhạy của phụ tải theo nhiệt độ ở từng giờ (MWh/°C), so sánh với hệ số khoảng 74,8 MWh/°C nêu trong [7] | Hình các thành phần chính và ma trận nhầm lẫn; nhận xét dựa trên số liệu |

### f) Câu hỏi nghiên cứu bắt buộc trả lời trong Kết luận
1. Mô hình của nhóm có tốt hơn dự báo chính thức của CND trong giai đoạn bình thường không? Trong giai đoạn phong tỏa thì sao?
2. Đặc trưng nào quan trọng nhất (trễ phụ tải, giờ, nhiệt độ, lễ), căn cứ vào kết quả chọn đặc trưng và phân tích độ nhạy?
3. Chuẩn hóa và momentum ảnh hưởng thế nào đến tốc độ hội tụ của hồi quy tuyến tính trên dữ liệu này?
4. MLP có lợi thế so với hồi quy tuyến tính ở những giờ hoặc loại ngày nào?

### g) Lưu ý khi thực hiện
- Thời tiết trong bộ dữ liệu là số liệu đã xảy ra (tái phân tích từ vệ tinh), không phải dự báo thời tiết; dùng nó tương đương giả định dự báo thời tiết hoàn hảo — nêu rõ hạn chế này.
- Không xáo trộn ngẫu nhiên và không dùng k-fold thông thường; dùng kiểm định trượt theo thời gian.
- MAPE nhạy với những giờ phụ tải thấp bất thường (sự cố, mất điện diện rộng); kiểm tra và nêu cách xử lý.

## 3. Biểu điểm Phần I (mục 3) — điểm chung của nhóm, thang 10
### 3.1. Điều kiện chung để một ý được tính điểm
- (a) Có mã nguồn tương ứng chạy lại được; báo cáo ghi rõ tệp, hàm hoặc ô notebook sinh ra kết quả (bảng truy vết ở Phụ lục D).
- (b) Số liệu trong báo cáo khớp với kết quả chạy lại, chỉ sai khác do làm tròn. Số liệu không tái lập được thì ý đó không được tính điểm.
- (c) Có nhận xét, giải thích ý nghĩa; chỉ dán kết quả mà không phân tích thì được tối đa một nửa số điểm của ý.
- (d) Không rò rỉ dữ liệu: chuẩn hóa, mã hóa, xây dựng đặc trưng, PCA, LDA, chọn đặc trưng, chọn siêu tham số và chọn ngưỡng chỉ được "học" trên tập huấn luyện hoặc tập kiểm định; tập kiểm tra chỉ dùng một lần để báo cáo kết quả cuối cùng.
- (e) Mỗi ý chấm ba mức: đạt đầy đủ (100% điểm của ý), đạt một phần (50%), không đạt hoặc không có (0).
- Với đề 3 (hồi quy), các yêu cầu phân lớp ở B4 và B7 dùng bài toán phụ "giờ cao điểm cần cảnh báo".

### 3.2. Bảng tổng hợp
| Khối | Nội dung | Điểm |
|---|---|---|
| B1 | Bài toán, dữ liệu, EDA và chia dữ liệu | 1,0 |
| B2 | Cơ sở lý thuyết và trích dẫn | 0,75 |
| B3 | Tối ưu Gradient Descent (chương 1) | 1,25 |
| B4 | Perceptron và Pocket (chương 2) | 1,0 |
| B5 | Mạng neural nhiều lớp và lan truyền ngược (chương 3) | 2,0 |
| B6 | Đặc trưng và giảm chiều (chương 4) | 1,5 |
| B7 | Tính tay đối chiếu với mã | 0,75 |
| B8 | Yêu cầu riêng của đề (R1–R4) | 1,0 |
| B9 | Đánh giá tổng hợp, thảo luận, kết luận | 0,5 |
| B10 | Hình thức, mã nguồn, khả năng tái lập | 0,25 |
| | Tổng Phần I | 10,0 |

### 3.3. Yêu cầu chi tiết từng khối (cột: Mã | Nội dung bắt buộc | Điều kiện được tính điểm | Điểm)
**B1 (1,0)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B1.1 | Phát biểu bài toán nghiệp vụ: ai dùng kết quả, ra quyết định gì, chi phí của từng loại sai; biến mục tiêu; chỉ số đánh giá chính và lý do chọn | Chỉ số chính phù hợp với bài toán (không dùng accuracy cho dữ liệu mất cân bằng); nêu chi phí sai lầm bằng ví dụ cụ thể | 0,25 |
| B1.2 | Mô tả dữ liệu: nguồn, giấy phép, trích dẫn bài báo gốc, ngày tải, kích thước tệp; từ điển dữ liệu (tên biến, ý nghĩa, đơn vị, kiểu, thang đo) | Đủ các thông tin; từ điển dữ liệu bao phủ mọi biến được dùng | 0,25 |
| B1.3 | EDA: thống kê mô tả, phân bố nhãn hoặc biến mục tiêu, giá trị thiếu, ngoại lai, tương quan; ít nhất 4 hình có nhận xét | Mỗi hình có ít nhất một nhận xét định lượng; phát hiện ít nhất một vấn đề của dữ liệu và nêu cách xử lý | 0,25 |
| B1.4 | Tiền xử lý và chia dữ liệu: xử lý thiếu, ngoại lai, mã hóa; chia huấn luyện/kiểm định/kiểm tra đúng quy định của đề (theo thời gian, phân tầng hoặc theo nhóm); bảng kích thước và tỉ lệ nhãn của từng tập | Dùng SEED = 2026 + G; không mẫu (khách hàng, địa điểm) nào thuộc hai tập; mọi phép biến đổi chỉ khớp (fit) trên tập huấn luyện | 0,25 |

**B2 (0,75)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B2.1 | Trình bày ngắn gọn, ký hiệu thống nhất: GD, SGD, mini-batch, momentum; perceptron, hàm mất mát perceptron, PLA, Pocket; MLP, hàm kích hoạt, hàm mất mát, lan truyền ngược (BP1–BP4); PCA, LDA, chọn đặc trưng; các chỉ số đánh giá dùng trong báo cáo | Bám sát tài liệu theo chỉ dẫn của đề cương: chương 1 – [2, tr. 158–173]; chương 2 – [2, tr. 175–183]; chương 3 – [1, tr. 115–146], [2, tr. 214–232]; chương 4 – [1, tr. 88–99, 521–567]; tối ưu – [3, chương 9]. Mỗi mục có trích dẫn; không chép nguyên văn quá 3 dòng liên tiếp | 0,5 |
| B2.2 | Ít nhất một suy dẫn do nhóm tự viết từng bước, chọn trong: (a) ∂J/∂z = ŷ − y với sigmoid + BCE hoặc softmax + entropy chéo; (b) gradient của BCE có trọng số lớp; (c) hướng chiếu PCA là véc tơ riêng ứng với trị riêng lớn nhất (thương Rayleigh); (d) nghiệm LDA hai lớp w ∝ S_W⁻¹(m1 − m0) | Suy dẫn đúng, đủ bước, ký hiệu khớp với mã | 0,25 |

**B3 (1,25)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B3.1 | Tự cài đặt GD theo lô, SGD và mini-batch cho mô hình tuyến tính của đề (hồi quy tuyến tính cho đề 3); viết rõ hàm mất mát có chính quy hóa L2 và gradient | Mã NumPy tự viết; công thức trong báo cáo khớp mã; đường mất mát giảm và ổn định | 0,5 |
| B3.2 | Tự cài đặt GD với momentum (khuyến khích thêm Nesterov hoặc Adam); so sánh với GD thường trên cùng một hình mất mát theo số lần cập nhật | Cùng điểm khởi tạo, cùng η; nêu số lần cập nhật để đạt cùng một mức mất mát | 0,25 |
| B3.3 | Thí nghiệm tốc độ học: ít nhất 4 giá trị η theo thang log (ví dụ 10⁻³, 10⁻², 10⁻¹, 1), chỉ ra trường hợp hội tụ chậm, dao động, phân kỳ; ảnh hưởng của chuẩn hóa z-score đến tốc độ hội tụ | Có hình và bảng; giải thích bằng độ cong của hàm mất mát (số điều kiện), liên hệ chương 1 và [3, chương 9] | 0,25 |
| B3.4 | Kiểm tra tính đúng: (a) kiểm tra gradient bằng sai phân hữu hạn trên một mẫu con nhỏ; (b) so với lời giải tham chiếu: nghiệm giải tích (hồi quy tuyến tính) hoặc scikit-learn cùng hệ số chính quy hóa (logistic, softmax) | (a) sai số tương đối không quá 10⁻⁶ (float64); (b) chỉ số trên tập kiểm định chênh không quá 0,005 hoặc giải thích được nguyên nhân | 0,25 |

**B4 (1,0)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B4.1 | Tự cài đặt PLA và Pocket; nêu rõ quy ước: nhãn ±1, véc tơ mở rộng x̃ = (x, 1), khởi tạo w̃ = 0, mẫu có y·g ≤ 0 là sai (kể cả g = 0), thứ tự duyệt, điều kiện dừng | Mã tự viết đúng quy ước | 0,25 |
| B4.2 | Kiểm tra khả tách tuyến tính của tập huấn luyện bằng bài toán quy hoạch tuyến tính khả thi [3, §8.6.1] với scipy.optimize.linprog, hoặc bằng việc PLA không hội tụ sau số epoch đủ lớn | Kết luận có căn cứ định lượng: trạng thái nghiệm của bài toán LP, hoặc số lỗi theo epoch | 0,25 |
| B4.3 | Thực nghiệm: số lỗi theo epoch của PLA và Pocket; ảnh hưởng của chuẩn hóa và thứ tự duyệt (ít nhất 5 hạt giống); kiểm chứng tính bất biến theo η khi w̃(0) = 0 | Có hình số lỗi theo epoch; bảng trung bình ± độ lệch chuẩn qua các lần chạy | 0,25 |
| B4.4 | So sánh perceptron với mô hình tuyến tính ở B3 và MLP ở B5 trên cùng tập kiểm định; vẽ vùng quyết định trên mặt phẳng hai đặc trưng (hoặc hai thành phần chính) của perceptron và MLP | Giải thích khác biệt qua hàm mất mát (J_P không phạt mẫu đúng nằm sát biên) và giới hạn của biên tuyến tính (liên hệ bài toán XOR) | 0,25 |

**B5 (2,0)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B5.1 | Tự cài đặt MLP bằng NumPy: lan truyền thuận dạng lô (ma trận), lan truyền ngược theo δ(l) (BP1–BP4), cập nhật mini-batch; ít nhất hai hàm kích hoạt ẩn (sigmoid, tanh, ReLU) và tầng ra phù hợp: tuyến tính + MSE (đề 3) | Công thức trong báo cáo khớp mã; mạng huấn luyện được (mất mát giảm) | 0,5 |
| B5.2 | Kiểm tra gradient bằng sai phân hữu hạn cho toàn bộ tham số trên ít nhất 2 kiến trúc, trong đó một kiến trúc có từ 2 tầng ẩn trở lên | Sai số tương đối không quá 10⁻⁶ (float64); bảng sai số theo từng ma trận trọng số | 0,25 |
| B5.3 | Thực nghiệm kiến trúc và khởi tạo: ít nhất 3 cấu hình độ rộng/độ sâu; khởi tạo bằng 0 hoặc hằng số so với Xavier/He; ít nhất 2 hàm kích hoạt ẩn | Bảng kết quả trên tập kiểm định; giải thích hiện tượng đối xứng khi khởi tạo hằng số, bão hòa và gradient biến mất khi dùng sigmoid nhiều tầng | 0,5 |
| B5.4 | Tối ưu và chính quy hóa: so sánh ít nhất SGD mini-batch và momentum (tự cài đặt); L2 và dừng sớm (dropout khuyến khích); đường cong học huấn luyện – kiểm định; chẩn đoán quá khớp, thiếu khớp | Siêu tham số chọn trên tập kiểm định (hoặc k-fold trên tập huấn luyện), không chọn trên tập kiểm tra | 0,5 |
| B5.5 | Đối chứng với thư viện: cùng kiến trúc và siêu tham số trong scikit-learn (MLPRegressor) hoặc PyTorch | Chênh lệch chỉ số chính được giải thích (khởi tạo, bộ tối ưu, điều kiện dừng) | 0,25 |

**B6 (1,5)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B6.1 | Phân tích đặc trưng gốc: thang đo (định danh, thứ bậc, khoảng, tỉ lệ); tiêu chí Fisher (đề 2 thêm IV) cho từng đặc trưng; ma trận tương quan và các nhóm đặc trưng dư thừa | Bảng xếp hạng đặc trưng; nhận xét ít nhất 3 đặc trưng mạnh hoặc yếu bằng ý nghĩa nghiệp vụ | 0,25 |
| B6.2 | Xây dựng ít nhất 5 đặc trưng mới có cơ sở nghiệp vụ (gợi ý trong từng đề); bảng: tên, công thức, ý nghĩa, Fisher (hoặc IV) trước và sau | Mọi thống kê dùng để tạo đặc trưng chỉ tính trên tập huấn luyện; không dùng thông tin của tương lai | 0,5 |
| B6.3 | PCA tự cài đặt (trị riêng hoặc SVD), đối chiếu sklearn.decomposition.PCA; biểu đồ phương sai giải thích và tích lũy; chọn k có lý do; sai số tái tạo; diễn giải ít nhất 2 thành phần chính qua hệ số tải (loadings) | Chuẩn hóa trước PCA khi biến khác đơn vị (hoặc giải thích vì sao không); trị riêng khớp thư viện đến 10⁻⁶ | 0,25 |
| B6.4 | LDA tự cài đặt (S_W, S_B, bài toán trị riêng tổng quát) cho bài toán phân lớp của đề (đề 3: phân loại loại ngày ở R4); chọn đặc trưng theo ít nhất 2 họ: lọc (Fisher, IV, tương quan), bọc (SFS), nhúng (L1) | Chọn đặc trưng thực hiện bên trong vòng kiểm định hoặc chỉ trên tập huấn luyện; liệt kê đặc trưng được giữ lại | 0,25 |
| B6.5 | Bảng so sánh cùng một mô hình (mô hình tuyến tính ở B3 và MLP) với: (i) đặc trưng gốc; (ii) gốc + đặc trưng mới; (iii) k thành phần chính; (iv) sau chọn đặc trưng; nhận xét theo hiện tượng Hughes và đường cong học | Cùng cách chia dữ liệu, cùng chỉ số; có khoảng tin cậy hoặc độ lệch chuẩn | 0,25 |

**B7 (0,75) — trình bày ở Phụ lục A của báo cáo.** Quy tắc chọn mẫu (bắt buộc): dùng bài toán hai lớp "giờ cao điểm"; lấy 3 mẫu lớp +1 và 3 mẫu lớp −1 từ tập huấn luyện theo đoạn mã dưới đây (cũng là `hand_calc.select_six_samples`), thứ tự duyệt xen kẽ +, −, +, −, +, −; dùng hai đặc trưng có tiêu chí Fisher lớn nhất cho bài toán hai lớp đó, đã chuẩn hóa z-score theo tập huấn luyện. Mọi giá trị làm tròn 4 chữ số thập phân; hồi quy logistic dùng nhãn y ∈ {0, 1}, PLA dùng nhãn ±1.
```
rng = np.random.default_rng(SEED)           # SEED = 2026 + G
pos_idx = np.flatnonzero(y_train == 1)      # thứ tự của tập huấn luyện
neg_idx = np.flatnonzero(y_train != 1)
p = rng.choice(pos_idx, 3, replace=False)
n = rng.choice(neg_idx, 3, replace=False)
idx = [p[0], n[0], p[1], n[1], p[2], n[2]]  # thứ tự duyệt
```
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B7.1 | (a) Một bước GD theo lô cho hồi quy logistic trên 6 mẫu (2 trọng số + hệ số tự do), w̃(0) = 0, η = 0,1, J là trung bình BCE không chính quy hóa: tính ŷ, J, ∇J, w̃(1) và J sau cập nhật. (b) Một epoch PLA trên 6 mẫu theo thứ tự quy định, w̃(0) = 0: ghi từng bước g, y·g, có cập nhật hay không, w̃ sau mỗi bước | Trình bày từng bước; sai khác so với kết quả mã không quá 10⁻⁴ | 0,25 |
| B7.2 | Một bước lan truyền thuận và ngược cho mạng 2–2–1 (sigmoid ở tầng ẩn và tầng ra, BCE) trên mẫu thứ nhất trong 6 mẫu. Khởi tạo: hàng 1 của W(1) = (0,2; −0,3), hàng 2 = (0,4; 0,1); b(1) = (0; 0); w(2) = (0,5; −0,6); b(2) = 0; η = 0,5. Tính z(1), a(1), ŷ, J, δ(2), δ(1), các gradient, tham số mới và J sau cập nhật | Như B7.1; thêm kiểm chứng ít nhất một đạo hàm bằng sai phân hữu hạn | 0,25 |
| B7.3 | PCA trên 6 mẫu × 2 đặc trưng: véc tơ trung bình, ma trận hiệp phương sai (chia n − 1), hai trị riêng, hai véc tơ riêng đơn vị (dấu chọn sao cho thành phần có trị tuyệt đối lớn nhất là dương), tỉ lệ phương sai giải thích, tọa độ chiếu của mẫu thứ nhất. LDA hai lớp trên cùng 6 mẫu: m+, m−, S_W, w ∝ S_W⁻¹(m+ − m−) chuẩn hóa ‖w‖ = 1, giá trị chiếu của 6 mẫu | Như B7.1; nếu S_W suy biến thì cộng 10⁻³·I và nêu rõ | 0,25 |

Ghi chú nhóm (không phải của đề): đề không nói rõ nhãn cho B7.2 (BCE); nhóm chốt dùng {0, 1} như B7.1 (docs/CONVENTIONS.md mục 3 và 7).

**B8 (1,0):** bốn yêu cầu R1–R4 (mục 2e ở trên), mỗi yêu cầu 0,25 điểm, chấm theo điều kiện kèm theo và theo mục 3.1.

**B9 (0,5)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B9.1 | Bảng tổng hợp mọi mô hình trên tập kiểm tra (dùng một lần) kèm mô hình cơ sở (đề 3 ghi sẵn); khoảng tin cậy 95% bằng bootstrap (ít nhất 1.000 lần lặp) cho chỉ số chính, hoặc trung bình ± độ lệch chuẩn qua nhiều hạt giống; kết luận chênh lệch có ý nghĩa hay không | Không chọn lại mô hình sau khi đã xem kết quả trên tập kiểm tra | 0,25 |
| B9.2 | Phân tích lỗi (ít nhất 10 mẫu dự đoán sai, phân nhóm nguyên nhân); hạn chế của nghiên cứu; khuyến nghị triển khai và giám sát (trôi dữ liệu, cập nhật mô hình); trả lời đủ bốn câu hỏi nghiên cứu của đề trong phần Kết luận | Câu trả lời dựa trên số liệu của chính nhóm | 0,25 |

**B10 (0,25)**
| Mã | Nội dung bắt buộc | Điều kiện | Điểm |
|---|---|---|---|
| B10.1 | Báo cáo đúng cấu trúc ở mục 5 và quy định ở mục 2.3; mã nguồn đúng cấu trúc ở Phụ lục 2, chạy lại toàn bộ bằng một lệnh (hoặc "Restart and run all" với notebook) và tái tạo đúng các bảng, hình chính; có bảng truy vết số liệu (Phụ lục D của báo cáo) | Giảng viên chạy lại được trong không quá 60 phút | 0,25 |

## 4. Quy định chung
### 2.2. Hồ sơ phải nộp
1. Báo cáo dạng .docx và .pdf, đặt tên `HMNC_BCCD_N<G>_De<k>`, ví dụ HMNC_BCCD_N07_De3.pdf. (Nhóm 18: `HMNC_BCCD_N18_De3`.)
2. Mã nguồn theo cấu trúc Phụ lục 2, nén .zip; hoặc kho GitHub chế độ riêng tư có mời giảng viên. Lịch sử commit phải thể hiện phần việc của từng thành viên.
3. README.md: phiên bản Python và thư viện (kèm requirements.txt); cách tải dữ liệu (đường dẫn gốc, ngày tải, kích thước tệp hoặc mã băm SHA-256); lệnh chạy lại toàn bộ kết quả.
4. Slide trình bày, tối đa 15 trang chiếu.
5. Hai phụ lục bắt buộc nằm trong báo cáo: bảng phân công có tỉ lệ đóng góp và chữ ký; bản khai báo sử dụng công cụ AI (mẫu Phụ lục 3 của đề).
Không nộp kèm dữ liệu gốc dung lượng lớn; chỉ nộp script tải dữ liệu hoặc hướng dẫn tải.

### 2.3. Hình thức báo cáo
- Khổ A4, Times New Roman cỡ 13, giãn dòng 1,3; lề trên 2 cm, dưới 2 cm, trái 3 cm, phải 2 cm; số trang ở giữa chân trang.
- Phần thân (từ Chương 1 đến hết Kết luận) dài 25–35 trang, khuyến nghị khoảng 30 trang; không tính bìa, lời cam đoan, mục lục, danh mục hình và bảng, bảng ký hiệu, tài liệu tham khảo và phụ lục. Phụ lục không quá 15 trang.
- Trong phần thân chỉ trích đoạn mã ngắn (mỗi đoạn không quá 15 dòng, tổng không quá 3 trang); mã đầy đủ nằm trong thư mục nộp kèm.
- Hình và bảng đánh số theo chương (Hình 3.2, Bảng 4.1), có chú thích, ghi nguồn nếu không do nhóm tạo và phải được nhắc đến trong văn bản; đồ thị có tên trục và đơn vị.
- Công thức đánh số theo chương, ví dụ (3.1); ký hiệu thống nhất, liệt kê trong bảng ký hiệu.
- Văn bản dùng dấu phẩy thập phân (0,875); bảng xuất trực tiếp từ mã có thể giữ dấu chấm nhưng nhất quán trong cùng một bảng.
- Tài liệu tham khảo theo chuẩn IEEE hoặc APA, nhất quán. Bắt buộc có [1], [2], [3] và bài báo gốc của bộ dữ liệu; trích dẫn ghi đến chương, mục hoặc trang, ví dụ [2, tr. 214–232].

### 2.4. Công cụ và phạm vi tự cài đặt
- Ngôn ngữ khuyến nghị: Python 3.10 trở lên với NumPy, pandas, Matplotlib, SciPy. Ngôn ngữ khác trong đề cương (C++, Java, .NET) cho phần tự cài đặt chỉ khi giảng viên đồng ý.
- scikit-learn được dùng cho tiền xử lý, chia dữ liệu, tính chỉ số và làm mô hình đối chứng; PyTorch hoặc TensorFlow chỉ để đối chứng, không bắt buộc.
- Phần bắt buộc tự cài đặt bằng NumPy, không autograd, không gọi mô hình có sẵn cho phần lõi: (i) GD theo lô, SGD, mini-batch và momentum cho mô hình tuyến tính; (ii) PLA và Pocket; (iii) MLP: lan truyền thuận, lan truyền ngược, cập nhật tham số, kiểm tra gradient bằng sai phân hữu hạn; (iv) PCA (trị riêng của ma trận hiệp phương sai hoặc SVD) và LDA (Fisher).
- Mã chạy được trên máy cá nhân hoặc Google Colab bản miễn phí, tổng thời gian chạy lại không quá 60 phút (không tính tải dữ liệu và bước trích đặc trưng tín hiệu một lần của đề 5). Khi dữ liệu lớn được lấy mẫu con cho thí nghiệm phụ nhưng phải nêu rõ cách lấy mẫu và giữ nguyên tập kiểm tra.

### 2.5. Mốc thời gian
| Mốc | Thời hạn | Ngày | Nội dung |
|---|---|---|---|
| 1 | T0 + 1 tuần | 11/11/2026 | Đăng ký nhóm: danh sách thành viên, nhóm trưởng, đề chọn |
| 2 | T0 + 3 tuần | 30/11/2026 | Nộp báo cáo tiến độ 2–3 trang: kết quả EDA, cách chia dữ liệu, kết quả GD và perceptron ban đầu, kế hoạch phần còn lại. Không chấm điểm, giảng viên góp ý; không nộp bị trừ 0,5 điểm Phần I |
| 3 | T0 + 6 tuần | 25/12/2026 | Nộp hồ sơ cuối theo mục 2.2 |
| 4 | Theo lịch thi (lịch chính thức, Phi xác nhận 20/11/2026) | 30/12/2026 | Trình bày và vấn đáp; mọi thành viên phải có mặt |

### 6.1–6.3. Bảo vệ và công thức điểm
- 6.1 Điều kiện chấm: đăng ký đúng hạn, đúng đề và bộ dữ liệu; hồ sơ đủ mục 2.2; không sao chép (vi phạm: 0 điểm bài thi và xử lý theo quy chế); sinh viên có mặt (vắng không lý do: 0 điểm bài thi).
- 6.2 Phần II (thang 10, chấm từng sinh viên): trình bày tối đa 12 phút, mọi thành viên trình bày phần mình; mỗi thành viên trả lời ít nhất ba câu hỏi cá nhân (II.2–II.4); giảng viên có thể yêu cầu chạy lại một đoạn mã, đổi nhanh một tham số và giải thích. Thời lượng bài thi theo đề cương 50 phút (lịch cụ thể theo thông báo của Khoa).

| Mã | Nội dung | Điểm |
|---|---|---|
| II.1 | Trình bày: đúng thời gian; cấu trúc rõ; nêu kết quả chính bằng số liệu; slide dễ đọc; trả lời đúng trọng tâm | 2,0 |
| II.2 | Câu hỏi về phần mình phụ trách: giải thích mã, công thức, lựa chọn thiết kế của phần việc ghi tên sinh viên trong bảng phân công | 3,0 |
| II.3 | Câu hỏi tính nhanh hoặc suy luận trên số liệu của nhóm (tính lại một bước cập nhật; dự đoán điều gì xảy ra khi tăng η hoặc bỏ chuẩn hóa; đọc và giải thích một ô của ma trận nhầm lẫn) | 2,5 |
| II.4 | Câu hỏi về phần do thành viên khác thực hiện: kiểm tra mức hiểu toàn bộ báo cáo | 2,5 |
| | Tổng Phần II | 10,0 |

Mỗi câu chấm bốn mức: đúng và nêu được bản chất (100%); đúng nhưng lúng túng ở chi tiết (60–80%); chỉ trả lời được một phần (30–50%); không trả lời được (0).
- 6.3 Điểm Phần I (thang 10) là điểm chung của nhóm, đã cộng điểm khuyến khích (6.5) và trừ điểm (6.4), không âm và không quá 10. Hệ số đóng góp k_i do giảng viên xác định từ bảng phân công, lịch sử commit và kết quả vấn đáp: 1,0 đầy đủ; 0,8 ít hơn rõ rệt; 0,5 không đáng kể; 0 không tham gia (nhóm xác nhận, hoặc không trả lời được câu nào về phần được giao). Nếu Phần II dưới 3,0 vì không giải thích được phần việc của mình thì k_i không quá 0,5.
  **Điểm thi của sinh viên i = 0,6 × k_i × Điểm Phần I + 0,4 × Điểm Phần II của sinh viên i.**

### 6.4. Các trường hợp trừ điểm (trừ vào Phần I)
| Trường hợp | Mức trừ |
|---|---|
| Nộp hồ sơ cuối muộn | 1,0 điểm mỗi ngày; quá 3 ngày không nhận bài (Phần I = 0) |
| Không nộp báo cáo tiến độ (mốc 2) | 0,5 điểm |
| Phần thân ngoài khoảng 25–35 trang | 0,5 điểm; ngoài khoảng 20–40 trang: 1,0 điểm |
| Dùng tập kiểm tra để chọn mô hình, siêu tham số, ngưỡng hoặc đặc trưng | 0,5 điểm; kết quả liên quan không được tính điểm |
| Hình, bảng không đánh số hoặc không ghi nguồn; tài liệu tham khảo thiếu hoặc không được trích dẫn trong văn bản | 0,25 – 0,5 điểm |
| Không chạy lại được bất kỳ kết quả nào từ mã nộp kèm | Phần I tối đa 3,0 điểm |

### 6.5. Điểm khuyến khích (cộng vào Phần I, tối đa 0,5 điểm)
- Tự cài đặt Adam hoặc Nesterov và phân tích đúng ảnh hưởng so với momentum: 0,25.
- Kiểm định thống kê ghép cặp giữa hai mô hình tốt nhất (bootstrap ghép cặp, McNemar hoặc DeLong): 0,25.
- Tái lập được một bảng hoặc hình trong bài báo gốc của bộ dữ liệu và giải thích chênh lệch: 0,25.
- Ứng dụng minh họa chạy được (ví dụ Streamlit hoặc Gradio) kèm chỉ số giám sát trôi dữ liệu như PSI: 0,25.

### 7. Liêm chính học thuật và sử dụng công cụ AI
- Được phép (khai báo ở Phụ lục C): tra cứu khái niệm; hỏi cách dùng hàm thư viện; nhờ tìm lỗi cú pháp, gợi ý gỡ lỗi; sửa chính tả và diễn đạt câu chữ.
- Không được phép: dùng AI sinh nguyên đoạn báo cáo, hoặc sinh mã cho các phần bắt buộc tự cài đặt ở mục 2.4 rồi nộp khi chưa hiểu; tạo số liệu, bảng, hình không có trong kết quả chạy; đưa vào báo cáo trích dẫn không tồn tại hoặc chưa đọc.
- Bắt buộc: mọi thành viên giải thích được mọi đoạn mã thuộc phần tự cài đặt và mọi con số trong báo cáo. Mã tham khảo (Kaggle, GitHub, sách, bài giảng) ghi nguồn ngay tại chỗ (chú thích trong mã) và trong tài liệu tham khảo; phần tự cài đặt không lấy từ nguồn ngoài.
- Hệ quả: khai báo trung thực không bị trừ điểm. Dùng không khai báo, hoặc không giải thích được phần việc khi vấn đáp, thì k_i và Phần II của người liên quan được xem xét lại theo 6.3; nghiêm trọng xử lý theo quy chế.

## 5. Cấu trúc báo cáo (mục 5, Bảng 3)
| Phần | Nội dung chính | Số trang | Khối chấm |
|---|---|---|---|
| Bìa (mẫu Phụ lục 1), lời cam đoan, mục lục, danh mục hình và bảng, bảng ký hiệu và chữ viết tắt | | Không tính | B10 |
| Chương 1. Tổng quan bài toán và dữ liệu | Bối cảnh, phát biểu bài toán, chỉ số đánh giá; nguồn dữ liệu; EDA; tiền xử lý; chia dữ liệu | 4–5 | B1 |
| Chương 2. Cơ sở lý thuyết | GD, SGD, momentum; perceptron, PLA, Pocket; MLP và lan truyền ngược; đặc trưng, PCA, LDA, chọn đặc trưng; chỉ số đánh giá | 5–6 | B2 |
| Chương 3. Xây dựng đặc trưng và giảm chiều | Phân tích đặc trưng gốc; đặc trưng mới; PCA; LDA; chọn đặc trưng; bảng so sánh | 5–6 | B6 |
| Chương 4. Mô hình tuyến tính: tối ưu GD và perceptron | Mô hình tuyến tính với GD, SGD, mini-batch, momentum; thí nghiệm tốc độ học; perceptron, Pocket; kiểm tra khả tách | 5–6 | B3, B4 |
| Chương 5. Mạng neural nhiều lớp | Cài đặt, kiểm tra gradient, thực nghiệm kiến trúc, khởi tạo, tối ưu, chính quy hóa; đối chứng thư viện | 5–6 | B5 |
| Chương 6. Đánh giá tổng hợp và yêu cầu riêng của đề | Bảng kết quả trên tập kiểm tra, khoảng tin cậy; R1–R4; phân tích lỗi; thảo luận | 4–5 | B8, B9 |
| Kết luận và hướng phát triển | Trả lời bốn câu hỏi nghiên cứu; hạn chế; khuyến nghị triển khai | 1 | B9 |
| Tài liệu tham khảo | IEEE hoặc APA | Không tính | B2, B10 |
| Phụ lục A. Tính tay đối chiếu | Ba phần B7.1–B7.3, kèm đoạn mã in kết quả đối chiếu | Tối đa 4 | B7 |
| Phụ lục B. Bảng phân công và tỉ lệ đóng góp | Có chữ ký của các thành viên (mẫu Phụ lục 3) | 1 | Mục 6, mục 7 |
| Phụ lục C. Khai báo sử dụng công cụ AI | Theo mẫu Phụ lục 3 | 1 | B10 |
| Phụ lục D. Hướng dẫn chạy mã và bảng truy vết | Mỗi bảng, hình trong báo cáo ứng với tệp, hàm hoặc ô notebook nào | 1–2 | UNKNOWN (bảng trích không rõ cột khối chấm của dòng này) |

Thân = Chương 1 đến Kết luận, khoảng 30 trang, phải nằm trong 25–35. Phụ lục không quá 15 trang.

## 6. Tài liệu tham khảo bắt buộc (mục 8) và chỉ dẫn trang (B2.1)
- [1] Đinh Mạnh Tường (2015). *Học máy: các kỹ thuật cơ bản và hiện đại*. NXB Đại học Quốc gia Hà Nội.
- [2] Fukunaga, K. (1990). *Introduction to Statistical Pattern Recognition* (2nd ed.). Academic Press.
- [3] Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press.
- [7] Aguilar Madrid, E., & Antonio, N. (2021). Short-term electricity load forecasting with machine learning. *Information*, 12(2), 50. https://doi.org/10.3390/info12020050 (Đề 3)
- [8] Aguilar Madrid, E. (2021). Short-term electricity load forecasting (Panama case study) [Dataset]. Mendeley Data, V1. https://doi.org/10.17632/byx7sztj59.1 (Đề 3)

| Nội dung | Chỉ dẫn trang theo B2.1 |
|---|---|
| Chương 1 (GD) | [2, tr. 158–173] |
| Chương 2 (perceptron) | [2, tr. 175–183] |
| Chương 3 (MLP) | [1, tr. 115–146], [2, tr. 214–232] |
| Chương 4 (đặc trưng, PCA, LDA, chọn đặc trưng) | [1, tr. 88–99, 521–567] |
| Tối ưu | [3, chương 9]; kiểm tra khả tách (B4.2): [3, §8.6.1] |

## 7. Cấu trúc thư mục nộp (Phụ lục 2, tóm tắt)
`README.md`, `requirements.txt`, `run_all.py`, `data/` (để trống khi nộp, có `download_data.py` in kích thước và mã băm), `src/` (`data_prep.py`, `features.py`, `optim_linear.py`, `perceptron.py`, `mlp.py`, `evaluate.py`, `hand_calc.py`), `notebooks/` (tùy chọn), `results/figures/`, `results/tables/`. README tối thiểu: phiên bản Python và thư viện; nguồn dữ liệu, ngày tải, kích thước/SHA-256; lệnh chạy lại toàn bộ (ví dụ `python run_all.py --seed 2033`) và thời gian chạy ước tính; bảng ánh xạ tệp kết quả với số hình, số bảng.
