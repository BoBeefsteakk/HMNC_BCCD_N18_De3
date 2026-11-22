---
id: T006
title: Tự cài đặt PLA và Pocket
phase: P2
checklist: B4.1
owner: viet
status: doing
due: 25/11/2026
files: src/perceptron.py
depends: -
---
# T006 — Tự cài đặt PLA và Pocket

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `count_errors`, `pla`, `pocket` theo docstring `src/perceptron.py` với quy ước nhãn ±1, x̃ = (x, 1), w̃(0) = 0 và mẫu có y·g ≤ 0 là sai (kể cả g = 0).


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/perceptron.py` (docstring)
- `docs/CONVENTIONS.md` mục 3
- `tests/test_interfaces.py` (các test_b4_*; KHÔNG sửa)
- `docs/VIET.md`


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b4_*` trong `tests/test_interfaces.py` xanh, KHÔNG SKIP.
- Nêu rõ thứ tự duyệt và điều kiện dừng trong Kết quả (cần cho báo cáo B4.1).
- `pocket` trả về w có số lỗi trên tập huấn luyện không lớn hơn `pla` trên dữ liệu thử.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã cài `count_errors`, `pla`, `pocket` trong `src/perceptron.py` (NumPy, float64). `check_separable_lp` và `run` vẫn là stub (B4.2–B4.4, ngoài T006).
- Đầu vào: `X` là X̃ đã có cột 1 ở cuối (người gọi thêm); nhãn bắt buộc ±1, sai thì báo lỗi. w̃(0) = 0, η = 1.
- Mẫu sai: `y·g <= 0` (kể cả g = 0), dùng chung trong cả ba hàm.
- **Thứ tự duyệt:** `shuffle=False` duyệt mẫu 0, 1, …, n−1 mỗi epoch; `shuffle=True` lấy hoán vị mới mỗi epoch từ `np.random.default_rng(seed)`.
- **Điều kiện dừng:** sau mỗi epoch đếm lỗi trên toàn tập; dừng khi 0 lỗi hoặc hết `max_epochs`.
- **Pocket:** cùng các bước cập nhật như PLA; sau mỗi lần cập nhật đếm lại lỗi toàn tập, giữ w ít lỗi nhất (túi ban đầu là w̃ = 0, n lỗi). `errors_per_epoch` ghi lỗi của w trong túi nên không tăng.
- Lệnh: `python -m pytest -q tests/test_interfaces.py -k b4` → 2 passed (không SKIP); `python -m pytest -q` → 91 passed, 11 skipped, 0 đỏ (22/11/2026).
- Chạy thử dữ liệu tổng hợp (như `_blobs` trong test, rng seed 0): khả tách (gap 10) PLA về 0 lỗi sau 1 epoch; không khả tách (gap 1, lật 15% nhãn, 120 mẫu, 50 epoch) PLA cuối 59 lỗi, dao động 45–65; Pocket 32 lỗi.
- Thêm `tests/test_perceptron_viet.py` (22/11/2026): đếm lỗi độc lập với `pc.count_errors`. Lý do: nếu `count_errors` lỡ dùng `< 0` thì Pocket trả w = 0 ("0 lỗi") mà `test_b4_*` vẫn xanh, vì test đó so bằng chính `count_errors`. Test mới bắt được lỗi này (đã thử). `python -m pytest -q` → 100 passed, 10 skipped, 0 đỏ.
- Chỗ còn dở: Pocket đếm lại lỗi toàn tập sau mỗi cập nhật nên chậm hơn PLA trên dữ liệu thật (~35 nghìn giờ train); chưa chạy trên nhãn cao điểm thật.
- Tự kiểm hiểu (model hỏi): `pla` | qua | 22/11/2026 (3 câu: điều kiện `<= 0`, bất biến theo η khi w̃(0) = 0, PLA trên dữ liệu không khả tách; sửa nhỏ: đổi `<= 0` thành `< 0` → w kẹt ở 0, errs = n mọi epoch)
- Tự kiểm hiểu (model hỏi): `pocket`, `count_errors` | chưa qua | 22/11/2026 (chưa hỏi: người làm dừng phần kiểm hiểu, tự khai đã hiểu; cần làm trước khi đặt `review`)

## Ghi chú AI đã dùng
Có: Claude Code viết `count_errors`, `pla`, `pocket` và hỏi kiểm hiểu; đã ghi 2 dòng (M, D) vào `docs/ai_usage_log.md`.
