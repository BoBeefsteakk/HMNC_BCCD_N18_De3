# Nhật ký sử dụng AI (nguồn cho Phụ lục C của báo cáo)

Mỗi lần dùng AI thêm MỘT dòng ở cuối bảng (chỉ thêm, không sửa dòng của người khác). Khai báo trung thực không bị trừ điểm (đề mục 7).

| Ngày | Công cụ (tên, phiên bản) | Việc | Tệp / phần báo cáo | Người |
|---|---|---|---|---|
| 16/11/2026 | Claude Code (claude-opus-5-5, claude-sonnet-5-5) | Dựng khung repo: cấu hình, cổng chặn rò rỉ, stub giao diện, test, script tải dữ liệu, `run_all.py`, `TEAM.md`, `docs/CONVENTIONS.md`, README. Không cài đặt thuật toán lõi | `src/config.py`, `src/guards.py`, `src/*.py` (stub), `tests/`, `data/download_data.py`, `run_all.py`, `TEAM.md`, `docs/CONVENTIONS.md`, `README.md` | Phi |
| 17/11/2026 | Claude Code, sub-agent Sonnet 5.5 | Chép yêu cầu đề, checklist, file nhiệm vụ từng người, hệ thống task, script `tasks.py`, agent và prompt | `docs/DE3.md`, `docs/CHECKLIST.md`, `docs/PHI.md`, `docs/HUAN.md`, `docs/VIET.md`, `tasks/`, `scripts/tasks.py`, `.claude/agents/`, `prompts/` | Phi |
| 17/11/2026 | Antigravity (agy 1.5.9) | Viết script kiểm môi trường và test chặn số lạ | `scripts/doctor.py`, `tests/test_no_magic_numbers.py` | Phi |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | CI, mẫu PR, CODEOWNERS | `.github/` | Phi |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | Nới luật AI về mã trong tài liệu hướng dẫn; dựng dàn ý Chương 1 và 2 (không viết đoạn báo cáo) | `TEAM.md`, `AGENTS.md`, `docs/`, `.claude/agents/`, `prompts/`, `tasks/`, `docs/BAOCAO_DAN_Y_C1_C2.md` | Phi |
