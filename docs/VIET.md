# VIET — nhiệm vụ cá nhân (Nguyễn Serov Trọng Việt)

Đọc theo thứ tự: `TEAM.md` → file này → `tasks/README.md` + file task được giao → `docs/CONVENTIONS.md` → `docs/CHECKLIST.md` → `docs/DE3.md`. Thiếu thông số hoặc chỗ mơ hồ: ghi "UNKNOWN: hỏi Phi" vào task, không tự quyết.

## a. Bạn là ai
| Mục | Giá trị |
|---|---|
| Tên | Nguyễn Serov Trọng Việt |
| Vai trò | Thành viên: perceptron, đặc trưng, PCA/LDA |
| GitHub | `viet29oct` |
| Nhánh duy nhất | `viet-perceptron-features` |
| `git config user.name` | `Nguyen Serov Trong Viet` |

## b. Mục tiêu điểm của bạn
| Mã | Nội dung | Điểm |
|---|---|---|
| B2.1 (phần của bạn) | Lý thuyết perceptron/PLA/Pocket, PCA, LDA, chọn đặc trưng (tổng B2.1 = 0,5, chia theo khối) | 0,5 chung |
| B2.2 | Suy dẫn tự viết: (d) nghiệm LDA hai lớp w ∝ S_W⁻¹(m1 − m0) | 0,25 |
| B4.1 | PLA và Pocket tự cài đặt | 0,25 |
| B4.2 | Kiểm tra khả tách tuyến tính | 0,25 |
| B4.3 | Thực nghiệm lỗi theo epoch, ≥ 5 hạt giống | 0,25 |
| B4.4 | So sánh perceptron với tuyến tính (B3) và MLP (B5) | 0,25 |
| B6.1 | Phân tích đặc trưng gốc, Fisher | 0,25 |
| B6.2 | ≥ 5 đặc trưng mới | 0,5 |
| B6.3 | PCA tự cài đặt | 0,25 |
| B6.4 | LDA tự cài đặt + chọn đặc trưng ≥ 2 họ | 0,25 |
| B6.5 | Bảng so sánh đặc trưng (cần mô hình của Huấn và Phi) | 0,25 |
| B7.1(b) | Tính tay một epoch PLA (chung B7.1 = 0,25 với Huấn) | 0,25 chung |
| B7.3 | Tính tay PCA 6×2 và LDA hai lớp | 0,25 |
| R4 | PCA đồ thị ngày, LDA 3 loại ngày, độ nhạy nhiệt độ | 0,25 |

## c. File được sửa / không được sửa (TEAM.md mục 3)
- Được sửa: `src/perceptron.py`, `src/features.py`, `src/hand_calc_viet.py`, `notebooks/viet_*`.
- Ai cũng được: file task của mình, `docs/trace_viet.md`, `docs/ai_usage_log.md` (chỉ thêm dòng), `results/figures/` và `results/tables/` (chỉ tệp do mã của bạn sinh, tên theo CONVENTIONS mục 5), `tests/` của khối mình.
- KHÔNG sửa: `src/config.py`, `src/data_prep.py`, `src/mlp.py`, `src/evaluate.py`, `src/hand_calc.py`, `run_all.py` (Phi); `src/optim_linear.py`, `src/hand_calc_huan.py`, `src/cnd_compare.py`, `docs/DATA_DICTIONARY.md` (Huấn); `docs/CONVENTIONS.md`, `docs/CHECKLIST.md`. Cần đổi → ghi vào task, nhắn chủ file.

## d. Lộ trình theo phase
Task chi tiết: `tasks/README.md`. Task của bạn: T006 (PLA/Pocket), T007 (Fisher + PCA).
Hạn ở bảng dưới là mốc tham khảo; nếu lệch với `due:` trong file task thì **theo file task**.
| Hạn nội bộ | Việc | Mã | Task |
|---|---|---|---|
| 22/11 (P1) | Đọc [2, tr. 175–183] và đặt nhãn ±1 cho bài toán "giờ cao điểm" khi Phi xong `peak_label`; thử PLA trên dữ liệu tổng hợp | B4.1 | T006 |
| 28/11 | `pla`, `pocket`, `count_errors` chạy đúng; lỗi theo epoch ban đầu để Phi đưa vào báo cáo tiến độ (nộp 30/11) | B4.1 | T006 |
| 05/12 (P3) | `fisher_score` và bảng xếp hạng đặc trưng gốc; ≥ 5 đặc trưng mới với trễ ≥ 240 giờ | B6.1, B6.2 | T007 |
| 09/12 | `pca` + đối chiếu sklearn; `check_separable_lp`; thực nghiệm ≥ 5 hạt giống | B6.3, B4.2, B4.3 | T006, T007 |
| 12/12 | `lda_two_class`, `lda_multiclass`, chọn đặc trưng ≥ 2 họ; R4; suy dẫn B2.2(d); `hand_calc_viet.py` (B7.1(b), B7.3) | B6.4, R4, B2.2, B7 | (task do Phi giao) |
| 19/12 (P4) | So sánh perceptron với tuyến tính và MLP (B4.4); bảng 4 cấu hình đặc trưng (B6.5) khi Huấn và Phi đã có mô hình | B4.4, B6.5 | (task do Phi giao) |

