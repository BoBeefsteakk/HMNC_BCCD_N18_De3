# PHI — nhiệm vụ cá nhân (Nguyễn Bảo Phi, trưởng nhóm)

Đọc theo thứ tự: `TEAM.md` → file này → `tasks/README.md` → `docs/CONVENTIONS.md` → `docs/CHECKLIST.md` → `docs/DE3.md`. Chỗ nào chưa rõ: ghi "UNKNOWN: hỏi Phi" vào task, không tự quyết.

## a. Bạn là ai
| Mục | Giá trị |
|---|---|
| Tên | Nguyễn Bảo Phi |
| Vai trò | Trưởng nhóm: giao task, review, merge; dữ liệu, MLP, đánh giá |
| GitHub | `BoBeefsteakk` |
| Nhánh duy nhất | `phi-lead-data-mlp` (`main` chỉ nhận PR, chỉ Phi merge) |
| `git config user.name` | `Nguyen Bao Phi` |

## b. Mục tiêu điểm của bạn
| Mã | Nội dung | Điểm |
|---|---|---|
| B1.4 | Tiền xử lý và chia dữ liệu 209/26/37/14 tuần | 0,25 |
| B2.1 (phần của bạn) | Lý thuyết MLP/BP1–BP4 và các chỉ số (tổng B2.1 = 0,5, ba người chia theo khối) | 0,5 chung |
| B5.1–B5.5 | MLP, kiểm tra gradient, kiến trúc/khởi tạo, tối ưu/chính quy hóa, đối chứng thư viện | 0,5 + 0,25 + 0,5 + 0,5 + 0,25 |
| B7.2 | Tính tay mạng 2–2–1 | 0,25 |
| R1 | Giao thức dự báo không rò rỉ | 0,25 |
| R3 | Phân tích sai số theo bối cảnh | 0,25 |
| B9.1, B9.2 | Đánh giá tổng hợp trên tập kiểm tra; phân tích lỗi, kết luận | 0,25 + 0,25 |
| B10.1 | Hình thức, mã nguồn, tái lập | 0,25 |
| 6.5 | Kiểm định ghép cặp; tái lập bảng/hình của [7]; ứng dụng + PSI (tùy chọn, bạn quyết) | 0,25 mỗi mục |
| Lãnh đạo | Giữ `config`, `CONVENTIONS`, `CHECKLIST`; báo cáo tiến độ; hồ sơ nộp | — |

## c. File được sửa / không được sửa (TEAM.md mục 3)
- Được sửa: `src/config.py`, `src/data_prep.py`, `src/mlp.py`, `src/evaluate.py`, `src/hand_calc.py`, `run_all.py`, `docs/` (trừ file task và `ai_usage_log.md`), `tasks/` (tạo task), `.github/`, `.claude/`, `prompts/`, `scripts/`, `TEAM.md`, `AGENTS.md`.
- Ai cũng được: file task của mình, `docs/trace_phi.md`, `docs/ai_usage_log.md` (chỉ thêm dòng), `results/figures|tables/` (tệp do mã của bạn sinh), `tests/` của khối mình.
- Không sửa: `src/optim_linear.py`, `src/hand_calc_huan.py`, `src/cnd_compare.py`, `notebooks/huan_*`, `docs/DATA_DICTIONARY.md` (Huấn); `src/perceptron.py`, `src/features.py`, `src/hand_calc_viet.py`, `notebooks/viet_*` (Việt). Cần đổi → ghi vào task, nhắn chủ file.

## d. Lộ trình theo phase
Task chi tiết: `tasks/README.md`. T001, T002 (dữ liệu/CND, P1) là của bạn.
Hạn ở bảng dưới là mốc tham khảo; nếu lệch với `due:` trong file task thì **theo file task**.
| Hạn nội bộ | Việc | Mã | Ghi chú |
|---|---|---|---|
| 20/11 | T001–T002: `download_data.py`, `load_raw`, `split_weeks`, `peak_label`, kiểm tra nhãn thời gian CND (UNKNOWN trong CONVENTIONS mục 1); báo kết quả để Huấn bắt đầu EDA/R2 | B1.4 | Mở khóa cho Huấn và Việt |
| 22/11 | Hết P1: bảng kích thước tập và tỉ lệ nhãn; README ghi ngày tải, kích thước/SHA-256 | B1.4 | |
| 28/11 | Gộp phần của từng người thành báo cáo tiến độ 2–3 trang | TĐ | Hạn nộp 30/11 |
| 07/12 | MLP: forward/backward/`grad_check`; thử trên dữ liệu tổng hợp | B5.1, B5.2 | |
| 12/12 | Thí nghiệm kiến trúc, khởi tạo, tối ưu, chính quy hóa, đối chứng sklearn; `hand_calc.py`; R1 | B5.3–B5.5, B7.2, R1 | Hạn P3 14/12 |
| 18/12 | Review hết PR; chạy `python run_all.py --final` ĐÚNG MỘT LẦN sau khi chốt mô hình; B9.1, R3 | B9.1, R3 | Hạn P4 20/12 |
| 24/12 | Hợp nhất báo cáo (Google Docs), Phụ lục B, C, D, slide, README; tự kiểm Phụ lục 5 | B9.2, B10.1 | Hạn nộp 25/12 |

