# CHECKLIST — việc cố định theo phase (chỉ Phi sửa)

- Chỉ Phi sửa file này. Người làm xong thì báo Phi; Phi đổi ☐ → ☑ khi việc xong VÀ có bằng chứng (mã chạy lại được, tệp kết quả trong `results/`, dòng truy vết trong `docs/trace_<tên>.md`).
- Mã (B1.1…B10.1, R1…R4) khớp mã chấm của đề; mỗi mã xuất hiện đúng một lần. Chi tiết nguyên văn: `docs/DE3.md`. Quy ước: `docs/CONVENTIONS.md`. Thông số: `src/config.py`.
- Nhóm 18, SEED = 2044. Tổng điểm Phần I = 10,0 (chưa tính khuyến khích tối đa 0,5 và trừ điểm 6.4).

## Điều kiện chung 3.1 (a)–(e) — áp dụng cho mọi ý
- ☐ (a) Có mã nguồn chạy lại được; báo cáo ghi rõ tệp, hàm hoặc ô notebook sinh kết quả (bảng truy vết = Phụ lục D, từ `docs/trace_*.md`).
- ☐ (b) Số liệu trong báo cáo khớp kết quả chạy lại (chỉ khác do làm tròn); không tái lập được thì ý đó không được tính điểm.
- ☐ (c) Mỗi kết quả có nhận xét, giải thích ý nghĩa; chỉ dán kết quả thì tối đa một nửa điểm của ý.
- ☐ (d) Không rò rỉ: chuẩn hóa, mã hóa, đặc trưng, PCA, LDA, chọn đặc trưng, siêu tham số, ngưỡng chỉ học trên train/val; tập kiểm tra dùng một lần.
- ☐ (e) Hiểu cách chấm ba mức: 100% / 50% / 0 cho từng ý.

## Phase

### P1 — Dữ liệu (đến 22/11/2026)
| Mã | Việc phải có | Điều kiện được điểm | Điểm | Người | Tệp kết quả / nơi nộp | ☐ |
|---|---|---|---|---|---|---|
| B1.1 | Phát biểu bài toán nghiệp vụ: ai dùng, ra quyết định gì, chi phí từng loại sai; biến mục tiêu; chỉ số chính (MAPE trung bình các tuần) và lý do chọn | Chỉ số chính phù hợp bài toán; nêu chi phí sai lầm bằng ví dụ cụ thể | 0,25 | Huấn | Báo cáo Chương 1; `docs/trace_huan.md` | ☐ |
| B1.2 | Mô tả dữ liệu: nguồn, giấy phép (CC BY 4.0), trích dẫn bài báo gốc [7] và dữ liệu [8], ngày tải, kích thước tệp; từ điển dữ liệu (tên biến, ý nghĩa, đơn vị, kiểu, thang đo) | Đủ thông tin; từ điển bao phủ mọi biến được dùng | 0,25 | Huấn | `docs/DATA_DICTIONARY.md`; README (ngày tải, kích thước/SHA-256); Chương 1 | ☐ |
| B1.4 | Tiền xử lý và chia dữ liệu: xử lý thiếu, ngoại lai (giờ tải < 50% trung vị), mã hóa; chia theo tuần Thứ Bảy → Thứ Sáu 209/26/37/14 tuần; bảng kích thước và tỉ lệ nhãn "giờ cao điểm" từng tập | SEED = 2044; không mẫu nào thuộc hai tập; mọi phép biến đổi chỉ fit trên train | 0,25 | Phi | `src/data_prep.py`; `results/tables/1_*_split_sizes.csv` (tên theo CONVENTIONS mục 5) | ☐ |