## e. Cách làm từng khối của bạn
1. **Perceptron** (`src/perceptron.py`, giữ nguyên chữ ký): `count_errors(w, X, y)`, `pla(X, y, max_epochs=100, shuffle=False, seed=0) -> (w_last, errors_per_epoch)`, `pocket(...) -> (w_best, errors_per_epoch)`, `check_separable_lp(X, y)`. Quy ước bắt buộc nêu trong báo cáo: nhãn ±1; `x̃ = (x, 1)`; `w̃(0) = 0`; mẫu có `y·g ≤ 0` là sai (kể cả g = 0); nêu thứ tự duyệt và điều kiện dừng.
2. **Thử trước trên dữ liệu tổng hợp**: chạy các hàm trên tập khả tách trong `tests/test_interfaces.py` (`test_b4_*`: PLA về 0 lỗi; Pocket không tệ hơn nghiệm cuối của PLA) trước khi dùng dữ liệu thật.
3. **Khả tách (B4.2)**: lập bài toán LP khả thi theo [3, §8.6.1] và gọi `scipy.optimize.linprog`; kết luận dựa vào trạng thái nghiệm hoặc số lỗi theo epoch.
4. **Thực nghiệm (B4.3)**: ≥ 5 hạt giống từ `config.get_seed()` (không viết số cứng), báo trung bình ± độ lệch chuẩn; so có/không z-score; kiểm chứng bất biến theo η khi `w̃(0) = 0`. Nhãn "giờ cao điểm": ngưỡng phân vị 90% của train (do `data_prep.peak_label`, Phi).
5. **Đặc trưng** (`src/features.py`): giao diện `fisher_score(x, y)`, `pca(X, k) -> dict(mean, components[k, d], eigvals[k], explained_ratio[k])` (hiệp phương sai chia n − 1), `lda_two_class(X, y) -> w` (chuẩn hóa ‖w‖ = 1), `lda_multiclass(X, y, k)`. Đặc trưng trễ ≥ `guards.min_safe_lag()` = 240 giờ; mọi thống kê chỉ tính trên train.
6. **PCA/LDA**: chạy trên dữ liệu tổng hợp trong `tests/test_interfaces.py` (`test_b6_*`: trị riêng khớp sklearn; hướng LDA tỉ lệ với S_W⁻¹(m1 − m0)) trước khi dùng dữ liệu thật; chuẩn hóa trước PCA khi khác đơn vị. R4: PCA trên véc tơ 24 giờ chia cho trung bình ngày; LDA 3 loại ngày + ma trận nhầm lẫn; độ nhạy theo nhiệt độ từng giờ (MWh/°C) so với giá trị nêu trong [7] (tra [7], không tự đặt số).
7. **Chọn đặc trưng**: ≥ 2 họ (lọc/bọc/nhúng); thực hiện bên trong vòng kiểm định hoặc chỉ trên train; liệt kê đặc trưng giữ lại.
8. **Tính tay** (`hand_calc_viet.py`): 6 mẫu lấy từ `hand_calc.select_six_samples` (đúng đoạn mã của đề), z-score theo train, làm tròn 4 chữ số; mã in ra khớp tính tay ≤ 10⁻⁴; PCA 6×2 chia n − 1, dấu véc tơ riêng: thành phần có trị tuyệt đối lớn nhất dương; LDA ‖w‖ = 1, S_W suy biến thì cộng 10⁻³·I và nêu rõ.
9. **Truy vết**: mỗi hình/bảng thêm một dòng vào `docs/trace_viet.md` (số hình/bảng | tệp | hàm hoặc ô notebook | mã task); hình `results/figures/3_<số>_*.png` hoặc `4_<số>_*.png` tùy chương; notebook `notebooks/viet_*.ipynb`, xóa output trước khi commit.

