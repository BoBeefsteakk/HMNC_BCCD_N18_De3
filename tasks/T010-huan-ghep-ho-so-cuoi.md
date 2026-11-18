---
id: T010
title: Ghép hồ sơ cuối
phase: P5
checklist: HS
owner: huan
status: todo
due: 22/12/2026
files: docs/BAOCAO_DAN_Y.md,docs/trace_huan.md
depends: T009
---
# T010 — Ghép hồ sơ cuối

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Ghép hồ sơ cuối (mã HS): báo cáo .docx và .pdf tên `HMNC_BCCD_N18_De3`, Phụ lục B (phân công, tỉ lệ đóng góp, chữ ký), Phụ lục C (khai báo AI, lấy từ `python scripts\ai_log.py appendix`), Phụ lục D (T009), slide ≤ 15 trang, README. Phi duyệt final.

## Đầu vào cần đọc
- `docs/CHECKLIST.md` (dòng HS), `docs/BAOCAO_DAN_Y.md` (mục "Checklist trước khi nộp")
- `docs/DE3.md` (quy định nộp, mục 2.2)

## Không được làm
- **AI không sinh đoạn báo cáo** (đề mục 7: cấm vô điều kiện). AI chỉ được sửa chính tả, diễn đạt (loại B, chỉ sửa chữ), dàn ý và đối chiếu số liệu (loại D); ghi `docs/ai_usage_log.md`.
- Không tự viết phần của Phi hoặc Việt: mỗi người tự viết phần khối mình (vấn đáp hỏi từng người). Việc của bạn là ghép, định dạng, kiểm nhất quán.
- Số liệu chỉ lấy từ tệp trong `results/`; không có kết quả thì ghi "chưa có", không bịa số.
- Không sửa file ngoài `files:`; thiếu thông tin thì ghi vào task và báo Phi.

## Xong khi
- Bản ghép xong gửi Phi trước **22/12/2026**; hạn nộp **25/12/2026** (muộn −1,0 điểm/ngày).
- Đủ thành phần theo 2.2; Phụ lục C khớp `docs/ai_usage_log.md`.
- Cảnh báo cho Phi: nộp mã qua GitHub thì repo phải riêng tư và mời giảng viên (hiện repo đang công khai).

## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
Tự kiểm hiểu (model hỏi): (mỗi hàm AI viết một dòng: `<hàm> | qua | <ngày>`; không có hàm AI viết thì ghi "không có")

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
