# Nhật ký quyết định (chỉ Phi thêm dòng)

Đổi một hằng số trong `src/config.py` hoặc một quy ước trong `docs/CONVENTIONS.md` thì thêm một dòng ở đây trước khi merge.

| Ngày | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| 17/11/2026 | Nhóm làm Đề 3; mã nhóm G = 18, SEED = 2044 | Cột "Nhóm" trên sheet đăng ký của lớp; SEED = 2026 + G (đề mục 2.1) | Mọi `rng` lấy từ `config.get_seed()` |
| 17/11/2026 | Đặc trưng trễ cố định phải ≥ 240 giờ; không dùng trễ 168 giờ | Quy tắc 72 giờ của đề: chỉ biết phụ tải đến hết Thứ Ba | `guards.min_safe_lag()`, `tests/test_guards.py` |
| 17/11/2026 | Nới luật AI về mã: AI được viết mã phần tự cài đặt nếu người nộp giải thích được, Phi review, ghi nhật ký. Giữ cấm sinh đoạn báo cáo, số liệu hoặc trích dẫn chưa kiểm | Đề mục 7 chỉ cấm nộp mã AI sinh "khi chưa hiểu"; cấm sinh nguyên đoạn báo cáo không có điều kiện | `TEAM.md` mục 8, `AGENTS.md`, `docs/{PHI,HUAN,VIET}.md`, agents, prompts, tasks. Rủi ro: mục 2.4 "tự cài đặt" có thể bị hiểu chặt hơn |
| 17/11/2026 | Ngưỡng hiểu trước khi merge hàm do AI viết: 3 câu trực tiếp không mở AI + tự sửa một chỗ nhỏ | Mã AI viết 100% rủi ro vấn đáp (ki ≤ 0,5 nếu Phần II < 3,0), đối chiếu chéo giữa các nhóm | `TEAM.md` mục 8, `docs/PHI.md` bước review 5 |
| 17/11/2026 | Kiểm hiểu do model chủ động hỏi (task-runner) trước khi `review`; Phi chỉ kiểm có dòng "qua" | Giảm tải cho Phi khi merge; chấp nhận kiểm tự giác (yếu hơn Phi hỏi trực tiếp) | `TEAM.md` mục 8, `docs/PHI.md`, agents, prompts, task template, mẫu PR |
| 17/11/2026 | Nhật ký AI ghi theo loại việc (T/G/M/B/D/R), mỗi loại một dòng cho mỗi task; thêm `scripts/ai_log.py` (check, appendix); CI kiểm định dạng | Giảm số dòng cho thành khoảng 10–14 dòng Phụ lục C vừa 1 trang | `docs/ai_usage_log.md`, `TEAM.md`, `docs/{PHI,HUAN,VIET}.md`, agents, prompts, task template, mẫu PR, `.github/workflows/ci.yml` |
| 17/11/2026 | Hạt giống lặp = SEED..SEED+4 (`get_run_seeds`, `N_RUN_SEEDS` = 5) | Đề B4.3 cần ≥ 5 hạt giống; cần quy ước chung để ba người ra cùng số | `src/config.py`, `docs/CONVENTIONS.md` mục 7 |
| 17/11/2026 | Bootstrap theo tuần, 2000 lần, CI 95% phân vị | Giờ liền nhau tương quan; đề yêu cầu ≥ 1.000 lần | `config.BOOTSTRAP_ITERS`, `BOOTSTRAP_CI` |
| 17/11/2026 | Tref chọn từ lưới phân vị `TREF_QUANTILES` của T trung bình 3 thành phố trên train, theo MAPE kiểm định | Không có nguồn cho giá trị Tref; tránh giả định đơn vị | `config.TREF_QUANTILES` |
| 17/11/2026 | Trễ và cửa sổ trượt dùng `FEATURE_LAGS_HOURS` = (336, 504, 672) | Khớp mô hình cơ sở (tuần 2–4), mọi trễ ≥ 240 giờ | `config.FEATURE_LAGS_HOURS` |
| 17/11/2026 | Nhãn B7.2 dùng {0, 1} | BCE cần nhãn {0, 1}; thống nhất với B7.1 | `docs/CONVENTIONS.md` mục 3 |
| 17/11/2026 | Nhãn thời gian phụ tải là giờ kết thúc: lùi 1 giờ (`TIMESTAMP_SHIFT_HOURS = -1`); thay quyết định "mặc định 0" ngày 17/11 | T001 18/11: 48.048 dòng = 286 tuần đủ giờ, dòng đầu 01:00, dòng cuối 00:00 Thứ Bảy; offset 0 làm vỡ phép chia tuần. T002 còn phải căn với CND | `docs/CONVENTIONS.md` mục 1 |
| 18/11/2026 | 4 tuần đầu của train chỉ làm lịch sử, không huấn luyện (`WARMUP_WEEKS`, phương án A); không điền khuyết | Trễ 672 giờ cần 4 tuần lịch sử; điền khuyết là bịa số | `config.WARMUP_WEEKS`, `data_prep.drop_warmup` |
| 18/11/2026 | Báo cáo và hồ sơ giao cho Huấn soạn và ghép; Phi tập trung phần core cùng Việt và duyệt final | Phi quản lý hai dự án; Huấn nhẹ nhất ở P3. Mỗi người vẫn tự viết phần khối mình (vấn đáp hỏi từng người) | README "Việc chính của từng người", `docs/CHECKLIST.md` (TĐ, B10.1, HS), `tasks/T008–T010` (T008 báo cáo tiến độ, T009 bảng truy vết, T010 ghép hồ sơ) |
