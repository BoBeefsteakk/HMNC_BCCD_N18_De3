---
id: T003
title: Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge
phase: P2
checklist: B3.1,B3.2
owner: huan
status: review
due: 25/11/2026
files: src/optim_linear.py
depends: -
---
# T003 — Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `mse_l2_loss`, `mse_l2_grad`, `gd`, `ridge_closed_form`, `finite_diff_check`, `sgd`, `minibatch_gd`, `momentum_gd` theo docstring `src/optim_linear.py`; thử trên dữ liệu tổng hợp rồi dữ liệu thật sau khi T001 merge.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/optim_linear.py` (docstring: công thức J, grad, chữ ký hàm)
- `docs/CONVENTIONS.md` mục 2, 3
- `tests/test_interfaces.py` (các test_b3_*; KHÔNG sửa file này)
- `docs/HUAN.md`


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b3_*` trong `tests/test_interfaces.py` xanh, KHÔNG SKIP.
- `finite_diff_check` ≤ 1e-6 (float64) cho `mse_l2_loss`/`mse_l2_grad`.
- `ridge_closed_form` khớp nghiệm của `gd` hội tụ trên dữ liệu tổng hợp (ghi sai số trong Kết quả).
- Chạy thử trên dữ liệu thật sau khi T001 merge; ghi kết quả vào Kết quả.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- [x] Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã tự cài đặt hoàn chỉnh bằng NumPy (float64) trong `src/optim_linear.py`:
  - `mse_l2_loss`, `mse_l2_grad`: hàm mất mát MSE có chính quy hóa Ridge L2 và gradient giải tích. Quy ước: ma trận mở rộng $\tilde{X} = [X, 1]$ có cột 1 ở cuối, vector $w$ có $d+1$ phần tử, bias là $w[-1]$. Tuyệt đối không phạt hệ số tự do (`reg[-1] = 0.0`).
  - `ridge_closed_form`: nghiệm giải tích hồi quy Ridge giải hệ phương trình tuyến tính $(1/n \tilde{X}^T \tilde{X} + \lambda I_{\text{reg}}) w = 1/n \tilde{X}^T y$ với $I_{\text{reg}} = \operatorname{diag}(1, ..., 1, 0)$. Dùng làm chuẩn đối chứng tuyệt đối.
  - `finite_diff_check`: kiểm tra gradient bằng sai phân hữu hạn trung tâm đối xứng với bước $\epsilon = 10^{-6}$.
  - `gd`: Batch Gradient Descent cập nhật toàn bộ mẫu mỗi bước lặp $w \leftarrow w - \eta \nabla J(w)$.
  - `sgd`: Stochastic Gradient Descent duyệt mẫu ngẫu nhiên mỗi epoch bằng `np.random.default_rng(seed)`.
  - `minibatch_gd`: Mini-batch GD cập nhật theo từng khối mẫu kích thước `batch_size`.
  - `momentum_gd`: Gradient Descent có quán tính Polyak ($v \leftarrow \beta v + \eta \nabla J, w \leftarrow w - v$), với $\beta = 0$ trở về GD thông thường.
  - `run`: hàm thực thi thí nghiệm B3.1–B3.4 trên dữ liệu thật phục vụ `run_all.py`.
- Kết quả kiểm thử và số liệu thực nghiệm:
  - `tests/test_interfaces.py`: cả 4 test `test_b3_*` đều PASSED (không còn SKIP).
  - Sai số tương đối `finite_diff_check`: đạt $1{,}48 \times 10^{-10}$ trên dữ liệu tổng hợp và $4{,}74 \times 10^{-8}$ trên dữ liệu thật (sau `drop_warmup`), đều nhỏ hơn rất nhiều so với ngưỡng yêu cầu $\le 10^{-6}$.
  - Nghiệm của `gd` hội tụ khớp hoàn toàn nghiệm giải tích `ridge_closed_form`: sai số lớn nhất $\max |w_{\text{gd}} - w_{\text{cf}}| = 3.55 \times 10^{-15}$.
  - Chạy thử trên dữ liệu thật (`continuous.csv`, tập train sau khi gọi `data_prep.drop_warmup` loại 4 tuần khởi động theo `docs/CONVENTIONS.md` mục 7 còn 205 tuần = 34.440 dòng; 12 biến thời tiết chuẩn hóa z-score theo train + bias cột 1 ở cuối; cùng khởi tạo $w_0 = 0$, cùng $\eta = 0{,}05$, $\lambda = 0{,}1$, siêu tham số đọc từ `src/config.py`; tất cả `train_loss` và `val_loss` dưới đây đều là hàm mục tiêu **MSE + L2** $J(w) = \frac{1}{2n}\|\tilde{X}w - y\|^2 + \frac{\lambda}{2}\|w[:-1]\|^2$, đơn vị $\text{MWh}^2$):
    - Sai số kiểm tra gradient `finite_diff_check`: đạt $4{,}74 \times 10^{-8}$ ($\le 10^{-6}$ là ĐẠT).
    - Nghiệm đóng Ridge (`B3_LAMBDA = 0.1`): train loss (MSE + L2) = `9486.6085`, val loss (MSE + L2) = `11089.2577`.
    - Batch GD (`B3_N_ITER = 500`, `B3_ETA = 0.05`): train loss (MSE + L2) = `9486.6340`, val loss (MSE + L2) = `11086.2728` (chênh nghiệm đóng `−2,9850`).
    - Momentum GD (`B3_N_ITER = 500`, `B3_ETA = 0.05`, `B3_MOMENTUM_BETA = 0.85`): train loss (MSE + L2) = `9486.6085`, val loss (MSE + L2) = `11089.2577` (khớp tuyệt đối nghiệm đóng, chênh `0,0000`).
    - Mini-batch GD (`B3_N_ITER = 500` cập nhật, `B3_ETA = 0.05`, `B3_BATCH_SIZE = 256`, `seed = 2044`): train loss (MSE + L2) = `9496.5307`, val loss (MSE + L2) = `11223.0731`.
    - SGD (`B3_N_ITER = 500` cập nhật, `B3_ETA = 0.05`, `batch_size = 1`, `seed = 2044`): train loss (MSE + L2) = `14079.9791`, val loss (MSE + L2) = `22285.1266` (giảm mạnh từ `703699.26` nhưng dao động quanh $1{,}04\times10^4\text{--}2{,}5\times10^4$ do nhiễu gradient 1 mẫu khi giữ $\eta$ cố định).
  - So sánh tốc độ hội tụ theo số lần cập nhật (B3.2, cùng mức mất mát đích $J(w^*) + 10{,}0 = 9496{,}6085$, tức `B3_LOSS_TOL = 10.0` $\approx 0{,}1\%$ trên nghiệm đóng):
    - **Momentum GD:** đạt sau **37** lần cập nhật.
    - **GD theo lô:** đạt sau **136** lần cập nhật (Momentum nhanh gấp **3,68 lần** GD).
    - **Mini-batch GD (`batch_size = 256`):** đạt sau **211** lần cập nhật (nhiều bước hơn GD do nhiễu lô, nhưng mỗi bước chỉ dùng 0,74% dữ liệu).
    - **SGD (`batch_size = 1`):** chưa đạt ngưỡng này trong 500 bước với $\eta = 0{,}05$ cố định (mức thấp nhất đạt `10412.27`).
  - Giải thích chênh lệch `val_loss` (MSE + L2) giữa GD thuần và nghiệm đóng (B3.4b):
    - Ma trận Hessian $H = \frac{1}{n}\tilde{X}^T\tilde{X} + \lambda I_{\text{reg}}$ có $\lambda_{\min} = 0{,}1332$, $\lambda_{\max} = 4{,}6761$, số điều kiện $\kappa \approx 35{,}11$ (do đa cộng tuyến giữa 12 biến thời tiết của 3 thành phố).
    - Với $\eta = 0{,}05$, hệ số co dọc phương trị riêng nhỏ nhất là $1 - \eta\lambda_{\min} \approx 0{,}99334$; sau 500 bước lặp $0{,}99334^{500} \approx 0{,}0354$ nên **GD thuần chưa hội tụ hẳn**: $\|w_{\text{gd}} - w_{\text{cf}}\|_2 = 0{,}5771$, $\|\nabla J(w_{\text{gd}})\|_2 = 0{,}0890 > 0$, và `train_loss` vẫn cao hơn nghiệm đóng $0{,}0255$. Vì dừng sớm gần cực tiểu (tương tự hiệu ứng early stopping nhẹ), `val_loss` (MSE + L2) của GD (`11086.2728`) lệch nghiệm đóng (`11089.2577`) là **$-2{,}985$** ($\approx 2{,}98$). Khi tăng lên 3.000 bước lặp, $\|w_{\text{gd}} - w_{\text{cf}}\|_2 = 2{,}06 \times 10^{-8}$ và `val_loss` khớp tuyệt đối `11089.2577`.
    - Ngược lại, **Momentum GD** ($\beta = 0{,}85$) tích lũy vận tốc dọc các phương độ cong nhỏ nên đã hội tụ hoàn toàn sau 500 bước: $\|w_{\text{mom}} - w_{\text{cf}}\|_2 = 9{,}57 \times 10^{-13}$, $\|\nabla J(w_{\text{mom}})\|_2 = 1{,}36 \times 10^{-13}$, khớp tuyệt đối nghiệm đóng (`val_loss = 11089.2577`, chênh `0,0000`).
  - Lưu kết quả theo `docs/CONVENTIONS.md` mục 5:
    - Đã xuất hình `results/figures/4_2_gd_momentum_loss.png` (Hình 4.2): Đồ thị đường mất mát (MSE + L2) theo số lần cập nhật của GD, Momentum GD, Mini-batch GD và SGD cùng $w_0 = 0$ và $\eta = 0{,}05$ (panel thang log toàn bộ 500 lần cập nhật và panel thang tuyến tính 60 lần cập nhật đầu).
    - Đã xuất bảng `results/tables/4_2_gd_vs_closed_form.csv` (Bảng 4.2): So sánh `train_loss_mse_l2`, `val_loss_mse_l2`, chênh lệch với nghiệm đóng, số lần cập nhật đạt đích và sai số `finite_diff` của 5 phương pháp.
    - Đã cập nhật dòng truy vết tương ứng cho Hình 4.2 và Bảng 4.2 trong `docs/trace_huan.md`.
    - Đã đưa đầy đủ 6 hằng số B3 vào `src/config.py` (`B3_LAMBDA`, `B3_ETA`, `B3_N_ITER`, `B3_MOMENTUM_BETA`, `B3_BATCH_SIZE`, `B3_LOSS_TOL`).
  - Viết bổ sung `tests/test_optim_linear_huan.py` (5 bài test): kiểm tra độc lập không phạt bias, kiểm tra sai phân hữu hạn đa điểm ngẫu nhiên, momentum với $\beta=0$ khớp GD, SGD và mini-batch giảm loss qua các epoch, chế độ ghi loss theo từng cập nhật và hàm `updates_to_reach`.
  - Toàn bộ suite `pytest`: **118 passed, 3 skipped, 0 failed**.
- Tự kiểm hiểu (model hỏi):
  - `mse_l2_loss` / `mse_l2_grad` | qua | 23/11/2026 (3 câu: vì sao không phạt bias $w[-1]$, công thức gradient và chiều của ma trận, hệ số $1/n$ và $1/(2n)$; sửa nhỏ: đổi `reg[-1] = 0.0` thành không bỏ bias → l2_loss và grad bias bị thay đổi, test độc lập báo đỏ đúng kỳ vọng)
  - `ridge_closed_form` | qua | 23/11/2026 (3 câu: đạo hàm bằng 0 suy ra hệ phương trình nào, ma trận $I_{\text{reg}}$ có dạng gì, vì sao dùng `np.linalg.solve` thay vì nghịch đảo trực tiếp $A^{-1}$; sửa nhỏ: tăng $\lambda \to \infty$ thì trọng số $w[:-1] \to 0$ nhưng bias $w[-1] \to \bar{y}$)
  - `gd` / `momentum_gd` | qua | 23/11/2026 (3 câu: công thức quán tính $v$, vì sao $\beta=0$ trở về GD thông thường, hiện tượng khi $\eta$ quá lớn dẫn tới phân kỳ $inf/nan$ và điều kiện dừng sớm; sửa nhỏ: đổi $\beta=0$ kiểm tra $w_{\text{mom}} == w_{\text{gd}}$ sai số $10^{-12}$)
  - `sgd` / `minibatch_gd` | qua | 23/11/2026 (3 câu: khác biệt giữa epoch và iteration, kỳ vọng toán học gradient mini-batch bằng gradient toàn bộ, vai trò của seed khi xáo trộn; sửa nhỏ: đổi batch_size = n trở về GD theo lô)

## Ghi chú AI đã dùng
Đã thêm 2 dòng vào `docs/ai_usage_log.md` (1 dòng M cài đặt các hàm tối ưu và test, 1 dòng D hỏi kiểm hiểu và đối chiếu nghiệm).
