"""Script kiểm tra môi trường làm việc (Đề 3, Nhóm 18).

Chạy bằng: python scripts\\doctor.py
Chỉ dùng thư viện chuẩn ở mức import đầu file.
"""
from __future__ import annotations

import hashlib
import importlib
import os
from pathlib import Path
import subprocess
import sys

# Cấu hình mã hóa UTF-8 cho console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Thêm thư mục gốc của repository vào sys.path để import src.config
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def calc_sha256(path: Path) -> str:
    """Tính mã băm sha256 của tệp theo từng khối 64KB."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


class Doctor:
    """Bộ thu thập và in kết quả kiểm tra môi trường."""

    def __init__(self) -> None:
        self.passes = 0
        self.warnings = 0
        self.errors = 0

    def ok(self, msg: str) -> None:
        self.passes += 1
        print(f"[ĐẠT] {msg}")

    def warn(self, msg: str, hint: str) -> None:
        self.warnings += 1
        print(f"[CẢNH BÁO] {msg} -> Gợi ý: {hint}")

    def error(self, msg: str, hint: str) -> None:
        self.errors += 1
        print(f"[LỖI] {msg} -> Gợi ý: {hint}")


def check_python_version(doc: Doctor) -> None:
    """(a) Kiểm tra Python >= 3.10."""
    try:
        major, minor, micro = sys.version_info.major, sys.version_info.minor, sys.version_info.micro
        if sys.version_info >= (3, 10):
            doc.ok(f"Phiên bản Python hiện tại ({major}.{minor}.{micro}) >= 3.10")
        else:
            doc.error(
                f"Phiên bản Python hiện tại ({major}.{minor}.{micro}) < 3.10",
                "Cài đặt Python phiên bản >= 3.10 (khuyến nghị Python 3.12 theo TEAM.md)."
            )
    except Exception as e:
        doc.error(f"Lỗi khi kiểm tra phiên bản Python: {e}", "Kiểm tra lại cài đặt Python.")


def check_dependencies(doc: Doctor) -> None:
    """(b) Kiểm tra import được numpy, pandas, scipy, sklearn, matplotlib, pytest."""
    required_packages = ["numpy", "pandas", "scipy", "sklearn", "matplotlib", "pytest"]
    missing = []
    for pkg in required_packages:
        try:
            importlib.import_module(pkg)
        except Exception:
            missing.append(pkg)

    if missing:
        doc.error(
            f"Không thể import các thư viện: {', '.join(missing)}",
            "Chạy lệnh 'pip install -r requirements.txt' để cài đặt đầy đủ các gói phụ thuộc."
        )
    else:
        doc.ok(f"Đã import thành công các thư viện cốt lõi: {', '.join(required_packages)}")


def check_virtualenv(doc: Doctor) -> None:
    """(c) Kiểm tra đang dùng virtualenv (sys.prefix != sys.base_prefix)."""
    try:
        if sys.prefix != sys.base_prefix:
            doc.ok(f"Đang sử dụng môi trường ảo (virtualenv): {sys.prefix}")
        else:
            doc.warn(
                "Không phát hiện môi trường ảo (sys.prefix == sys.base_prefix)",
                "Kích hoạt môi trường ảo trước khi làm việc: .\\.venv\\Scripts\\Activate.ps1"
            )
    except Exception as e:
        doc.warn(f"Lỗi khi kiểm tra virtualenv: {e}", "Kiểm tra kích hoạt môi trường ảo.")


def check_git_branch(doc: Doctor) -> str | None:
    """(d) Kiểm tra git chạy được và nhánh hiện tại hợp lệ."""
    try:
        proc = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=ROOT,
            check=True
        )
        current_branch = proc.stdout.strip()
        valid_branches = {"main", "phi-lead-data-mlp", "huan-eda-gd", "viet-perceptron-features"}
        if current_branch == "main":
            doc.warn(
                "Nhánh hiện tại là 'main': đừng làm việc trực tiếp trên main",
                "Chuyển sang nhánh được phân công (git checkout phi-lead-data-mlp / huan-eda-gd / viet-perceptron-features)."
            )
        elif current_branch in valid_branches:
            doc.ok(f"Nhánh git hiện tại hợp lệ: '{current_branch}'")
        else:
            doc.error(
                f"Nhánh git hiện tại '{current_branch}' không hợp lệ (phải thuộc {valid_branches})",
                "Chuyển sang đúng nhánh được phân công theo TEAM.md mục 1."
            )
        return current_branch
    except Exception as e:
        doc.error(
            f"Lệnh git không chạy được hoặc gặp lỗi: {e}",
            "Cài đặt Git và đảm bảo git có trong biến môi trường PATH."
        )
        return None


def check_git_user_and_branch(doc: Doctor, current_branch: str | None) -> None:
    """(e) Kiểm tra git config user.name và sự khớp nối với nhánh hiện tại."""
    try:
        proc = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True,
            text=True,
            cwd=ROOT,
            check=True
        )
        user_name = proc.stdout.strip()
        branch_user_map = {
            "phi-lead-data-mlp": "Nguyen Bao Phi",
            "huan-eda-gd": "Do Minh Huan",
            "viet-perceptron-features": "Nguyen Serov Trong Viet",
        }
        allowed_users = set(branch_user_map.values())

        if user_name not in allowed_users:
            doc.error(
                f"git config user.name ('{user_name}') không thuộc danh sách thành viên hợp lệ",
                f"Chạy lệnh: git config user.name \"<Tên>\" với Tên thuộc: {', '.join(sorted(allowed_users))}."
            )
        else:
            if current_branch in branch_user_map:
                expected_user = branch_user_map[current_branch]
                if user_name != expected_user:
                    doc.error(
                        f"Nhánh '{current_branch}' không khớp với user.name '{user_name}' (kỳ vọng '{expected_user}')",
                        f"Chuyển sang đúng nhánh của bạn hoặc sửa git config user.name \"{expected_user}\"."
                    )
                else:
                    doc.ok(f"git config user.name ('{user_name}') khớp chính xác với nhánh '{current_branch}'")
            elif current_branch == "main":
                doc.ok(f"git config user.name ('{user_name}') hợp lệ (đang ở nhánh chung 'main')")
            else:
                doc.error(
                    f"Nhánh '{current_branch}' không xác định để đối chiếu với user.name '{user_name}'",
                    "Chuyển về đúng nhánh làm việc cá nhân của bạn theo TEAM.md."
                )
    except Exception as e:
        doc.error(
            f"Lỗi khi kiểm tra git config user.name: {e}",
            "Kiểm tra cấu hình git config user.name."
        )


def check_data_files(doc: Doctor) -> None:
    """(f) Kiểm tra tệp dữ liệu continuous, forecast và metadata_pdf."""
    try:
        from src.config import DATA_FILES, MENDELEY_URL
        for key in ("continuous", "forecast"):
            info = DATA_FILES[key]
            local_name = info["local_name"]
            dest = ROOT / "data" / "raw" / local_name
            dest_rel = f"data\\raw\\{local_name}"
            url = MENDELEY_URL.format(file_id=info["file_id"])
            download_hint = (
                f"Chạy 'python data\\download_data.py'. "
                f"Nếu gặp 403, tải bằng lệnh: curl -L -o \"{dest_rel}\" \"{url}\""
            )

            if not dest.exists():
                doc.error(f"Thiếu tệp dữ liệu '{dest_rel}'", download_hint)
            else:
                actual_size = dest.stat().st_size
                if actual_size != info["size"]:
                    doc.error(
                        f"Tệp dữ liệu '{dest_rel}' sai kích thước ({actual_size} bytes, kỳ vọng {info['size']})",
                        download_hint
                    )
                else:
                    actual_sha = calc_sha256(dest)
                    if actual_sha != info["sha256"]:
                        doc.error(
                            f"Tệp dữ liệu '{dest_rel}' sai sha256 ({actual_sha[:10]}..., kỳ vọng {info['sha256'][:10]}...)",
                            download_hint
                        )
                    else:
                        doc.ok(f"Tệp dữ liệu '{dest_rel}' hợp lệ (kích thước {info['size']} bytes, đúng sha256)")

        # Kiểm tra metadata_pdf (tùy chọn, chỉ cảnh báo nếu thiếu)
        pdf_info = DATA_FILES.get("metadata_pdf")
        if pdf_info:
            pdf_local = pdf_info["local_name"]
            pdf_dest = ROOT / "data" / "raw" / pdf_local
            pdf_dest_rel = f"data\\raw\\{pdf_local}"
            pdf_url = MENDELEY_URL.format(file_id=pdf_info["file_id"])
            pdf_hint = (
                f"Chạy 'python data\\download_data.py --with-pdf'. "
                f"Nếu gặp 403, tải bằng lệnh: curl -L -o \"{pdf_dest_rel}\" \"{pdf_url}\""
            )

            if not pdf_dest.exists():
                doc.warn(f"Thiếu tệp tài liệu tùy chọn '{pdf_dest_rel}'", pdf_hint)
            elif pdf_dest.stat().st_size != pdf_info["size"] or calc_sha256(pdf_dest) != pdf_info["sha256"]:
                doc.warn(f"Tệp tùy chọn '{pdf_dest_rel}' sai kích thước hoặc sha256", pdf_hint)
            else:
                doc.ok(f"Tệp tài liệu tùy chọn '{pdf_dest_rel}' hợp lệ")
    except Exception as e:
        doc.error(f"Lỗi khi kiểm tra dữ liệu từ src.config: {e}", "Kiểm tra file src/config.py.")


def check_seed(doc: Doctor) -> None:
    """(g) Kiểm tra src.config.get_seed() trả về 2044."""
    try:
        from src.config import get_seed
        seed = get_seed()
        if seed == 2044:
            doc.ok("src.config.get_seed() = 2044 hợp lệ")
        else:
            doc.error(
                f"src.config.get_seed() trả về {seed} (kỳ vọng 2044)",
                "Đặt biến môi trường BCCD_G=18 hoặc sửa GROUP_ID trong src/config.py thành 18."
            )
    except Exception as e:
        doc.error(f"Lỗi khi gọi src.config.get_seed(): {e}", "Kiểm tra hàm get_seed trong src/config.py.")


def check_large_untracked_files(doc: Doctor) -> None:
    """(h) Kiểm tra git status --porcelain có tệp > 1 MB chưa bị ignore thì cảnh báo."""
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=ROOT,
            check=True
        )
        large_files = []
        for raw_line in proc.stdout.splitlines():
            line = raw_line.strip()
            if not line or len(line) < 3:
                continue
            filepath_part = line[2:].strip()
            if " -> " in filepath_part:
                filepath_part = filepath_part.split(" -> ")[1].strip()
            if filepath_part.startswith('"') and filepath_part.endswith('"'):
                filepath_part = filepath_part[1:-1]
            target_path = ROOT / filepath_part
            try:
                if target_path.is_file():
                    file_size = target_path.stat().st_size
                    if file_size > 1024 * 1024:
                        mb_size = file_size / (1024 * 1024)
                        large_files.append(f"{filepath_part} ({mb_size:.2f} MB)")
            except OSError:
                pass

        if large_files:
            doc.warn(
                f"Phát hiện tệp > 1 MB chưa bị ignore trong git status: {', '.join(large_files)}",
                "Thêm các tệp này vào .gitignore để tránh commit nhầm dữ liệu lớn (TEAM.md mục 9)."
            )
        else:
            doc.ok("Không có tệp nào > 1 MB chưa bị ignore trong git status")
    except Exception as e:
        doc.warn(f"Không thể kiểm tra tệp lớn qua git status: {e}", "Kiểm tra trạng thái git repo.")


def print_summary(doc: Doctor) -> int:
    """(i) In dòng tổng kết cuối và trả về mã thoát (1 nếu có lỗi, 0 nếu không có lỗi)."""
    print("=" * 60)
    print(f"Tổng kết kiểm tra: {doc.passes} [ĐẠT], {doc.warnings} [CẢNH BÁO], {doc.errors} [LỖI]")
    if doc.errors > 0:
        print("Kết luận: Môi trường làm việc CHƯA ĐẠT. Vui lòng khắc phục các mục [LỖI] ở trên.")
        return 1
    if doc.warnings > 0:
        print("Kết luận: Môi trường làm việc ĐẠT (kèm các cảnh báo cần lưu ý).")
        return 0
    print("Kết luận: Môi trường làm việc hoàn toàn ĐẠT yêu cầu.")
    return 0


def main() -> None:
    doc = Doctor()
    print("Bắt đầu kiểm tra môi trường làm việc (scripts/doctor.py)...")
    print("-" * 60)

    # (a) Python >= 3.10
    check_python_version(doc)

    # (b) Thư viện cốt lõi
    check_dependencies(doc)

    # (c) Virtualenv
    check_virtualenv(doc)

    # (d) Git branch
    current_branch = check_git_branch(doc)

    # (e) Git user.name và branch
    check_git_user_and_branch(doc, current_branch)

    # (f) Dữ liệu raw
    check_data_files(doc)

    # (g) Hạt giống ngẫu nhiên SEED
    check_seed(doc)

    # (h) Tệp lớn chưa ignore
    check_large_untracked_files(doc)

    # (i) Tổng kết
    exit_code = print_summary(doc)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
