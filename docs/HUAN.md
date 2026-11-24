# HUAN — nhiệm vụ cá nhân (Đỗ Minh Huấn)

Đọc theo thứ tự: `TEAM.md` → file này → `tasks/README.md` + file task được giao → `docs/CONVENTIONS.md` → `docs/CHECKLIST.md` → `docs/DE3.md`. Thiếu thông số hoặc chỗ mơ hồ: ghi "UNKNOWN: hỏi Phi" vào task, không tự quyết.

## a. Bạn là ai
| Mục | Giá trị |
|---|---|
| Tên | Đỗ Minh Huấn |
| Vai trò | Thành viên: EDA, GD/SGD/momentum, so sánh với CND |
| GitHub | `minhhuan15082k5-sudo` |
| Nhánh duy nhất | `huan-eda-gd` |
| `git config user.name` | `Do Minh Huan` |

## b. Mục tiêu điểm của bạn
| Mã | Nội dung | Điểm |
|---|---|---|
| B1.1 | Phát biểu bài toán nghiệp vụ, chỉ số chính | 0,25 |
| B1.2 | Mô tả dữ liệu + từ điển dữ liệu | 0,25 |
| B1.3 | EDA (≥ 4 hình có nhận xét định lượng) | 0,25 |
| B2.1 (phần GD) | Lý thuyết GD, SGD, mini-batch, momentum (tổng B2.1 = 0,5, chia theo khối) | 0,5 chung |
| B3.1 | GD theo lô, SGD, mini-batch | 0,5 |
| B3.2 | Momentum, so sánh với GD | 0,25 |
| B3.3 | Thí nghiệm tốc độ học, z-score | 0,25 |
| B3.4 | Kiểm tra gradient, đối chiếu nghiệm giải tích | 0,25 |
| B7.1(a) | Tính tay một bước GD logistic (chung B7.1 = 0,25 với Việt) | 0,25 chung |
| R2 | So sánh với CND và mô hình cơ sở | 0,25 |
| TĐ, HS, B10.1 (phần báo cáo) | Soạn báo cáo tiến độ, ghép hồ sơ cuối, bảng truy vết (Phụ lục D), kiểm cấu trúc báo cáo; Phi duyệt final | điều kiện chấm; B10.1: 0,25 chung với Phi |
| 6.5 | Tự cài đặt Adam hoặc Nesterov + phân tích so với momentum | 0,25 |

## c. File được sửa / không được sửa (TEAM.md mục 3)
- Được sửa: `src/optim_linear.py`, `src/hand_calc_huan.py`, `src/cnd_compare.py`, `notebooks/huan_*`, `docs/DATA_DICTIONARY.md`.
- Ai cũng được: file task của mình, `docs/trace_huan.md`, `docs/ai_usage_log.md` (chỉ thêm dòng), `results/figures/` và `results/tables/` (chỉ tệp do mã của bạn sinh, tên theo CONVENTIONS mục 5), `tests/` của khối mình.
- KHÔNG sửa: `src/config.py`, `src/data_prep.py`, `src/mlp.py`, `src/evaluate.py`, `src/hand_calc.py`, `run_all.py` (Phi); `src/perceptron.py`, `src/features.py`, `src/hand_calc_viet.py` (Việt); `docs/CONVENTIONS.md`, `docs/CHECKLIST.md`. Cần đổi → ghi vào task, nhắn chủ file.

## d. Lộ trình theo phase
Task chi tiết: `tasks/README.md`. Task của bạn: T003 (GD), T004 (từ điển dữ liệu), T005 (EDA).
Hạn ở bảng dưới là mốc tham khảo; nếu lệch với `due:` trong file task thì **theo file task**.
| Hạn nội bộ | Việc | Mã | Task |
|---|---|---|---|
| 22/11 (P1) | Từ điển dữ liệu đủ 12 biến thời tiết + lịch + `nat_demand`; nháp B1.1 (ai dùng, quyết định gì, chi phí lỗi, vì sao MAPE) | B1.1, B1.2 | T004 |
| 27/11 | EDA ≥ 4 hình có nhận xét định lượng (cần `data_prep` của Phi); ghi vấn đề dữ liệu và cách xử lý | B1.3 | T005 |
| 28/11 | `gd`, `sgd`, `minibatch_gd`, `momentum_gd`, kiểm tra gradient; kết quả ban đầu Huấn tự đưa vào báo cáo tiến độ T008 (nộp 30/11) | B3.1, B3.2, B3.4 | T003 |
| 07/12 (P3) | Quét η (≥ 4 giá trị theo log), z-score vs không chuẩn hóa; phần lý thuyết GD cho Chương 2 | B3.3, B2.1 | T003 |
| 10/12 | `hand_calc_huan.py`: B7.1(a) | B7.1(a) | (task do Phi giao) |
| 18/12 (P4) | `cnd_compare.py`: R2 (cần kết luận căn thời gian CND của Phi, T002) | R2 | (task do Phi giao) |
| 27/11 | Soạn báo cáo tiến độ 2–3 trang từ phần của ba người (mỗi người tự viết phần mình) | TĐ | T008 |
| 20/12 | Bảng truy vết (Phụ lục D) và kiểm cấu trúc báo cáo theo mục 5 của đề | B10.1 | T009 |
| 22/12 | Ghép hồ sơ cuối: báo cáo .docx/.pdf, Phụ lục B, C, D, slide ≤ 15 trang, README | HS | T010 |
| tùy chọn | Nesterov/Adam | 6.5 | |

