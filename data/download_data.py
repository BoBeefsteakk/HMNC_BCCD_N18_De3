"""Tải dữ liệu Đề 3 từ Mendeley Data (không cần đăng nhập), in kích thước + SHA-256 và so với giá trị mong đợi.

Dùng:  python data/download_data.py [--with-pdf] [--force]
Nguồn: https://data.mendeley.com/datasets/byx7sztj59/1  (doi:10.17632/byx7sztj59.1, CC BY 4.0) — tài liệu [8].
Dữ liệu ghi vào data/raw/ (đã .gitignore; KHÔNG nộp kèm dữ liệu gốc — đề mục 2.2).
Chỉ dùng thư viện chuẩn để chạy được trước cả khi cài requirements.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # console Windows mặc định cp1252 sẽ lỗi khi in tiếng Việt
    sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config import DATA_FILES, MENDELEY_URL, RAW_DIR  # noqa: E402


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-pdf", action="store_true", help="tải thêm PDF mô tả cột (tham khảo cho từ điển dữ liệu B1.2)")
    ap.add_argument("--force", action="store_true", help="tải lại dù đã có tệp đúng")
    args = ap.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    keys = ["continuous", "forecast"] + (["metadata_pdf"] if args.with_pdf else [])
    ok = True
    print(f"Ngày tải: {date.today().isoformat()}")
    for k in keys:
        meta = DATA_FILES[k]
        dest = RAW_DIR / meta["local_name"]
        if dest.exists() and not args.force and sha256_of(dest) == meta["sha256"]:
            print(f"[có sẵn] {dest.name}")
        else:
            url = MENDELEY_URL.format(file_id=meta["file_id"])
            print(f"[tải]    {meta['remote_name']}  <-  {url}")
            try:
                urllib.request.urlretrieve(url, dest)
            except urllib.error.HTTPError as e:
                # Một số máy/mạng bị Mendeley từ chối client Python (HTTP 403). Không né chặn: hướng dẫn tải tay.
                print(f"         Không tải tự động được (HTTP {e.code}). Tải tay bằng trình duyệt hoặc curl:")
                print(f"           curl -L -o \"{dest}\" \"{url}\"")
                print(f"         rồi chạy lại script này để kiểm tra kích thước và SHA-256.")
                ok = False
                continue
        size, digest = dest.stat().st_size, sha256_of(dest)
        good = size == meta["size"] and digest == meta["sha256"]
        ok &= good
        print(f"         {dest.name}: {size:,} byte, sha256={digest} -> {'ĐÚNG' if good else 'SAI so với giá trị mong đợi'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