### P2 — Tiến độ (đến 30/11/2026)
Nộp báo cáo tiến độ 2–3 trang (kết quả EDA, cách chia dữ liệu, kết quả GD và perceptron ban đầu, kế hoạch phần còn lại). Không nộp bị trừ 0,5 điểm Phần I (không chấm điểm, giảng viên góp ý).
| Mã | Việc phải có | Điều kiện được điểm | Điểm | Người | Tệp kết quả / nơi nộp | ☐ |
|---|---|---|---|---|---|---|
| TĐ | Báo cáo tiến độ 2–3 trang nộp đúng hạn (không phải mã chấm của đề; tránh trừ 0,5) | Nộp trước 30/11/2026; nội dung đủ 4 ý ở trên | (tránh −0,5) | Huấn soạn (mỗi người cấp phần của mình), Phi duyệt | Nơi nộp theo thông báo của giảng viên (UNKNOWN: hỏi Phi) | ☐ |
| B1.3 | EDA: thống kê mô tả, phân bố biến mục tiêu/nhãn, giá trị thiếu, ngoại lai, tương quan; ≥ 4 hình có nhận xét | Mỗi hình ≥ 1 nhận xét định lượng; ≥ 1 vấn đề của dữ liệu và cách xử lý | 0,25 | Huấn | `notebooks/huan_*`; `results/figures/1_*` | ☑ |
| B3.1 | Tự cài đặt GD theo lô, SGD, mini-batch cho hồi quy tuyến tính (MSE + L2); viết rõ hàm mất mát và gradient | Mã NumPy tự viết; công thức trong báo cáo khớp mã; mất mát giảm và ổn định | 0,5 | Huấn | `src/optim_linear.py`; `results/figures/4_*` | ☐ |
| B3.2 | Tự cài đặt GD với momentum (khuyến khích Nesterov/Adam); so sánh với GD thường trên cùng hình mất mát theo số lần cập nhật | Cùng điểm khởi tạo, cùng η; nêu số lần cập nhật để đạt cùng mức mất mát | 0,25 | Huấn | `src/optim_linear.py`; `results/figures, results/tables/4_*` | ☑ |
| B3.4 | Kiểm tra tính đúng: (a) gradient bằng sai phân hữu hạn trên mẫu con nhỏ; (b) so với nghiệm giải tích của bình phương tối thiểu có chính quy hóa | (a) sai số tương đối ≤ 10⁻⁶ (float64); (b) chỉ số trên tập kiểm định chênh ≤ 0,005 hoặc giải thích được nguyên nhân | 0,25 | Huấn | `src/optim_linear.py` (`finite_diff_check`, `ridge_closed_form`); `results/tables/4_*` | ☑ |
| B4.1 | Tự cài đặt PLA và Pocket; nêu quy ước: nhãn ±1, x̃ = (x, 1), w̃(0) = 0, mẫu y·g ≤ 0 là sai (kể cả g = 0), thứ tự duyệt, điều kiện dừng | Mã tự viết đúng quy ước | 0,25 | Việt | `src/perceptron.py` | ☐ |

