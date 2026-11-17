# AGENTS.md

Đọc **`TEAM.md`** trước và làm đúng theo đó (xác định người dùng, nhánh, file sở hữu, task, commit, PR, luật AI).

Ba điều không được quên:
1. Không tự đặt thông số, không đổi chữ ký hàm: lấy từ `src/config.py` và `docs/CONVENTIONS.md`; thiếu thì dừng và hỏi.
2. Phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + lan truyền ngược, PCA, LDA): được viết mã, nhưng người dùng phải hiểu từng dòng, Phi review trước khi merge, và phải ghi `docs/ai_usage_log.md`. Không viết nguyên đoạn báo cáo; không làm thay tính tay B7 và suy dẫn B2.2.
3. Không bịa số liệu; khi task xong nhắc người dùng ghi `docs/ai_usage_log.md` (mỗi loại việc một dòng, gộp mọi phiên của task).

Agent dùng sẵn: `.claude/agents/task-runner.md`, `reviewer.md`, `viva-coach.md` (bản dán cho công cụ khác: `prompts/`).