## e. Cách làm từng khối của bạn
1. **Giao diện** (`src/optim_linear.py`, giữ nguyên tên và chữ ký): `mse_l2_loss(w, X, y, lam)`, `mse_l2_grad`, `gd(X, y, lam, eta, n_iter, w0=None)`, `sgd(X, y, lam, eta, n_epochs, seed)`, `minibatch_gd(..., batch_size, seed)`, `momentum_gd(X, y, lam, eta, beta, n_iter, w0=None)`, `ridge_closed_form`, `finite_diff_check`. Mỗi hàm lặp trả `(w, loss_history)`.
2. **Quy ước**: `X̃ = [X, 1]` (cột 1 ở cuối), `w` có d+1 phần tử; `J = 1/(2n)·‖X̃w − y‖² + (λ/2)·‖w[:-1]‖²` (không phạt hệ số tự do); `grad = 1/n·X̃ᵀ(X̃w − y) + λ·[w[:-1], 0]`. Float64.
3. **Thứ tự làm**: (i) viết loss và grad; (ii) chạy `finite_diff_check` trên mẫu con nhỏ; (iii) thử thuật toán trên dữ liệu tổng hợp trong `tests/test_interfaces.py` (`test_b3_*`: grad khớp sai phân, nghiệm đóng là điểm dừng, GD hội tụ về nghiệm bình phương tối thiểu và về nghiệm đóng có L2) trước khi dùng dữ liệu thật; (iv) mới chạy dữ liệu thật.
4. **Dữ liệu thật**: z-score khớp trên train, áp cho val bằng cùng tham số; chỉ báo cáo trên train/val (tập kiểm tra do Phi mở). Hạt giống từ `config.get_seed()`; không viết số thẳng vào code.
5. **B3.2/B3.3**: cùng điểm khởi tạo và cùng η khi so momentum với GD; nêu số lần cập nhật để đạt cùng mức mất mát. Quét η theo thang log (ví dụ 10⁻³, 10⁻², 10⁻¹, 1); chỉ ra chậm, dao động, phân kỳ; giải thích bằng độ cong (số điều kiện) của Hessian XᵀX/n; ghi rõ cách đặt η cho từng trường hợp (z-score và không z-score).
6. **B3.4(b)**: so với `ridge_closed_form` trên val; chênh ≤ 0,005 hoặc giải thích nguyên nhân.
7. **R2** (`cnd_compare.py`): căn dự báo CND với phụ tải thực; chờ Phi kết luận nhãn thời gian (UNKNOWN trong CONVENTIONS mục 1). Dùng đúng các tuần kiểm tra chung; báo cáo riêng (a) 37 tuần và (b) 14 tuần. Chỉ số theo CONVENTIONS mục 4.
8. **Truy vết**: mỗi hình/bảng thêm một dòng vào `docs/trace_huan.md` (số hình/bảng | tệp | hàm hoặc ô notebook | mã task); hình `results/figures/4_<số>_<mô_tả>.png`; notebook `notebooks/huan_*.ipynb`, chỉ gọi hàm trong `src/`, xóa output trước khi commit.

