# Nhật ký sử dụng AI (nguồn cho Phụ lục C của báo cáo)

**Cách ghi (giảm tối đa):** cuối mỗi task, trước khi đặt `status review`, mỗi **loại việc** đã dùng AI ghi MỘT dòng, gộp mọi phiên trong task đó. Không ghi từng câu hỏi. Chỉ thêm dòng, không sửa dòng của người khác. Khai báo trung thực không bị trừ điểm (đề mục 7).

| Mã | Loại | Phải ghi thêm |
|---|---|---|
| T | Tra cứu, giải thích khái niệm | không cần chi tiết (gộp cả tuần cũng được) |
| G | Gỡ lỗi, hỏi cách dùng hàm | tệp |
| M | AI viết hoặc sửa mã | **tên hàm** trong dấu `...` |
| B | Sửa chính tả, diễn đạt báo cáo (chỉ sửa chữ, không sinh đoạn mới) | mục báo cáo |
| D | Dàn ý, tài liệu hướng dẫn, đối chiếu số liệu, ôn vấn đáp | phần liên quan |
| R | Gợi ý tài liệu tham khảo | nguồn nhóm đã đọc |

Cột `Người` ghi `Phi`, `Huấn` hoặc `Việt`; cột `Task` ghi mã task (`T003`) hoặc `LEAD`. Kiểm định dạng: `python scripts\ai_log.py check`. Phi gộp thành bảng Phụ lục C: `python scripts\ai_log.py appendix`.

