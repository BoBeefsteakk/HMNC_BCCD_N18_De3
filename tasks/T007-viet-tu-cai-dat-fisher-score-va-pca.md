---
id: T007
title: Tự cài đặt Fisher score và PCA
phase: P2
checklist: B6.1,B6.3
owner: viet
status: done
due: 27/11/2026
files: src/features.py
depends: -
---
# T007 — Tự cài đặt Fisher score và PCA

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tự cài đặt `fisher_score` và `pca` (trị riêng ma trận hiệp phương sai chia n−1, hoặc SVD) trên dữ liệu tổng hợp.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `src/features.py` (docstring)
- `docs/CONVENTIONS.md` mục 2
- `tests/test_interfaces.py` (các test_b6_*; KHÔNG sửa)
- `docs/VIET.md`


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- Các `test_b6_pca_*` xanh, KHÔNG SKIP.
- Trị riêng khớp `sklearn.decomposition.PCA` đến 1e-6 (sklearn chỉ dùng để đối chứng).
- `fisher_score` có kiểm tra trên dữ liệu tổng hợp mà bạn tự tính tay được.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- ☑ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- Đã cài `pca` và `fisher_score` trong `src/features.py` (NumPy, float64). `lda_two_class`, `lda_multiclass`, `run` vẫn là stub (ngoài T007).
- `pca(X, k)`: X **không** có cột 1; trừ trung bình, hiệp phương sai `Xcᵀ Xc / (n − 1)`, `np.linalg.eigh`, xếp trị riêng giảm dần, lấy k véc tơ riêng làm hàng của `components`. Dấu: phần tử có |·| lớn nhất mang dấu dương (quy ước B7.3). `explained_ratio` = trị riêng / tổng mọi trị riêng.
- `fisher_score(x, y)`: J = (m1 − m0)² / (s1² + s0²), s² là phương sai trong lớp **chia n_c**; nhận nhãn ±1 hoặc {0, 1}; mẫu số 0 thì trả inf (hai trung bình khác) hoặc 0.
- UNKNOWN: hỏi Phi — CONVENTIONS chưa chốt công thức Fisher (chia n_c hay n_c − 1, hay dạng tán xạ Σ(x − m)² của Duda). Với lớp lệch 10/90 thì cách chia có thể đổi thứ hạng; `hand_calc.py` (B7) dùng hàm này nên cần chốt một dạng.
- Kiểm trên dữ liệu tổng hợp tính tay được (`tests/test_features_viet.py`): Fisher với x = (1, 2, 3 | 5, 7) → m0 = 2, s0² = 2/3, m1 = 6, s1² = 1, J = 16 / (5/3) = 9,6; PCA hai điểm (0, 0), (2, 2) → trị riêng 4, véc tơ (1, 1)/√2. Thêm kiểm: đổi mã nhãn không đổi J, đặc trưng hằng, dấu PCA, trực chuẩn, tổng tỉ lệ = 1 khi k = d.
- Đối chứng sklearn (dữ liệu của `test_b6_pca_*`, seed 3): max |Δ trị riêng| = 1,8·10⁻¹⁵, max |Δ tỉ lệ| = 1,1·10⁻¹⁶ (ngưỡng 10⁻⁶).
- Lệnh: `python -m pytest -q tests/test_features_viet.py tests/test_interfaces.py -k "b6 or features_viet"` → 7 passed, 1 skipped (LDA, ngoài T007); `python -m pytest -q` → 98 passed, 10 skipped, 0 đỏ (22/11/2026).
- Chạy thử trên train thật (22/11/2026; không ghi file kết quả): `fisher_score` chạy trên cả 15 cột (thời tiết + lịch), mọi giá trị hữu hạn, cao nhất là ba cột T2M; `pca` trên 12 biến thời tiết z-score theo train, max |Δ trị riêng| với sklearn = 1,3·10⁻¹⁵.
- Chỗ còn dở: bảng xếp hạng Fisher và biểu đồ PCA cho báo cáo (B6.1, B6.3) để task sau; con số ở trên chỉ để kiểm mã, không đưa vào báo cáo.
- Tự kiểm hiểu (model hỏi): `fisher_score` | qua | 22/11/2026 (3 câu: ý nghĩa tử/mẫu, tính tay x = (0, 2 | 4, 6) → J = 8, chỉ tính trên train)
- Tự kiểm hiểu (model hỏi): `pca` | qua | 22/11/2026 (3 câu: trừ trung bình, chia n thì trị riêng nhân (n−1)/n và véc tơ riêng không đổi, z-score khi khác đơn vị; sửa nhỏ: `/ (n - 1)` → `/ n`, giải thích test đỏ)

## Ghi chú AI đã dùng
Có: Claude Code viết `pca`, `fisher_score` và test bổ sung; soạn câu hỏi ôn để tự kiểm hiểu. Đã ghi 2 dòng (M, D) vào `docs/ai_usage_log.md`.