### P3 — Lõi (đến 14/12/2026)
| Mã | Việc phải có | Điều kiện được điểm | Điểm | Người | Tệp kết quả / nơi nộp | ☐ |
|---|---|---|---|---|---|---|
| B2.1 | Lý thuyết ngắn gọn, ký hiệu thống nhất: GD/SGD/mini-batch/momentum; perceptron, hàm mất mát perceptron, PLA, Pocket; MLP, kích hoạt, mất mát, BP1–BP4; PCA, LDA, chọn đặc trưng; các chỉ số. Mỗi người viết khối của mình: GD → Huấn; perceptron, PCA, LDA, chọn đặc trưng → Việt; MLP, chỉ số → Phi | Bám tài liệu: chương 1 [2, tr. 158–173]; chương 2 [2, tr. 175–183]; chương 3 [1, tr. 115–146], [2, tr. 214–232]; chương 4 [1, tr. 88–99, 521–567]; tối ưu [3, chương 9]. Mỗi mục có trích dẫn; không chép nguyên văn quá 3 dòng liên tiếp | 0,5 | Huấn / Việt / Phi (theo khối) | Báo cáo Chương 2 | ☐ |
| B2.2 | ≥ 1 suy dẫn tự viết từng bước. Đã chọn: (d) nghiệm LDA hai lớp w ∝ S_W⁻¹(m1 − m0) | Đúng, đủ bước, ký hiệu khớp mã (`features.lda_two_class`) | 0,25 | Việt | Báo cáo Chương 2 hoặc 3 | ☐ |
| B3.3 | Thí nghiệm η: ≥ 4 giá trị theo thang log (ví dụ 10⁻³, 10⁻², 10⁻¹, 1), chỉ ra hội tụ chậm, dao động, phân kỳ; ảnh hưởng của z-score đến tốc độ hội tụ | Có hình và bảng; giải thích bằng độ cong (số điều kiện), liên hệ chương 1 và [3, chương 9] | 0,25 | Huấn | `src/optim_linear.py` (`run`); `results/figures/4_*_lr_sweep.png` (mẫu tên) | ☐ |
| B4.2 | Kiểm tra khả tách tuyến tính của train: LP khả thi [3, §8.6.1] với `scipy.optimize.linprog`, hoặc PLA không hội tụ sau số epoch đủ lớn | Kết luận có căn cứ định lượng (trạng thái LP hoặc số lỗi theo epoch) | 0,25 | Việt | `src/perceptron.py` (`check_separable_lp`); `results/tables/4_*` | ☐ |
| B4.3 | Số lỗi theo epoch của PLA và Pocket; ảnh hưởng của chuẩn hóa và thứ tự duyệt (≥ 5 hạt giống); kiểm chứng bất biến theo η khi w̃(0) = 0 | Hình số lỗi theo epoch; bảng trung bình ± độ lệch chuẩn | 0,25 | Việt | `src/perceptron.py` (`run`); `results/figures, results/tables/4_*` | ☐ |
| B5.1 | Tự cài đặt MLP bằng NumPy: forward dạng lô, backward theo δ(l) (BP1–BP4), cập nhật mini-batch; ≥ 2 hàm kích hoạt ẩn; tầng ra tuyến tính + MSE | Công thức khớp mã; mất mát giảm | 0,5 | Phi | `src/mlp.py` | ☐ |
| B5.2 | Kiểm tra gradient bằng sai phân hữu hạn cho toàn bộ tham số trên ≥ 2 kiến trúc, một kiến trúc ≥ 2 tầng ẩn | Sai số tương đối ≤ 10⁻⁶ (float64); bảng sai số theo từng ma trận trọng số | 0,25 | Phi | `src/mlp.py` (`grad_check`); `results/tables/5_*` | ☐ |
| B5.3 | Thực nghiệm kiến trúc và khởi tạo: ≥ 3 cấu hình rộng/sâu; khởi tạo 0/hằng số so với Xavier/He; ≥ 2 hàm kích hoạt ẩn | Bảng trên tập kiểm định; giải thích đối xứng khi khởi tạo hằng số, bão hòa và gradient biến mất (sigmoid nhiều tầng) | 0,5 | Phi | `src/mlp.py` (`run`); `results/tables/5_*` | ☐ |
| B5.4 | So sánh SGD mini-batch và momentum (tự cài đặt); L2 và dừng sớm (dropout khuyến khích); đường cong học train–val; chẩn đoán quá khớp/thiếu khớp | Siêu tham số chọn trên tập kiểm định (hoặc k-fold trên train), không chọn trên tập kiểm tra | 0,5 | Phi | `src/mlp.py` (`run`); `results/figures/5_*` | ☐ |
| B5.5 | Đối chứng thư viện: cùng kiến trúc và siêu tham số với scikit-learn `MLPRegressor` (hoặc PyTorch) | Chênh lệch chỉ số chính được giải thích (khởi tạo, bộ tối ưu, điều kiện dừng) | 0,25 | Phi | `src/mlp.py`; `results/tables/5_*` | ☐ |
| B6.1 | Phân tích đặc trưng gốc: thang đo; tiêu chí Fisher từng đặc trưng; ma trận tương quan và nhóm đặc trưng dư thừa | Bảng xếp hạng; nhận xét ≥ 3 đặc trưng mạnh/yếu bằng ý nghĩa nghiệp vụ | 0,25 | Việt | `src/features.py` (`fisher_score`); `results/tables/3_*` | ☐ |
| B6.2 | ≥ 5 đặc trưng mới có cơ sở nghiệp vụ (trễ ≥ 240 giờ, trung bình/độ lệch chuẩn trượt theo tuần, lịch, thời tiết: CDH, giờ × nhiệt độ); bảng: tên, công thức, ý nghĩa, Fisher trước và sau | Thống kê chỉ tính trên train; không dùng thông tin tương lai | 0,5 | Việt | `src/features.py`; `results/tables/3_*` | ☐ |
| B6.3 | PCA tự cài đặt (trị riêng hoặc SVD) đối chiếu `sklearn.decomposition.PCA`; biểu đồ phương sai giải thích và tích lũy; chọn k có lý do; sai số tái tạo; diễn giải ≥ 2 thành phần qua loadings | Chuẩn hóa trước PCA khi khác đơn vị (hoặc giải thích); trị riêng khớp thư viện đến 10⁻⁶ | 0,25 | Việt | `src/features.py` (`pca`); `results/figures/3_*` | ☐ |
| B6.4 | LDA tự cài đặt (S_W, S_B, bài toán trị riêng tổng quát) cho phân loại loại ngày (R4); chọn đặc trưng ≥ 2 họ: lọc (Fisher/tương quan), bọc (SFS), nhúng (L1) | Chọn đặc trưng bên trong vòng kiểm định hoặc chỉ trên train; liệt kê đặc trưng được giữ lại | 0,25 | Việt | `src/features.py` (`lda_two_class`, `lda_multiclass`); `results/tables/3_*` | ☐ |
| B7.1 | (a) Một bước GD theo lô cho hồi quy logistic trên 6 mẫu, w̃(0) = 0, η = 0,1, J = trung bình BCE không chính quy hóa: ŷ, J, ∇J, w̃(1), J sau cập nhật. (b) Một epoch PLA trên 6 mẫu, w̃(0) = 0: từng bước g, y·g, có cập nhật hay không, w̃ | Từng bước; sai khác với mã ≤ 10⁻⁴; 6 mẫu chọn đúng đoạn mã của đề (`hand_calc.select_six_samples`) | 0,25 | (a) Huấn; (b) Việt | `src/hand_calc_huan.py`, `src/hand_calc_viet.py`; Phụ lục A | ☐ |
| B7.2 | Một bước forward + backward mạng 2–2–1 (sigmoid, BCE) trên mẫu thứ nhất; khởi tạo W(1) hàng 1 = (0,2; −0,3), hàng 2 = (0,4; 0,1), b(1) = (0; 0), w(2) = (0,5; −0,6), b(2) = 0, η = 0,5; tính z(1), a(1), ŷ, J, δ(2), δ(1), gradient, tham số mới, J sau cập nhật | Như B7.1; thêm kiểm chứng ≥ 1 đạo hàm bằng sai phân hữu hạn | 0,25 | Phi | `src/hand_calc.py`; Phụ lục A | ☐ |
| B7.3 | PCA 6×2 (trung bình, hiệp phương sai chia n − 1, 2 trị riêng, 2 véc tơ riêng đơn vị với thành phần trị tuyệt đối lớn nhất dương, tỉ lệ phương sai, tọa độ chiếu mẫu 1) và LDA hai lớp (m+, m−, S_W, w ∝ S_W⁻¹(m+ − m−), ‖w‖ = 1, giá trị chiếu 6 mẫu) | Như B7.1; S_W suy biến thì cộng 10⁻³·I và nêu rõ | 0,25 | Việt | `src/hand_calc_viet.py`; Phụ lục A | ☐ |
| R1 | Bảng "đặc trưng – độ trễ nhỏ nhất – vì sao hợp lệ" (dùng `guards.lag_violations`); thí nghiệm có/không rò rỉ (dùng nhầm L(h−24) hoặc L(h−168)) cho thấy sai số "ảo" | Có bảng kiểm tra độ trễ; thí nghiệm trên tập kiểm định | 0,25 | Phi | `src/guards.py`, `src/evaluate.py`; `results/tables/6_*` | ☐ |
| R4 | PCA trên véc tơ 24 giờ chia cho trung bình ngày, diễn giải 2–3 thành phần (dạng đường 24 giờ); LDA 3 loại ngày (làm việc, cuối tuần, lễ) + ma trận nhầm lẫn; độ nhạy theo nhiệt độ từng giờ (MWh/°C) so với ≈ 74,8 MWh/°C trong [7] | Hình các thành phần và ma trận nhầm lẫn; nhận xét dựa trên số liệu | 0,25 | Việt | `src/features.py`; `results/figures/6_*` | ☐ |