## f. Dùng AI cho phần của bạn
| Được hỏi AI | Không được để AI làm |
|---|---|
| Khái niệm GD/SGD/momentum, số điều kiện, hội tụ | Nộp mã GD/SGD/momentum bạn chưa hiểu (AI được viết; bạn giải thích được từng dòng, Phi review) |
| Cách dùng `numpy`, `pandas`, `matplotlib`; sửa lỗi cú pháp, giải thích traceback | Viết thay tính tay B7.1(a) hoặc sinh số cho Phụ lục A |
| Gợi ý cách vẽ hình EDA, cách mô tả dữ liệu | Sinh nguyên đoạn B1.1, từ điển dữ liệu, hoặc phần lý thuyết |
| Sửa chính tả, diễn đạt câu chữ | Tạo số liệu, bảng, hình không do mã nhóm chạy; thêm tài liệu tham khảo chưa đọc |
| Nhờ đặt câu hỏi ôn vấn đáp | Chọn η/siêu tham số bằng cách nhìn tập kiểm tra |

Cuối mỗi task (trước `review`), mỗi loại việc AI đã dùng ghi MỘT dòng vào `docs/ai_usage_log.md` (gộp mọi phiên của task; 7 cột và 6 loại T/G/M/B/D/R xem đầu file; việc M ghi tên hàm). Phần GD là phần bắt buộc tự cài đặt (đề mục 2.4): AI được viết mã, nhưng bạn phải giải thích được từng dòng, Phi review trước khi merge, nhật ký ghi rõ (khai ở Phụ lục C).

## g. Chuẩn bị vấn đáp
**II.2 — phải giải thích được**: công thức J và grad có L2 (vì sao không phạt hệ số tự do); khác nhau giữa GD theo lô, SGD, mini-batch; công thức cập nhật momentum; vì sao η lớn gây phân kỳ và liên hệ độ cong; tác dụng của z-score lên tốc độ hội tụ; kiểm tra gradient bằng sai phân hữu hạn; nghiệm đóng của hồi quy chính quy hóa; ý nghĩa các biến trong từ điển dữ liệu; chỉ số kỹ năng so với CND.
**II.3 — câu hỏi mẫu (không có đáp án ở đây)**:
1. Tính lại một bước GD theo lô cho 6 mẫu ở Phụ lục A với η khác.
2. Tăng η gấp 10 thì đường mất mát thay đổi ra sao? Bỏ z-score thì sao?
3. Với β = 0 momentum trở thành gì? Với β gần 1 thì sao?
4. Vì sao SGD có đường mất mát nhiễu hơn GD theo lô?
5. Tăng λ thì nghiệm `ridge_closed_form` thay đổi thế nào?
6. Đọc một giá trị trong bảng so sánh với CND và nói ý nghĩa của chỉ số kỹ năng.
7. Hình EDA nào cho thấy vấn đề của dữ liệu và bạn xử lý ra sao?
8. Vì sao MAPE thay đổi nhiều giữa giai đoạn (a) và (b)?
**II.4 — phần của hai người còn lại**:
1. (Phi) Vì sao dùng độ trễ ≥ 240 giờ? Chia dữ liệu theo tuần thế nào?
2. (Phi) Kiểm tra gradient của MLP khác của hồi quy tuyến tính ở điểm nào?
3. (Việt) Mẫu nào bị coi là sai trong PLA? Pocket khác PLA ra sao?
4. (Việt) PCA chọn k thành phần dựa trên tiêu chí nào?

## h. Lỗi hay gặp ở khối của bạn
- Rò rỉ chuẩn hóa: tính mean/std trên cả train+val (hoặc cả bộ dữ liệu) thay vì chỉ train; áp lại tham số train cho val.
- Quên cột 1 (hệ số tự do) trong `X̃`, hoặc đặt cột 1 ở đầu thay vì cuối (sai quy ước, lệch chỉ số khi áp L2).
- Phạt L2 cả hệ số tự do; thiếu hệ số 1/n hoặc 1/(2n) làm grad không khớp sai phân hữu hạn.
- SGD/mini-batch không xáo thứ tự bằng `seed` từ `config.get_seed()`; kết quả không tái lập.
- Chọn η bằng cách nhìn val rồi báo cáo như phát hiện độc lập; so sánh momentum và GD khác điểm khởi tạo hoặc khác η.
- Đặt η quá lớn nên loss thành `inf`/`nan` mà không nhận ra là phân kỳ; quên dừng sớm khi `nan`.
- Kiểm tra gradient bằng eps quá nhỏ hoặc không dùng float64 nên vượt ngưỡng 10⁻⁶.
- Căn CND lệch 1 giờ (xem UNKNOWN nhãn thời gian); tính MAPE trên giờ tải thấp bất thường mà không đánh dấu.
