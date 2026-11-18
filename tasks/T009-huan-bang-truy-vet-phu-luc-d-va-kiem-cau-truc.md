---
id: T009
title: Bảng truy vết (Phụ lục D) và kiểm cấu trúc báo cáo
phase: P5
checklist: B10.1
owner: huan
status: todo
due: 20/12/2026
files: docs/BAOCAO_DAN_Y.md,docs/trace_huan.md
depends: T008
---
# T009 — Bảng truy vết (Phụ lục D) và kiểm cấu trúc báo cáo

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Ghép bảng truy vết (Phụ lục D) từ `docs/trace_phi.md`, `docs/trace_huan.md`, `docs/trace_viet.md`; kiểm báo cáo đúng cấu trúc mục 5 của đề và quy định 2.3 (mã B10.1; phần "chạy lại một lệnh" của B10.1 do Phi).

## Đầu vào cần đọc
- `docs/CHECKLIST.md` (dòng B10.1), `docs/CONVENTIONS.md` mục 5, `docs/BAOCAO_DAN_Y.md`
- Ba file truy vết `docs/trace_*.md`

## Không được làm
- **AI không sinh đoạn báo cáo** (đề mục 7: cấm vô điều kiện). AI chỉ được sửa chính tả, diễn đạt (loại B, chỉ sửa chữ), dàn ý và đối chiếu số liệu (loại D); ghi `docs/ai_usage_log.md`.
- Không tự viết phần của Phi hoặc Việt: mỗi người tự viết phần khối mình (vấn đáp hỏi từng người). Việc của bạn là ghép, định dạng, kiểm nhất quán.
- Số liệu chỉ lấy từ tệp trong `results/`; không có kết quả thì ghi "chưa có", không bịa số.
- Không sửa file ngoài `files:`; thiếu thông tin thì ghi vào task và báo Phi.

## Xong khi
- Bảng Phụ lục D: mỗi hình, bảng trong báo cáo có một dòng (số | tệp | hàm hoặc ô | mã task) và tệp đó tồn tại trong `results/`.
- Báo cáo đúng cấu trúc mục 5 của đề; danh sách chỗ lệch (nếu có) gửi Phi.

## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
Tự kiểm hiểu (model hỏi): (mỗi hàm AI viết một dòng: `<hàm> | qua | <ngày>`; không có hàm AI viết thì ghi "không có")

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