### P4 — Đánh giá (đến 20/12/2026)
| Mã | Việc phải có | Điều kiện được điểm | Điểm | Người | Tệp kết quả / nơi nộp | ☐ |
|---|---|---|---|---|---|---|
| B4.4 | So sánh perceptron với mô hình tuyến tính (B3) và MLP (B5) trên cùng tập kiểm định; vẽ vùng quyết định trên 2 đặc trưng (hoặc 2 thành phần chính) của perceptron và MLP | Giải thích qua hàm mất mát (J_P không phạt mẫu đúng sát biên) và giới hạn biên tuyến tính (XOR) | 0,25 | Việt (cần mô hình MLP của Phi) | `src/perceptron.py` (`run`); `results/figures/4_*` | ☐ |
| B6.5 | So sánh cùng một mô hình (tuyến tính ở B3 và MLP) với (i) đặc trưng gốc, (ii) gốc + mới, (iii) k thành phần chính, (iv) sau chọn đặc trưng; nhận xét theo hiện tượng Hughes và đường cong học | Cùng cách chia, cùng chỉ số; có khoảng tin cậy hoặc độ lệch chuẩn | 0,25 | Việt (cần mô hình của Huấn và Phi) | `results/tables/3_*` | ☐ |
| R2 | So sánh với CND và mô hình cơ sở (trễ 336 h; trung bình các tuần thứ 2, 3, 4 trước): MAPE, RMSE, sai số đỉnh/đáy/năng lượng theo từng tuần kiểm tra và trung bình; chỉ số kỹ năng = 1 − MAPE_mô_hình/MAPE_cơ_sở; số tuần tốt hơn CND | Căn đúng thời điểm giữa dự báo CND và số liệu thực; mọi mô hình dùng cùng các tuần kiểm tra | 0,25 | Huấn | `src/cnd_compare.py`; `results/tables/6_*` | ☐ |
| R3 | Sai số theo giờ trong ngày; ngày làm việc/cuối tuần/lễ; giai đoạn (a) và (b); nhận diện thời điểm thay đổi cấu trúc; thử ≥ 1 cách thích nghi (cửa sổ trượt, tăng trọng số mẫu gần) | Bảng MAPE theo từng nhóm; giải thích bằng số liệu | 0,25 | Phi | `src/evaluate.py`; `results/tables/6_*` | ☐ |
| B9.1 | Chạy tập kiểm tra đúng một lần: `python run_all.py --final` (Phi chạy). Bảng mọi mô hình + mô hình cơ sở (trễ 336 h; trung bình tuần 2, 3, 4; CND); khoảng tin cậy 95% bootstrap ≥ 1.000 lần (hoặc trung bình ± độ lệch chuẩn nhiều seed); kết luận chênh lệch có ý nghĩa không; báo cáo riêng (a) 37 tuần và (b) 14 tuần | Không chọn lại mô hình sau khi xem tập kiểm tra | 0,25 | Phi | `src/evaluate.py`; `results/tables/6_*`; `results/.test_used` (khóa) | ☐ |

