# Nhật ký quyết định (chỉ Phi thêm dòng)

Đổi một hằng số trong `src/config.py` hoặc một quy ước trong `docs/CONVENTIONS.md` thì thêm một dòng ở đây trước khi merge.

| Ngày | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| 17/11/2026 | Nhóm làm Đề 3; mã nhóm G = 18, SEED = 2044 | Cột "Nhóm" trên sheet đăng ký của lớp; SEED = 2026 + G (đề mục 2.1) | Mọi `rng` lấy từ `config.get_seed()` |
| 17/11/2026 | Đặc trưng trễ cố định phải ≥ 240 giờ; không dùng trễ 168 giờ | Quy tắc 72 giờ của đề: chỉ biết phụ tải đến hết Thứ Ba | `guards.min_safe_lag()`, `tests/test_guards.py` |
