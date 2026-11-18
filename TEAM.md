# TEAM.md — ĐỌC FILE NÀY TRƯỚC KHI LÀM BẤT CỨ VIỆC GÌ

Dành cho mọi thành viên VÀ mọi AI (Claude, ChatGPT, Antigravity, ...).
**AI: làm đúng các bước dưới đây. Không tự đặt quy tắc khác. Không chắc thì DỪNG và hỏi người dùng.**

Dự án: báo cáo chuyên đề Học máy nâng cao, **Đề 3 – dự báo phụ tải điện Panama theo giờ cho tuần tới**. Nhóm 18, SEED = 2044.

## 1. Xác định người đang làm việc
Chạy `git config user.name` rồi đối chiếu bảng. Không khớp ai → hỏi người dùng "Bạn là Phi, Huấn hay Việt?" trước khi làm tiếp.

| Người | `git config user.name` | Vai trò | GitHub | Nhánh DUY NHẤT được dùng | Đọc file nhiệm vụ |
|---|---|---|---|---|---|
| Nguyễn Bảo Phi | `Nguyen Bao Phi` | Trưởng nhóm: giao task, review, merge; dữ liệu, MLP, đánh giá | `BoBeefsteakk` | `phi-lead-data-mlp` | `docs/PHI.md` |
| Đỗ Minh Huấn | `Do Minh Huan` | Thành viên: EDA, GD/SGD/momentum, so sánh với CND | `minhhuan15082k5-sudo` | `huan-eda-gd` | `docs/HUAN.md` |
| Nguyễn Serov Trọng Việt | `Nguyen Serov Trong Viet` | Thành viên: perceptron, đặc trưng, PCA/LDA | `viet29oct` | `viet-perceptron-features` | `docs/VIET.md` |

Nhánh chung: `main` (chỉ nhận PR, chỉ Phi merge). **Chỉ có đúng 4 nhánh này.**

## 2. Bộ file phải biết (đọc theo thứ tự)
1. `TEAM.md` (file này) → 2. file nhiệm vụ của bạn (`docs/<TÊN>.md`) → 3. `tasks/README.md` + file task được giao → 4. `docs/CONVENTIONS.md` → 5. `docs/CHECKLIST.md` (việc cố định theo phase) → 6. `docs/DE3.md` (yêu cầu gốc của đề, chỉ để tra cứu).

Mỗi loại thông tin chỉ có MỘT chỗ:

| Loại | Ở đâu | Ai được sửa |
|---|---|---|
| Thông số (SEED, ngày chia, độ trễ, phân vị, tên cột, đường dẫn) | `src/config.py` | Chỉ Phi |
| Quy ước (công thức, nhãn, tên tệp, giao diện hàm) | `docs/CONVENTIONS.md` | Chỉ Phi |
| Checklist theo phase | `docs/CHECKLIST.md` | Chỉ Phi |
| Task hằng ngày | `tasks/Txxx-*.md` | Phi tạo; người được giao cập nhật `status` và "Kết quả" |
| Luật cho AI | `TEAM.md`, `AGENTS.md` | Chỉ Phi |

## 3. File sở hữu (mỗi file một chủ)
| Người | Được sửa |
|---|---|
| Phi | `src/config.py`, `src/data_prep.py`, `src/mlp.py`, `src/evaluate.py`, `src/hand_calc.py`, `run_all.py`, `docs/` (trừ file task và `ai_usage_log.md`), `tasks/` (tạo task), `.github/`, `.claude/`, `prompts/`, `scripts/`, `TEAM.md`, `AGENTS.md` |
| Huấn | `src/optim_linear.py`, `src/hand_calc_huan.py`, `src/cnd_compare.py`, `notebooks/huan_*`, `docs/DATA_DICTIONARY.md`, `docs/BAOCAO_DAN_Y.md` (dàn ý báo cáo) |
| Việt | `src/perceptron.py`, `src/features.py`, `src/hand_calc_viet.py`, `notebooks/viet_*` |
| Ai cũng được | file task của mình, `docs/trace_<tên>.md` của mình, `docs/ai_usage_log.md` (chỉ thêm dòng), `results/figures|tables/` (chỉ tệp do mã của mình sinh ra, tên theo `CONVENTIONS.md`), `tests/` của khối mình |