### P5 — Nộp (đến 25/12/2026; vấn đáp 30/12/2026)
| Mã | Việc phải có | Điều kiện được điểm | Điểm | Người | Tệp kết quả / nơi nộp | ☐ |
|---|---|---|---|---|---|---|
| B9.2 | Phân tích lỗi (≥ 10 mẫu sai, phân nhóm nguyên nhân); hạn chế; khuyến nghị triển khai và giám sát (trôi dữ liệu, cập nhật mô hình); trả lời đủ 4 câu hỏi nghiên cứu trong Kết luận | Dựa trên số liệu của nhóm | 0,25 | Phi (mọi người đóng góp) | Báo cáo Chương 6 và Kết luận | ☐ |
| B10.1 | Báo cáo đúng cấu trúc mục 5 và quy định 2.3; mã đúng cấu trúc Phụ lục 2; chạy lại bằng một lệnh, tái tạo đúng bảng/hình chính; bảng truy vết (Phụ lục D) | Giảng viên chạy lại ≤ 60 phút | 0,25 | Phi (chạy lại một lệnh); Huấn (cấu trúc báo cáo, Phụ lục D); mọi người đóng góp | `run_all.py`; README; Phụ lục D | ☐ |
| HS | Hồ sơ cuối theo 2.2: báo cáo .docx và .pdf tên `HMNC_BCCD_N18_De3`; mã nguồn (.zip hoặc GitHub riêng tư mời giảng viên); README (Python, thư viện, cách tải dữ liệu, ngày tải, kích thước/SHA-256, lệnh chạy lại); slide ≤ 15 trang; Phụ lục B (phân công, tỉ lệ đóng góp, chữ ký) và Phụ lục C (khai báo AI) nằm trong báo cáo | Đủ thành phần, nộp đúng hạn (muộn: −1,0 điểm/ngày) | (điều kiện chấm; tránh trừ) | Huấn ghép, Phi duyệt final (mọi người đóng góp) | Nơi nộp theo thông báo của giảng viên (UNKNOWN: hỏi Phi) | ☐ |

### Điểm khuyến khích 6.5 (tối đa 0,5; không bắt buộc)
| Việc | Điểm | Người | ☐ |
|---|---|---|---|
| Tự cài đặt Adam hoặc Nesterov và phân tích đúng ảnh hưởng so với momentum | 0,25 | Huấn | ☐ |
| Kiểm định ghép cặp giữa hai mô hình tốt nhất (bootstrap ghép cặp, McNemar hoặc DeLong) | 0,25 | Phi | ☐ |
| Tái lập một bảng hoặc hình trong bài báo gốc [7] và giải thích chênh lệch | 0,25 | Phi | ☐ |
| Ứng dụng minh họa (Streamlit/Gradio) + chỉ số trôi dữ liệu như PSI | 0,25 | Tùy chọn, Phi quyết | ☐ |

