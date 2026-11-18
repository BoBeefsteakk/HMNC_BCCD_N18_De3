---
id: T008
title: Báo cáo tiến độ 2–3 trang
phase: P2
checklist: TĐ
owner: huan
status: todo
due: 27/11/2026
files: docs/BAOCAO_DAN_Y.md,docs/trace_huan.md
depends: T003,T005,T006
---
# T008 — Báo cáo tiến độ 2–3 trang

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Soạn báo cáo tiến độ 2–3 trang (mã TĐ): kết quả EDA, cách chia dữ liệu, kết quả ban đầu của GD và perceptron, kế hoạch phần còn lại. Không nộp là bị trừ 0,5 điểm.

## Đầu vào cần đọc
- `TEAM.md`, `docs/HUAN.md`, `docs/CONVENTIONS.md`, `docs/CHECKLIST.md` (dòng TĐ)
- `docs/BAOCAO_DAN_Y.md` (mục "Báo cáo tiến độ")
- Kết quả của T001, T003, T005, T006 (xin từng người; đây là phần của họ viết)

## Không được làm
- **AI không sinh đoạn báo cáo** (đề mục 7: cấm vô điều kiện). AI chỉ được sửa chính tả, diễn đạt (loại B, chỉ sửa chữ), dàn ý và đối chiếu số liệu (loại D); ghi `docs/ai_usage_log.md`.
- Không tự viết phần của Phi hoặc Việt: mỗi người tự viết phần khối mình (vấn đáp hỏi từng người). Việc của bạn là ghép, định dạng, kiểm nhất quán.
- Số liệu chỉ lấy từ tệp trong `results/`; không có kết quả thì ghi "chưa có", không bịa số.
- Không sửa file ngoài `files:`; thiếu thông tin thì ghi vào task và báo Phi.

## Xong khi
- Bản nháp 2–3 trang gửi Phi duyệt trước **28/11/2026**; nộp trước **30/11/2026** (nơi nộp theo thông báo của giảng viên).
- Đủ 4 ý đề yêu cầu; mỗi người đã tự viết phần khối mình, bạn chỉ ghép và định dạng.
- Mọi con số đều có trong `results/` hoặc ghi rõ "chưa có".

## Tôi giải thích được
- ☐ Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
Tự kiểm hiểu (model hỏi): (mỗi hàm AI viết một dòng: `<hàm> | qua | <ngày>`; không có hàm AI viết thì ghi "không có")

## Ghi chú AI đã dùng
Nếu dùng AI: ghi vào `docs/ai_usage_log.md` mỗi loại việc một dòng, gộp mọi phiên của task (loại T/G/M/B/D/R, xem đầu file; việc M ghi tên hàm). Không dùng AI thì ghi "không".