## e. Cách làm từng khối của bạn
1. **Dữ liệu (`data_prep.py`)**: làm theo docstring (`load_raw`, `week_starts`, `split_weeks`, `peak_label`, `align_cnd`). Assert số tuần = `config.EXPECTED_WEEKS`. Ngưỡng "giờ cao điểm" = phân vị `config.PEAK_QUANTILE` tính trên train. Đánh dấu giờ tải < 50% trung vị và nêu cách xử lý. Mọi `rng` từ `config.get_seed()`.
2. **MLP (`mlp.py`)**: giữ đúng giao diện `MLP(layer_sizes, hidden, init, seed)`, `forward`, `loss`, `backward`, `fit`, `predict`, `grad_check`. Float64; `X̃ = [X, 1]` nếu docstring ghi vậy. Trước khi dùng dữ liệu thật, chạy `grad_check` và thử huấn luyện trên dữ liệu tổng hợp như trong `tests/test_interfaces.py` (`test_b5_*`). Chuẩn hóa biến đích theo train; chỉ số báo cáo trên thang MWh gốc. Chọn siêu tham số trên val.
3. **Tính tay (`hand_calc.py`)**: 6 mẫu từ `select_six_samples(y_train, seed)`, hai đặc trưng Fisher lớn nhất (cần `features.fisher_score` của Việt), z-score theo train, làm tròn 4 chữ số; mã in ra khớp tính tay ≤ 10⁻⁴.
4. **R1**: lập bảng độ trễ bằng `guards.lag_violations` / `min_safe_lag()` (240 giờ); thí nghiệm có/không rò rỉ (L(h−24), L(h−168)) trên val.
5. **Đánh giá (`evaluate.py`)**: MAPE theo tuần rồi trung bình; MAE, RMSE, đỉnh/đáy/năng lượng tuần; skill score; `bootstrap_ci` ≥ 1.000 lần; tập kiểm tra chỉ qua `guards.open_test_set(final=True)`.
6. **Truy vết**: mỗi hình/bảng thêm một dòng vào `docs/trace_phi.md` (số hình/bảng | tệp | hàm hoặc ô | mã task). Tên tệp theo CONVENTIONS mục 5 (ví dụ `results/figures/5_1_*.png`).

## f. Dùng AI cho phần của bạn
| Được hỏi AI | Không được để AI làm |
|---|---|
| Khái niệm (BP1–BP4, khởi tạo Xavier/He, bootstrap, MAPE) | Nộp mã MLP bạn chưa hiểu (AI được viết; bạn giải thích được từng dòng, Phi review) |
| Cách dùng hàm `pandas`, `scikit-learn` (`MLPRegressor`), `matplotlib` | Viết thay tính tay B7.2 hoặc sinh số cho Phụ lục A |
| Tìm lỗi cú pháp, gợi ý gỡ lỗi, giải thích traceback | Sinh nguyên đoạn báo cáo; sinh số liệu, bảng, hình không do mã nhóm chạy |
| Sửa chính tả, diễn đạt câu chữ | Thêm tài liệu tham khảo chưa đọc |
| Nhờ đặt câu hỏi ôn vấn đáp, kiểm tra suy luận của bạn | Quyết định thay bạn việc mở tập kiểm tra |

Cuối mỗi task (trước `review`), mỗi loại việc AI đã dùng ghi MỘT dòng vào `docs/ai_usage_log.md` (gộp mọi phiên của task; 7 cột và 6 loại T/G/M/B/D/R xem đầu file; việc M ghi tên hàm). Mã MLP do AI viết: bạn phải hiểu và giải thích được từng dòng, ghi rõ trong dòng nhật ký (khai ở Phụ lục C).