## Trừ điểm 6.4 — kiểm trước khi nộp
- ☐ Nộp hồ sơ cuối đúng hạn 25/12/2026 (muộn: −1,0 điểm mỗi ngày; quá 3 ngày Phần I = 0).
- ☐ Đã nộp báo cáo tiến độ đúng hạn 30/11/2026 (không nộp: −0,5).
- ☐ Phần thân 25–35 trang (ngoài: −0,5; ngoài 20–40 trang: −1,0).
- ☐ Không dùng tập kiểm tra để chọn mô hình, siêu tham số, ngưỡng, đặc trưng (vi phạm: −0,5 và kết quả liên quan không được tính điểm).
- ☐ Mọi hình/bảng có số, chú thích, nguồn và được nhắc trong văn bản; tài liệu tham khảo đủ và được trích dẫn (thiếu: −0,25 đến −0,5).
- ☐ Chạy lại được mọi kết quả từ mã nộp kèm (không: Phần I tối đa 3,0).

## Tự kiểm Phụ lục 5 (chỉnh cho Đề 3)
- ☐ Dùng đúng bộ dữ liệu của đề; README ghi ngày tải và kích thước hoặc SHA-256.
- ☐ SEED = 2044 (2026 + 18) dùng ở mọi bước ngẫu nhiên.
- ☐ Tập kiểm tra chỉ dùng một lần ở cuối; không tuần nào nằm ở hai tập.
- ☐ Chuẩn hóa, mã hóa, PCA, LDA, chọn đặc trưng, ngưỡng phân vị 90% chỉ khớp trên tập huấn luyện.
- ☐ Đủ phần tự cài đặt: GD, SGD, mini-batch, momentum; PLA, Pocket; MLP (forward, backward, kiểm tra gradient); PCA; LDA.
- ☐ Kiểm tra gradient sai số tương đối ≤ 10⁻⁶ cho mô hình tuyến tính và cho MLP.
- ☐ Đủ thí nghiệm: tốc độ học, chuẩn hóa, kiến trúc, khởi tạo, bộ tối ưu, chính quy hóa.
- ☐ ≥ 5 đặc trưng mới, kèm bảng công thức – ý nghĩa – Fisher.
- ☐ Bảng tổng hợp trên tập kiểm tra với mô hình cơ sở và khoảng tin cậy.
- ☐ Đủ R1–R4 và trả lời đủ bốn câu hỏi nghiên cứu.
- ☐ Phụ lục A đủ ba phần tính tay, khớp mã đến 10⁻⁴.
- ☐ Thân 25–35 trang; hình, bảng, công thức đánh số; trích dẫn [1], [2], [3], [7], [8].
- ☐ Phụ lục D có bảng truy vết số liệu đầy đủ.
- ☐ Đã chạy thử toàn bộ mã trên máy khác hoặc phiên Colab mới theo README.
- ☐ Bảng phân công có chữ ký; khai báo AI đầy đủ.
- ☐ Tên tệp đúng quy định (`HMNC_BCCD_N18_De3`); nộp đúng hạn.

## Câu hỏi nghiên cứu (4 câu, trả lời trong Kết luận)
- ☐ (1) Mô hình của nhóm có tốt hơn dự báo của CND trong giai đoạn bình thường không? Trong giai đoạn phong tỏa thì sao?
- ☐ (2) Đặc trưng nào quan trọng nhất (trễ phụ tải, giờ, nhiệt độ, lễ), căn cứ kết quả chọn đặc trưng và phân tích độ nhạy?
- ☐ (3) Chuẩn hóa và momentum ảnh hưởng thế nào đến tốc độ hội tụ của hồi quy tuyến tính trên dữ liệu này?
- ☐ (4) MLP có lợi thế so với hồi quy tuyến tính ở những giờ hoặc loại ngày nào?

## Giới hạn
Chạy lại ≤ 60 phút · thân 25–35 trang (phụ lục ≤ 15 trang) · slide ≤ 15 trang · mỗi đoạn mã trong thân ≤ 15 dòng, tổng mã trong thân ≤ 3 trang · trình bày tối đa 12 phút.
