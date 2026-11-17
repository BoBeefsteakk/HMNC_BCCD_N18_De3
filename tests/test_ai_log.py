"""Kiểm scripts/ai_log.py và định dạng thật của docs/ai_usage_log.md."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import ai_log  # noqa: E402

HEAD = "| Ngày | Công cụ | Loại | Việc | Tệp / phần báo cáo | Người | Task |\n|---|---|---|---|---|---|---|\n"


def test_real_log_is_valid():
    text = (ROOT / "docs" / "ai_usage_log.md").read_text(encoding="utf-8")
    assert ai_log.check(text) == []


def test_bad_rows_are_caught():
    bad = HEAD + "| 1/1 | X | Z | viec | `a.py` | Phi | T001 |\n| 1/1 | X | M | viec | a.py | Bob | T001 |\n| 1/1 | X |\n"
    errors = ai_log.check(bad)
    assert any("Loại 'Z'" in e for e in errors)
    assert any("Người 'Bob'" in e for e in errors)
    assert any("tên hàm" in e for e in errors)
    assert any("có 2 ô" in e for e in errors)


def test_appendix_merges_same_person_tool_kind():
    ok = HEAD + (
        "| 1/1 | Claude | M | viết `gd` | `src/optim_linear.py` (`gd`) | Huấn | T003 |\n"
        "| 2/1 | Claude | M | viết `sgd` | `src/optim_linear.py` (`sgd`) | Huấn | T003 |\n"
        "| 2/1 | Claude | B | sửa diễn đạt | Chương 1.1 | Huấn | T005 |\n"
    )
    assert ai_log.check(ok) == []
    table = ai_log.appendix(ok)
    body = [l for l in table.splitlines() if l.startswith("| ") and not l.startswith("| STT")]
    assert len(body) == 2  # hai dòng M gộp thành một, một dòng B
