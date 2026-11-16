"""Chạy lại toàn bộ kết quả bằng MỘT lệnh (đề B10.1, Phụ lục 2).

    python run_all.py            # phát triển: chỉ dùng train/val; stage chưa cài đặt in [TODO] và bỏ qua
    python run_all.py --final    # chạy cuối: mở tập kiểm tra ĐÚNG MỘT LẦN (src/guards.py); thiếu stage -> exit 1

Hạt giống: SEED = 2026 + G (src/config.py). Mỗi stage là một module trong src/ có hàm run(seed, final).
"""
from __future__ import annotations

import argparse
import importlib
import sys
import time

if hasattr(sys.stdout, "reconfigure"):  # console Windows mặc định cp1252 sẽ lỗi khi in tiếng Việt
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

STAGES = ["data_prep", "features", "optim_linear", "perceptron", "mlp", "evaluate", "hand_calc"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=None, help="mặc định: 2026 + G từ src/config.py")
    ap.add_argument("--final", action="store_true", help="chạy cuối cùng, mở tập kiểm tra một lần")
    ap.add_argument("--only", choices=STAGES, help="chỉ chạy một stage")
    args = ap.parse_args()

    from src import config

    try:
        seed = args.seed if args.seed is not None else config.get_seed()
    except RuntimeError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        return 2
    todo, t0 = [], time.time()
    for name in [args.only] if args.only else STAGES:
        mod = importlib.import_module(f"src.{name}")
        t = time.time()
        try:
            mod.run(seed=seed, final=args.final)
            print(f"[ok]   {name} ({time.time() - t:.1f}s)")
        except NotImplementedError:
            todo.append(name)
            print(f"[TODO] {name}: chưa cài đặt")
    print(f"Tổng {time.time() - t0:.1f}s (giới hạn đề: 60 phút). Chưa cài đặt: {todo or 'không'}")
    return 1 if (todo and args.final) else 0


if __name__ == "__main__":
    sys.exit(main())
