# Nhật ký quyết định (chỉ Phi thêm dòng)

Đổi một hằng số trong `src/config.py` hoặc một quy ước trong `docs/CONVENTIONS.md` thì thêm một dòng ở đây trước khi merge.

| Ngày | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| 17/11/2026 | Nhóm làm Đề 3; mã nhóm G = 18, SEED = 2044 | Cột "Nhóm" trên sheet đăng ký của lớp; SEED = 2026 + G (đề mục 2.1) | Mọi `rng` lấy từ `config.get_seed()` |
| 17/11/2026 | Đặc trưng trễ cố định phải ≥ 240 giờ; không dùng trễ 168 giờ | Quy tắc 72 giờ của đề: chỉ biết phụ tải đến hết Thứ Ba | `guards.min_safe_lag()`, `tests/test_guards.py` |
| 17/11/2026 | Nới luật AI về mã: AI được viết mã phần tự cài đặt nếu người nộp giải thích được, Phi review, ghi nhật ký. Giữ cấm sinh đoạn báo cáo, số liệu hoặc trích dẫn chưa kiểm | Đề mục 7 chỉ cấm nộp mã AI sinh "khi chưa hiểu"; cấm sinh nguyên đoạn báo cáo không có điều kiện | `TEAM.md` mục 8, `AGENTS.md`, `docs/{PHI,HUAN,VIET}.md`, agents, prompts, tasks. Rủi ro: mục 2.4 "tự cài đặt" có thể bị hiểu chặt hơn |
| 17/11/2026 | Ngưỡng hiểu trước khi merge hàm do AI viết: 3 câu trực tiếp không mở AI + tự sửa một chỗ nhỏ | Mã AI viết 100% rủi ro vấn đáp (ki ≤ 0,5 nếu Phần II < 3,0), đối chiếu chéo giữa các nhóm | `TEAM.md` mục 8, `docs/PHI.md` bước review 5 |
