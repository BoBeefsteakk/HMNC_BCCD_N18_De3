"""Cấu trúc nộp bài theo Phụ lục 2 của đề: thiếu thành phần nào thì test đỏ."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    "run_all.py",
    "data/download_data.py",
    "src/data_prep.py",
    "src/features.py",
    "src/optim_linear.py",
    "src/perceptron.py",
    "src/mlp.py",
    "src/evaluate.py",
    "src/hand_calc.py",
]
REQUIRED_DIRS = ["notebooks", "results/figures", "results/tables"]


def test_required_files_exist():
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    assert not missing, f"Thiếu tệp theo Phụ lục 2: {missing}"


def test_required_dirs_exist():
    missing = [p for p in REQUIRED_DIRS if not (ROOT / p).is_dir()]
    assert not missing, f"Thiếu thư mục theo Phụ lục 2: {missing}"


def test_raw_data_is_not_tracked():
    """Đề mục 2.2: không nộp kèm dữ liệu gốc."""
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "data/raw/" in gi
