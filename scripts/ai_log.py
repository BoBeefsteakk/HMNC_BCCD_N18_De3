"""Nhật ký AI: kiểm định dạng và gộp thành bảng Phụ lục C (chỉ dùng thư viện chuẩn).

    python scripts\\ai_log.py check       # kiểm định dạng bảng trong docs/ai_usage_log.md
    python scripts\\ai_log.py appendix    # in bảng Phụ lục C (gộp theo người, công cụ, loại)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / "docs" / "ai_usage_log.md"

COLUMNS = ["Ngày", "Công cụ", "Loại", "Việc", "Tệp / phần báo cáo", "Người", "Task"]
KINDS = {
    "T": "Tra cứu, giải thích khái niệm",
    "G": "Gỡ lỗi, hỏi cách dùng hàm",
    "M": "AI viết hoặc sửa mã",
    "B": "Sửa chính tả, diễn đạt báo cáo (chỉ sửa chữ)",
    "D": "Dàn ý, tài liệu hướng dẫn, đối chiếu số liệu, ôn vấn đáp",
    "R": "Gợi ý tài liệu tham khảo",
}
PEOPLE = {"Phi", "Huấn", "Việt"}
PAGE_LIMIT_ROWS = 15  # Phụ lục C dài 1 trang (đề, mục 5); ước lượng số dòng vừa một trang


def parse_rows(text: str) -> list[tuple[int, list[str]]]:
    """Trả về (số dòng, các ô) cho mọi dòng dữ liệu của bảng đầu tiên có đủ tiêu đề."""
    rows: list[tuple[int, list[str]]] = []
    in_table = False
    for no, line in enumerate(text.splitlines(), start=1):
        s = line.strip()
        if not s.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not in_table:
            if cells and cells[0] == COLUMNS[0]:
                in_table = True
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue  # dòng phân cách |---|---|
        rows.append((no, cells))
    return rows


def check(text: str) -> list[str]:
    errors: list[str] = []
    header_ok = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.strip("|").split("|")[0].strip() == COLUMNS[0]:
            header_cells = [c.strip() for c in s.strip("|").split("|")]
            header_ok = len(header_cells) == len(COLUMNS)
            break
    if not header_ok:
        errors.append(f"Tiêu đề bảng phải có đúng {len(COLUMNS)} cột: {' | '.join(COLUMNS)}")
        return errors
    for no, cells in parse_rows(text):
        if len(cells) != len(COLUMNS):
            errors.append(f"Dòng {no}: có {len(cells)} ô, cần {len(COLUMNS)} ({' | '.join(COLUMNS)})")
            continue
        row = dict(zip(COLUMNS, cells))
        if row["Loại"] not in KINDS:
            errors.append(f"Dòng {no}: Loại '{row['Loại']}' không hợp lệ, chọn một trong {', '.join(KINDS)}")
        if row["Người"] not in PEOPLE:
            errors.append(f"Dòng {no}: Người '{row['Người']}' không hợp lệ, chọn một trong {', '.join(sorted(PEOPLE))}")
        for k in ("Ngày", "Công cụ", "Việc", "Tệp / phần báo cáo", "Task"):
            if not row[k]:
                errors.append(f"Dòng {no}: ô '{k}' đang trống")
        if row["Loại"] == "M" and "`" not in row["Tệp / phần báo cáo"]:
            errors.append(f"Dòng {no}: loại M phải ghi tệp và tên hàm trong dấu `...`")
    return errors


def appendix(text: str) -> str:
    groups: dict[tuple[str, str, str], dict[str, list[str]]] = {}
    for _, cells in parse_rows(text):
        if len(cells) != len(COLUMNS):
            continue
        row = dict(zip(COLUMNS, cells))
        key = (row["Người"], row["Công cụ"], row["Loại"])
        g = groups.setdefault(key, {"viec": [], "tep": []})
        if row["Việc"] not in g["viec"]:
            g["viec"].append(row["Việc"])
        if row["Tệp / phần báo cáo"] not in g["tep"]:
            g["tep"].append(row["Tệp / phần báo cáo"])
    out = [
        "| STT | Công cụ (tên, phiên bản) | Mục đích sử dụng | Phần báo cáo hoặc tệp mã liên quan | Nội dung yêu cầu chính (tóm tắt) | Người dùng |",
        "|---|---|---|---|---|---|",
    ]
    for i, ((person, tool, kind), g) in enumerate(sorted(groups.items()), start=1):
        out.append(f"| {i} | {tool} | {KINDS.get(kind, kind)} | {'; '.join(g['tep'])} | {'; '.join(g['viec'])} | {person} |")
    out.append("")
    out.append("Nhóm cam kết nội dung khai báo trên là trung thực; mọi thành viên hiểu và giải thích được toàn bộ báo cáo và mã nguồn nộp kèm.")
    if len(groups) > PAGE_LIMIT_ROWS:
        out.append("")
        out.append(f"CẢNH BÁO: {len(groups)} dòng, có thể vượt 1 trang của Phụ lục C; gộp bớt các dòng gần nhau.")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "appendix"])
    ap.add_argument("--file", default=str(LOG_PATH))
    args = ap.parse_args(argv)
    text = Path(args.file).read_text(encoding="utf-8")
    errors = check(text)
    if args.cmd == "check":
        if errors:
            print("\n".join(errors))
            return 1
        print(f"Nhật ký AI hợp lệ: {len(parse_rows(text))} dòng.")
        return 0
    if errors:
        print("Nhật ký còn lỗi, sửa trước khi gộp:\n" + "\n".join(errors))
        return 1
    print(appendix(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