Cần sửa file của người khác → ghi vào task, nhắn chủ file. Không tự sửa.

## 4. Bắt đầu mỗi buổi làm (bắt buộc, đúng thứ tự; PowerShell)
```powershell
cd "D:\uni\Machine Learning\HMNC_BCCD_N18_De3"     # hoặc nơi bạn clone
.\.venv\Scripts\Activate.ps1
git checkout <nhánh-của-bạn>
git pull origin <nhánh-của-bạn>
git fetch origin
git merge origin/main
python scripts\doctor.py
```
- `doctor.py` báo LỖI thì sửa theo hướng dẫn nó in ra trước khi làm việc.
- Merge `origin/main` bị xung đột → **DỪNG**. File không thuộc quyền của bạn thì lấy bản của `main`. Còn lại báo Phi. AI không tự giải quyết xung đột.
- Ngày đầu tiên: `git clone` repo, `git checkout <nhánh-của-bạn>`, `python -m venv .venv`, kích hoạt, `pip install -r requirements.txt`, `$env:PYTHONUTF8=1`, `git config user.name "<tên ở bảng mục 1>"`, tải dữ liệu theo `README.md`.

## 5. Nhận và làm task
1. Mở `tasks/README.md`, tìm task có `owner` là bạn và `status: todo` (ưu tiên theo hạn).
2. Đọc file task. **Chỉ sửa các file ghi ở dòng `files:`.**
3. Đổi `status: doing`. Làm xong → `status: review` và điền mục "Kết quả".
4. Thông số lấy từ `src/config.py`. Thiếu thông số → KHÔNG tự đặt, ghi vào task và báo Phi.
5. Phần lõi (mục 8): AI được viết mã, nhưng bạn phải hiểu và tự giải thích được từng dòng.

## 6. Commit và push
- Mẫu commit: `T003 feat(b3): them momentum gd`
  - `T003` = mã task; Phi dùng `LEAD` cho việc quản trị.
  - loại: `feat` | `fix` | `test` | `docs` | `chore`
  - phạm vi: `b1`…`b10`, `r1`…`r4`, `report`
- Trước khi commit: `python -m pytest` không được có test ĐỎ (SKIP thì được).
- Lệnh git ĐƯỢC PHÉP: `status`, `diff`, `log`, `add <tệp cụ thể>`, `commit`, `pull origin <nhánh-của-bạn>`, `fetch`, `merge origin/main`, `checkout <nhánh-của-bạn>`, `push origin <nhánh-của-bạn>`.
- Lệnh git CẤM: `reset --hard`, `push --force`/`-f`, `rebase`, `checkout -- .`, `clean -f`, `branch -D`, `commit --amend` sau khi đã push, `add .` / `add -A` (tránh thêm nhầm tệp), mọi lệnh đụng nhánh của người khác.

## 7. Pull Request
- Mỗi người có MỘT PR thường trực `<nhánh-của-bạn> → main`. Đã có thì chỉ push thêm.
- Tiêu đề: `[huan-eda-gd] T003 T004` (liệt kê mã task trong PR). Điền đủ mẫu PR.
- Reviewer là Phi. **Chỉ Phi merge** (merge commit, không squash).
- Review chỉ được HỎI và GỢI Ý công thức; **không dán code mẫu cho người khác chép** (để người nộp tự hiểu và tự sửa, bảo vệ điểm vấn đáp).
- Sau khi Phi báo "đã merge", mọi người làm lại mục 4.