| Ngày | Công cụ | Loại | Việc | Tệp / phần báo cáo | Người | Task |
|---|---|---|---|---|---|---|
| 16/11/2026 | Claude Code (claude-opus-5-5, claude-sonnet-5-5) | M | Dựng khung repo: cấu hình, cổng chặn rò rỉ, stub giao diện, test, script tải dữ liệu, `run_all.py`, `TEAM.md`, `docs/CONVENTIONS.md`, README. Không cài đặt thuật toán lõi | `src/config.py`, `src/guards.py`, `src/*.py` (stub), `tests/`, `data/download_data.py`, `run_all.py`, `TEAM.md`, `docs/CONVENTIONS.md`, `README.md` | Phi | LEAD |
| 17/11/2026 | Claude Code, sub-agent Sonnet 5.5 | M | Chép yêu cầu đề, checklist, file nhiệm vụ từng người, hệ thống task, script `tasks.py`, agent và prompt | `docs/DE3.md`, `docs/CHECKLIST.md`, `docs/PHI.md`, `docs/HUAN.md`, `docs/VIET.md`, `tasks/`, `scripts/tasks.py`, `.claude/agents/`, `prompts/` | Phi | LEAD |
| 17/11/2026 | Antigravity (agy 1.5.9) | M | Viết script kiểm môi trường và test chặn số lạ | `scripts/doctor.py`, `tests/test_no_magic_numbers.py` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | M | CI, mẫu PR, CODEOWNERS | `.github/` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Nới luật AI về mã trong tài liệu hướng dẫn; dựng dàn ý Chương 1 và 2 (không viết đoạn báo cáo) | `TEAM.md`, `AGENTS.md`, `docs/`, `.claude/agents/`, `prompts/`, `tasks/`, `docs/BAOCAO_DAN_Y_C1_C2.md` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Ghi "ngưỡng hiểu" vào hướng dẫn review | `TEAM.md`, `docs/PHI.md`, `docs/decisions/README.md` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Chuyển bước kiểm hiểu sang model chủ động hỏi | `TEAM.md`, `docs/PHI.md`, `.claude/agents/`, `prompts/`, `tasks/_TEMPLATE.md`, `.github/` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Đổi định dạng nhật ký AI (6 loại, một dòng mỗi loại mỗi task), viết `scripts/ai_log.py` | `docs/ai_usage_log.md`, `scripts/ai_log.py`, `tests/test_ai_log.py` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Dựng dàn ý đầy đủ báo cáo (bìa đến phụ lục, không viết đoạn báo cáo) | `docs/BAOCAO_DAN_Y.md` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | M | Thêm hằng số quyết định và `get_run_seeds` | `src/config.py` (`get_run_seeds`), `tests/test_config_decisions.py` | Phi | LEAD |
| 17/11/2026 | Claude Code (claude-sonnet-5-5) | D | Ghi các quyết định vào quy ước, dàn ý, nhật ký quyết định | `docs/CONVENTIONS.md`, `docs/BAOCAO_DAN_Y.md`, `docs/decisions/README.md` | Phi | LEAD |
| 18/11/2026 | Claude Code (claude-sonnet-5-5) | M | Nạp dữ liệu, chia tuần, nhãn cao điểm, giờ phụ tải thấp, test | `src/data_prep.py` (`parse_raw`, `week_starts`, `split_weeks`, `peak_label`, `low_load_hours`, `drop_warmup`), `tests/test_data_prep.py`, `src/config.py` | Phi | T001 |
| 18/11/2026 | Claude Code (claude-sonnet-5-5) | D | Khảo sát dữ liệu thật, ghi chú dữ liệu và quy ước | `docs/CONVENTIONS.md`, `docs/decisions/README.md`, `tasks/T001-phi-nap-du-lieu-phu-tai-va-chia-tuan.md` | Phi | T001 |
| 18/11/2026 | Claude Code (claude-sonnet-5-5) | D | Thêm mục "Việc chính của từng người" vào README | `README.md` | Phi | LEAD |
| 18/11/2026 | Claude Code (claude-sonnet-5-5) | D | Chuyển phần báo cáo và hồ sơ sang Huấn trong các tài liệu phân công | `README.md`, `docs/CHECKLIST.md`, `docs/PHI.md`, `docs/HUAN.md`, `TEAM.md`, `scripts/tasks.py`, `tasks/T008-T010` | Phi | LEAD |
| 18/11/2026 | Claude Code (claude-sonnet-5-5) | M | Nạp CND, căn nhãn giờ, MAPE theo độ dịch trên val, test | `src/data_prep.py` (`load_cnd`, `align_cnd`, `cnd_mape`, `select_cnd_shift`), `tests/test_data_prep.py`, `src/config.py` | Phi | T002 |
| 21/11/2026 | Antigravity (Gemini 3.8 Flash) | D | Trích xuất siêu dữ liệu từ PDF, đối chiếu số liệu thống kê mô tả 17 biến | docs/DATA_DICTIONARY.md | Huấn | T004 |
| 22/11/2026 | Claude Code (claude-opus-5-5) | M | Viết PLA, Pocket, đếm lỗi; chạy thử trên dữ liệu tổng hợp | `src/perceptron.py` (`count_errors`, `pla`, `pocket`, `_check_inputs`, `_epoch_order`) | Việt | T006 |
| 22/11/2026 | Claude Code (claude-opus-5-5) | D | Hỏi kiểm hiểu `pla` (3 câu + sửa nhỏ), ôn vấn đáp B4.1 | `tasks/T006-viet-tu-cai-dat-pla-va-pocket.md` | Việt | T006 |
| 22/11/2026 | Claude Code (claude-opus-5-5) | M | Viết PCA và tiêu chí Fisher, test tính tay được trên dữ liệu tổng hợp | `src/features.py` (`pca`, `fisher_score`), `tests/test_features_viet.py` | Việt | T007 |
| 22/11/2026 | Claude Code (claude-opus-5-5) | D | Soạn câu hỏi ôn kiểm hiểu `pocket`, `count_errors`, `pca`, `fisher_score` (tài liệu ôn cá nhân, không nộp) | B4.1, B6.1, B6.3 | Việt | T007 |
| 22/11/2026 | Claude Code (claude-opus-5-5) | M | Thêm test đếm lỗi độc lập cho Pocket (bắt lỗi `count_errors` bỏ sót g = 0) | `tests/test_perceptron_viet.py` | Việt | T006 |
| 23/11/2026 | Antigravity (Gemini 3.8 Flash) | M | Cài đặt các hàm tối ưu tuyến tính, L2 loss, gradient và nghiệm đóng | `src/optim_linear.py` (`mse_l2_loss`, `mse_l2_grad`, `ridge_closed_form`, `finite_diff_check`, `gd`, `sgd`, `minibatch_gd`, `momentum_gd`), `tests/test_optim_linear_huan.py` | Huấn | T003 |
| 23/11/2026 | Antigravity (Gemini 3.8 Flash) | D | Hỏi kiểm hiểu gd, momentum, loss/grad (3 câu + sửa nhỏ), đối chiếu nghiệm giải tích | `tasks/T003-huan-tu-cai-dat-gd-sgd-mini-batch-va-nghiem-d.md` | Huấn | T003 |
