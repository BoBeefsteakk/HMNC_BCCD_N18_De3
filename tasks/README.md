# Task của nhóm

1. Task do Phi tạo (`python scripts\tasks.py new ...`); người làm không tự tạo hay đổi nội dung giao việc.
2. Tìm task có `owner` là bạn và `status: todo`, ưu tiên theo hạn (`due`).
3. Chỉ sửa các file ghi ở dòng `files:` của task; thông số lấy từ `src/config.py`.
4. Người làm chỉ đổi `status` (todo → doing → review) và điền mục "Kết quả"; Phi đặt `done` sau khi merge.
5. Commit theo mẫu `T003 feat(b3): ...`; dùng AI thì thêm một dòng vào `docs/ai_usage_log.md`.
6. Kiểm tra: `python scripts\tasks.py check`. Bảng dưới do `python scripts\tasks.py readme` sinh, không sửa tay.


## P1

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T001 | phi | review | 20/11/2026 | B1.4 | [Nạp dữ liệu phụ tải và chia tuần](T001-phi-nap-du-lieu-phu-tai-va-chia-tuan.md) |
| T004 | huan | todo | 21/11/2026 | B1.2 | [Từ điển dữ liệu](T004-huan-tu-dien-du-lieu.md) |
| T002 | phi | todo | 22/11/2026 | B1.4,R2 | [Căn dự báo CND với phụ tải thực](T002-phi-can-du-bao-cnd-voi-phu-tai-thuc.md) |

## P2

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T003 | huan | todo | 25/11/2026 | B3.1,B3.2 | [Tự cài đặt GD, SGD, mini-batch, momentum và nghiệm đóng ridge](T003-huan-tu-cai-dat-gd-sgd-mini-batch-va-nghiem-d.md) |
| T006 | viet | todo | 25/11/2026 | B4.1 | [Tự cài đặt PLA và Pocket](T006-viet-tu-cai-dat-pla-va-pocket.md) |
| T005 | huan | todo | 26/11/2026 | B1.1,B1.3 | [Bài toán nghiệp vụ và EDA](T005-huan-bai-toan-nghiep-vu-va-eda.md) |
| T007 | viet | todo | 27/11/2026 | B6.1,B6.3 | [Tự cài đặt Fisher score và PCA](T007-viet-tu-cai-dat-fisher-score-va-pca.md) |
| T008 | huan | todo | 27/11/2026 | TĐ | [Báo cáo tiến độ 2–3 trang](T008-huan-bao-cao-tien-do-2-3-trang.md) |

## P5

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T009 | huan | todo | 20/12/2026 | B10.1 | [Bảng truy vết (Phụ lục D) và kiểm cấu trúc báo cáo](T009-huan-bang-truy-vet-phu-luc-d-va-kiem-cau-truc.md) |
| T010 | huan | todo | 22/12/2026 | HS | [Ghép hồ sơ cuối](T010-huan-ghep-ho-so-cuoi.md) |