## f. Dùng AI cho phần của bạn
| Được hỏi AI | Không được để AI làm |
|---|---|
| Khái niệm PLA, Pocket, Fisher, PCA, LDA, hiện tượng Hughes | Nộp mã PLA/Pocket/PCA/LDA bạn chưa hiểu (AI được viết; bạn giải thích được từng dòng, Phi review) |
| Cách dùng `scipy.optimize.linprog`, `numpy.linalg.eigh`, `sklearn.decomposition.PCA` (để đối chứng) | Viết thay suy dẫn B2.2(d) hoặc phần tính tay B7.1(b), B7.3 |
| Tìm lỗi cú pháp, giải thích traceback, cách vẽ hình | Sinh nguyên đoạn báo cáo; sinh số liệu, bảng, hình không do mã nhóm chạy |
| Sửa chính tả, diễn đạt câu chữ | Thêm tài liệu tham khảo chưa đọc; tự đặt hệ số từ [7] |
| Nhờ đặt câu hỏi ôn vấn đáp | Chọn đặc trưng hoặc ngưỡng bằng cách nhìn tập kiểm tra |

Cuối mỗi task (trước `review`), mỗi loại việc AI đã dùng ghi MỘT dòng vào `docs/ai_usage_log.md` (gộp mọi phiên của task; 7 cột và 6 loại T/G/M/B/D/R xem đầu file; việc M ghi tên hàm). PLA/Pocket, PCA, LDA là phần bắt buộc tự cài đặt (đề mục 2.4): AI được viết mã, nhưng bạn phải giải thích được từng dòng, Phi review trước khi merge, nhật ký ghi rõ (khai ở Phụ lục C).

## g. Chuẩn bị vấn đáp
**II.2 — phải giải thích được**: hàm mất mát perceptron J_P và vì sao không phạt mẫu đúng sát biên; PLA và Pocket khác nhau thế nào; quy ước y·g ≤ 0; vì sao w̃(0) = 0 thì kết quả bất biến theo η; bài toán LP kiểm tra khả tách; tiêu chí Fisher; PCA qua trị riêng/SVD, phương sai giải thích, loadings, sai số tái tạo; LDA (S_W, S_B), vì sao w ∝ S_W⁻¹(m1 − m0); ba họ chọn đặc trưng; hiện tượng Hughes.
**II.3 — câu hỏi mẫu (không có đáp án ở đây)**:
1. Thực hiện lại một bước PLA ở Phụ lục A với mẫu khác; mẫu có g = 0 xử lý thế nào?
2. Dữ liệu không khả tách thì PLA làm gì? Pocket trả về gì?
3. Nếu bỏ z-score, số lỗi theo epoch thay đổi ra sao?
4. Tăng k thành phần chính thì phương sai giải thích và sai số tái tạo thay đổi thế nào?
5. Đọc một ô của ma trận nhầm lẫn LDA 3 loại ngày và nêu loại ngày hay bị nhầm.
6. Đặc trưng L(h−168) hợp lệ hay không? Vì sao đặc trưng nào bạn đã tạo đều ≥ 240 giờ?
7. Vì sao PCA cần chuẩn hóa khi 12 biến thời tiết khác đơn vị?
8. Chọn đặc trưng ở vòng nào để tránh rò rỉ?
**II.4 — phần của hai người còn lại**:
1. (Huấn) Momentum cập nhật thế nào; η quá lớn thì sao?
2. (Huấn) Hồi quy chính quy hóa có nghiệm đóng thế nào?
3. (Phi) Chia 209/26/37/14 tuần dựa vào đâu; vì sao không xáo trộn?
4. (Phi) BP1–BP4 dùng để làm gì; kiểm tra gradient ra sao?

## h. Lỗi hay gặp ở khối của bạn
- Rò rỉ: tính phân vị 90%, mean/std, Fisher hoặc chọn đặc trưng (SFS, L1) trên cả bộ dữ liệu thay vì train/val.
- Quy ước sai dấu: coi y·g < 0 là sai (bỏ sót g = 0); khởi tạo `w̃(0)` khác 0 nên mất tính bất biến theo η.
- Nhầm nhãn {0, 1} và ±1 giữa hồi quy logistic và PLA (đổi bằng `(y+1)/2`).
- Điều kiện dừng PLA không rõ; số epoch quá nhỏ rồi kết luận "không khả tách"; bỏ qua kết quả LP.
- PCA: quên trừ trung bình; chia n thay vì n − 1 (lệch trị riêng so với sklearn); không chuẩn hóa 12 biến khác đơn vị; dấu véc tơ riêng không theo quy ước B7.3.
- LDA: S_W suy biến (đặc trưng cộng tuyến) mà không xử lý; quên chuẩn hóa ‖w‖ = 1; nhầm w ∝ S_W⁻¹(m+ − m−).
- Đặc trưng trễ L(h−24)/L(h−168) lọt vào mô hình (< 240 giờ), hoặc thống kê trượt dùng dữ liệu sau Thứ Ba của tuần dự báo.
- Hạt giống cố định trong code thay vì lấy từ `config.get_seed()`; chỉ chạy 1 hạt giống nhưng báo trung bình ± độ lệch chuẩn.