## 8. Luật AI (theo đề, mục 7)
- ĐƯỢC: tra khái niệm; hỏi cách dùng hàm thư viện; tìm lỗi, gỡ lỗi; sửa chính tả, diễn đạt; dựng dàn ý báo cáo; đặt câu hỏi ôn vấn đáp; gợi ý tài liệu tham khảo để nhóm đọc; viết mã sinh bảng, hình (con số lên báo cáo chỉ lấy từ `results/` do mã chạy ra).
- ĐƯỢC (quyết định của trưởng nhóm, 17/11/2026): **AI viết hoặc sửa mã, kể cả phần bắt buộc tự cài đặt** (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + lan truyền ngược + kiểm tra gradient, PCA, LDA), với 3 điều kiện: (1) người nộp giải thích được từng dòng (vấn đáp có thể bắt chạy lại, đổi tham số); (2) Phi review trước khi merge và task có dòng "Tự kiểm hiểu: qua" (ngưỡng hiểu bên dưới); (3) ghi dòng vào `docs/ai_usage_log.md` để khai ở Phụ lục C.
- **Ngưỡng hiểu bắt buộc** cho mỗi hàm do AI viết trong phần tự cài đặt: **model chủ động hỏi**, không chờ Phi. Trước khi đặt `status review`, model (task-runner) hỏi người nộp 3 câu về hàm đó (trả lời bằng lời mình, không mở AI) và yêu cầu tự sửa một chỗ nhỏ rồi giải thích kết quả; `qua` thì ghi một dòng `Tự kiểm hiểu (model hỏi): <hàm> | qua | <ngày>` vào "Kết quả" của task. Chưa qua thì chưa nộp. Phi chỉ kiểm dòng này có mặt, không phải hỏi từng người; muốn thì Phi hỏi xen kẽ vài hàm. Đây là kiểm tự giác (không chứng minh được người nộp không hỏi AI khác), nhưng người chịu trách nhiệm khi vấn đáp là chính họ.
- KHÔNG ĐƯỢC: sinh nguyên đoạn báo cáo (đề mục 7 cấm thẳng; chỉ được dàn ý, sửa chính tả, diễn đạt); để AI làm thay phần tính tay B7 và suy dẫn B2.2 (đề yêu cầu nhóm tự tính, tự viết); tạo số liệu/bảng/hình không do mã của nhóm chạy ra; đưa vào báo cáo tài liệu chưa đọc hoặc chưa kiểm tra là tồn tại thật.
- Rủi ro đã biết: mục 2.4 của đề yêu cầu "tự cài đặt" và chỉ cấm nộp mã AI sinh "khi chưa hiểu". Nếu giảng viên hiểu chặt hơn, phần mã do AI viết có thể bị xem là vi phạm. Phi biết và chấp nhận; mọi lần AI viết mã phải có trong nhật ký.
- **Nhật ký AI** (`docs/ai_usage_log.md`): cuối mỗi task (trước `review`), mỗi loại việc AI đã dùng ghi MỘT dòng (gộp mọi phiên của task; 7 cột và 6 loại T/G/M/B/D/R xem đầu file; việc M ghi tên hàm). Khai báo trung thực không bị trừ điểm. Phi gộp thành Phụ lục C bằng `python scripts\ai_log.py appendix`.
- Mọi thành viên phải giải thích được mọi dòng mã tự cài đặt và mọi con số trong báo cáo, kể cả phần người khác làm (vấn đáp hỏi chéo).

## 9. Điều CẤM khác (người và AI)
- Tạo nhánh khác ngoài 4 nhánh; push thẳng `main`; push lên nhánh người khác.
- Sửa file ngoài danh sách sở hữu (mục 3) hoặc ngoài `files:` của task.
- Viết thông số thẳng vào code thay vì lấy từ `src/config.py` (có test chặn).
- Đọc nhãn tập kiểm tra khi chưa được Phi cho phép: chỉ `python run_all.py --final` do Phi chạy, một lần.
- Commit dữ liệu thô, `.venv/`, tệp > 1 MB, notebook còn output.
- Đổi tên hàm hoặc chữ ký đã nêu trong stub của `src/` và `docs/CONVENTIONS.md`.

## 10. Lệnh thường dùng (PowerShell)
```powershell
python scripts\doctor.py            # kiểm môi trường
python -m pytest                    # chạy test
python scripts\tasks.py list        # xem task
python scripts\tasks.py list --owner huan
python run_all.py                   # chạy các stage (phát triển, không chạm tập kiểm tra)
```

## 11. Công cụ AI
Dùng công cụ nào cũng được. Claude Code đọc `CLAUDE.md`, Antigravity đọc `GEMINI.md`/`AGENTS.md`; cả hai chỉ trỏ về file này. ChatGPT / Claude web: dán `prompts/START.md` + file task vào đầu cuộc chat. Agent dùng sẵn: `.claude/agents/` (task-runner, reviewer, viva-coach), bản dán tương ứng trong `prompts/`.