## g. Chuẩn bị vấn đáp
**II.2 — phải giải thích được**: công thức BP1–BP4 và vì sao ∂J/∂z của tầng ra tuyến tính + MSE có dạng như vậy; kiểm tra gradient bằng sai phân hữu hạn và vì sao ngưỡng 10⁻⁶; khởi tạo 0 vs Xavier/He; vì sao chuẩn hóa biến đích; định nghĩa MAPE theo tuần; chia dữ liệu theo tuần và quy tắc 72 giờ (độ trễ ≥ 240 giờ); khóa tập kiểm tra.
**II.3 — câu hỏi mẫu (không có đáp án ở đây)**:
1. Tính lại một bước cập nhật mạng 2–2–1 ở Phụ lục A với η khác.
2. Điều gì xảy ra với gradient khi xếp nhiều tầng sigmoid? Khi khởi tạo mọi trọng số bằng nhau?
3. Đổi η hoặc kích thước mini-batch thì đường cong học thay đổi ra sao?
4. Vì sao L(h−168) tạo sai số "ảo" ở R1? Hợp lệ cho bao nhiêu giờ trong tuần?
5. Đọc một dòng trong bảng MAPE theo giờ trong ngày của R3 và giải thích.
6. Vì sao MAPE nhạy với giờ tải thấp bất thường? Nhóm đã xử lý thế nào?
7. Khoảng tin cậy bootstrap được tính trên đơn vị nào (giờ hay tuần)? Vì sao?
**II.4 — phần của hai người còn lại**:
1. (Huấn) Số điều kiện của hàm mất mát liên hệ thế nào với η và với z-score?
2. (Huấn) Momentum thay đổi số lần cập nhật để đạt cùng mức mất mát ra sao?
3. (Việt) Quy ước y·g ≤ 0 trong PLA; vì sao w̃(0) = 0 làm kết quả bất biến theo η?
4. (Việt) Hướng PCA là véc tơ riêng của trị riêng lớn nhất vì sao; LDA hai lớp cho w ∝ ?

## h. Lỗi hay gặp ở khối của bạn
- Rò rỉ: tính phân vị 90% hoặc mean/std chuẩn hóa trên cả bộ dữ liệu thay vì train; chuẩn hóa lại riêng cho val/test.
- Chia tuần sai: tuần bắt đầu Thứ Bảy 00:00 (`hour_in_week` = 0), không phải Thứ Hai; lệch 1 giờ nếu nhãn thời gian là "giờ kết thúc" (UNKNOWN, kiểm trong T002).
- Dùng đặc trưng trễ < 240 giờ (ví dụ 24, 168) trong mô hình chính.
- `grad_check`: bỏ sót bias; eps quá nhỏ gây nhiễu số; kiểm tra trên mẫu quá lớn khiến chậm; quên float64.
- Khởi tạo ngẫu nhiên không lấy từ `config.get_seed()`; kết quả không tái lập.
- Chọn kiến trúc/siêu tham số bằng nhìn tập kiểm tra; chạy `--final` nhiều lần (khóa `results/.test_used` sẽ chặn, đừng xóa để chọn lại).
- Quên đổi thang về MWh gốc trước khi tính MAPE/RMSE; chia cho y = 0 hoặc rất nhỏ.
- Chạy lại tổng > 60 phút vì thí nghiệm lưới quá lớn; quên lấy mẫu con cho thí nghiệm phụ (phải nêu rõ cách lấy).

## Vai trò trưởng nhóm
**Giao task mới**: `python scripts\tasks.py new` (script đang được tạo; nếu chưa chạy được ghi UNKNOWN và nhắn người phụ trách script). Mỗi task có `owner`, `status`, `files:` và hạn; giao theo thứ tự phase trong `docs/CHECKLIST.md`.
**Quy trình review PR** (reviewer là Phi, mỗi người một PR thường trực `<nhánh> → main`):
1. Mở PR, kiểm tiêu đề `[nhánh] Txxx Tyyy` và mẫu PR đã điền đủ.
2. Chạy `python scripts\doctor.py` và `python -m pytest` trên nhánh; không được có test ĐỎ.
3. `git diff main...<nhánh>`: chỉ thay đổi trong `files:` của task và trong danh sách sở hữu (TEAM.md mục 3).
4. Kiểm bất biến: thông số lấy từ `config.py`; không rò rỉ; float64; không `rng` ngoài `get_seed()`; không đọc nhãn tập kiểm tra; notebook không còn output; không tệp > 1 MB.
5. Chỉ HỎI và GỢI Ý công thức hoặc hướng kiểm tra; KHÔNG dán code mẫu cho người khác chép. Với mỗi hàm AI viết trong phần tự cài đặt: **không cần bạn hỏi**; chỉ kiểm mục "Kết quả" của task có dòng `Tự kiểm hiểu (model hỏi): <hàm> | qua`. Thiếu hoặc `chưa qua` thì trả lại (TEAM.md mục 8). Muốn thì hỏi xen kẽ vài hàm, không bắt buộc.
6. Đối chiếu số trong `results/` với dòng truy vết `docs/trace_<tên>.md`.
7. Đạt thì **merge commit, không squash**, rồi báo "đã merge"; mọi người làm lại các bước đầu buổi (TEAM.md mục 4). Không đạt thì ghi mục cần sửa vào task.
**Giữ chuẩn**: chỉ bạn sửa `config.py`, `CONVENTIONS.md`, `CHECKLIST.md`; đổi hằng số → ghi quyết định vào `docs/decisions/`. Cập nhật ☑ trong CHECKLIST khi có bằng chứng.
**Chạy `--final`**: chỉ bạn, đúng một lần, sau khi mọi mô hình, siêu tham số và ngưỡng đã chốt trên val. Muốn chạy lại để tái lập: xóa `results/.test_used` và báo cả nhóm; không dùng để chọn lại.
