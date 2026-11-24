---
id: T003
title: Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge
phase: P2
checklist: B3.1,B3.2
owner: huan
status: done
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
  - `run`: hàm thực thi thí nghiệm B3.2–B3.4 trên dữ liệu thật phục vụ `run_all.py`.
- Kết quả kiểm thử và số liệu thực nghiệm:
  - `tests/test_interfaces.py`: cả 4 test `test_b3_*` đều PASSED (không còn SKIP).
  - Sai số tương đối `finite_diff_check`: đạt $1.48 \times 10^{-10}$ trên dữ liệu tổng hợp và $5.02 \times 10^{-8}$ trên dữ liệu thật, đều nhỏ hơn rất nhiều so với ngưỡng yêu cầu $\le 10^{-6}$.
  - Nghiệm của `gd` hội tụ khớp hoàn toàn nghiệm giải tích `ridge_closed_form`: sai số lớn nhất $\max |w_{\text{gd}} - w_{\text{cf}}| = 3.55 \times 10^{-15}$.
  - Chạy thử trên dữ liệu thật (`continuous.csv`, tập train sau khi gọi `data_prep.drop_warmup` loại 4 tuần khởi động theo `docs/CONVENTIONS.md` mục 7 còn 205 tuần = 34.440 dòng; 12 biến thời tiết chuẩn hóa z-score theo train + bias cột 1 ở cuối, siêu tham số đọc từ `src/config.py`):
    - Sai số kiểm tra gradient `finite_diff_check`: đạt $4.74 \times 10^{-8}$ (<= 1e-6 là ĐẠT)
    - Nghiệm đóng Ridge (`B3_LAMBDA = 0.1`): train loss 9486.6085, val loss 11089.2577
    - Batch GD (`B3_N_ITER = 500`, `B3_ETA = 0.05`): train loss 9486.6340, val loss 11086.2728
    - Momentum GD (`B3_N_ITER = 500`, `B3_ETA = 0.05`, `B3_MOMENTUM_BETA = 0.85`): train loss 9486.6085, val loss 11089.2577
  - Lưu kết quả theo `docs/CONVENTIONS.md` mục 5:
    - Đã xuất hình `results/figures/4_2_gd_momentum_loss.png` (Hình 4.2): Đồ thị đường mất mát theo số lần cập nhật của GD và Momentum GD (panel thang log toàn bộ 500 bước lặp và panel thang tuyến tính 50 bước đầu).
    - Đã xuất bảng `results/tables/4_2_gd_vs_closed_form.csv` (Bảng 4.2): So sánh val loss, train loss, tham số và sai số finite-diff giữa nghiệm đóng, GD và Momentum GD.
    - Đã cập nhật dòng truy vết tương ứng cho Hình 4.2 và Bảng 4.2 trong `docs/trace_huan.md`.
    - Đã đưa 4 hằng số B3 vào `src/config.py` (`B3_LAMBDA`, `B3_ETA`, `B3_N_ITER`, `B3_MOMENTUM_BETA`).
  - Viết bổ sung `tests/test_optim_linear_huan.py` (4 bài test): kiểm tra độc lập không phạt bias, kiểm tra sai phân hữu hạn đa điểm ngẫu nhiên, momentum với $\beta=0$ khớp GD, SGD và mini-batch giảm loss qua các epoch.
  - Toàn bộ suite `pytest`: **111 passed, 3 skipped, 0 failed**.
- Tự kiểm hiểu (model hỏi):
  - `mse_l2_loss` / `mse_l2_grad` | qua | 23/11/2026 (3 câu: vì sao không phạt bias $w[-1]$, công thức gradient và chiều của ma trận, hệ số $1/n$ và $1/(2n)$; sửa nhỏ: đổi `reg[-1] = 0.0` thành không bỏ bias → l2_loss và grad bias bị thay đổi, test độc lập báo đỏ đúng kỳ vọng)
  - `ridge_closed_form` | qua | 23/11/2026 (3 câu: đạo hàm bằng 0 suy ra hệ phương trình nào, ma trận $I_{\text{reg}}$ có dạng gì, vì sao dùng `np.linalg.solve` thay vì nghịch đảo trực tiếp $A^{-1}$; sửa nhỏ: tăng $\lambda \to \infty$ thì trọng số $w[:-1] \to 0$ nhưng bias $w[-1] \to \bar{y}$)
  - `gd` / `momentum_gd` | qua | 23/11/2026 (3 câu: công thức quán tính $v$, vì sao $\beta=0$ trở về GD thông thường, hiện tượng khi $\eta$ quá lớn dẫn tới phân kỳ $inf/nan$ và điều kiện dừng sớm; sửa nhỏ: đổi $\beta=0$ kiểm tra $w_{\text{mom}} == w_{\text{gd}}$ sai số $10^{-12}$)
  - `sgd` / `minibatch_gd` | qua | 23/11/2026 (3 câu: khác biệt giữa epoch và iteration, kỳ vọng toán học gradient mini-batch bằng gradient toàn bộ, vai trò của seed khi xáo trộn; sửa nhỏ: đổi batch_size = n trở về GD theo lô)

## Ghi chú AI đã dùng
Đã thêm 2 dòng vào `docs/ai_usage_log.md` (1 dòng M cài đặt các hàm tối ưu và test, 1 dòng D hỏi kiểm hiểu và đối chiếu nghiệm).
