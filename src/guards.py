"""Hai "cổng chặn" chống lỗi mà đề trừ điểm nặng (đề mục 3.1d, 4.4 R1, 6.4).

1. Quy tắc 72 giờ: dự báo cho tuần tới (Thứ Bảy 00:00 -> Thứ Sáu 23:00) chỉ được dùng phụ tải đến hết
   Thứ Ba trước đó. Dùng `lag_violations` để lập bảng "đặc trưng – độ trễ nhỏ nhất – vì sao hợp lệ" (R1).
2. Tập kiểm tra chỉ dùng MỘT lần: `open_test_set(final=True)`.

Quy ước thời gian (đã kiểm ở T001/T002, xem docs/CONVENTIONS.md mục 1): ta tính theo mốc "giờ bắt đầu"; nhãn gốc của tệp là giờ kết thúc.
Nếu nhãn thời gian trong tệp là "giờ kết thúc", ngưỡng đúng là 239 giờ; dùng 240 là an toàn cho cả hai
cách hiểu, và mọi trễ là bội số của tuần (336, 504, 672...) cho cùng kết luận.
"""
from __future__ import annotations

from pathlib import Path

from .config import HOURS_PER_WEEK, RESULTS_DIR

# Thứ Ba 23:00 là mẫu cuối cùng đã biết; mẫu đó cách Thứ Bảy 00:00 đúng 73 giờ.
LAST_KNOWN_GAP_HOURS = 73


def min_lag_for_hour(hour_in_week: int) -> int:
    """Độ trễ nhỏ nhất (giờ) hợp lệ cho giờ thứ `hour_in_week` (0 = Thứ Bảy 00:00 ... 167 = Thứ Sáu 23:00)."""
    if not 0 <= hour_in_week < HOURS_PER_WEEK:
        raise ValueError("hour_in_week phải nằm trong [0, 167]")
    return hour_in_week + LAST_KNOWN_GAP_HOURS


def min_safe_lag() -> int:
    """Độ trễ cố định nhỏ nhất dùng được cho MỌI giờ trong tuần = 240."""
    return min_lag_for_hour(HOURS_PER_WEEK - 1)


def valid_hours_for_lag(lag_hours: int) -> int:
    """Số giờ trong tuần (0..168) mà đặc trưng L_{h-lag} hợp lệ. Ví dụ lag 168 -> 96 giờ (Thứ Bảy..Thứ Ba)."""
    return max(0, min(HOURS_PER_WEEK, lag_hours - LAST_KNOWN_GAP_HOURS + 1))


def is_lag_valid(lag_hours: int, hour_in_week: int | None = None) -> bool:
    """Hợp lệ cho một giờ cụ thể, hoặc (hour_in_week=None) cho mọi giờ trong tuần."""
    need = min_safe_lag() if hour_in_week is None else min_lag_for_hour(hour_in_week)
    return lag_hours >= need


def lag_violations(lag_table: dict[str, int]) -> list[str]:
    """Nhận {tên đặc trưng: độ trễ nhỏ nhất (giờ)}; trả về danh sách mô tả vi phạm (rỗng = sạch)."""
    out = []
    for name, lag in lag_table.items():
        if not is_lag_valid(lag):
            out.append(
                f"{name}: trễ {lag} h < {min_safe_lag()} h (chỉ hợp lệ cho {valid_hours_for_lag(lag)}/168 giờ trong tuần)"
            )
    return out


# --- Tập kiểm tra chỉ dùng một lần ----------------------------------------------------------------
DEFAULT_LOCK = RESULTS_DIR / ".test_used"


class TestSetLockError(PermissionError):
    __test__ = False  # không cho pytest thu thập nhầm là lớp test


def open_test_set(final: bool, lock_path: Path | None = None) -> None:
    """Gọi trước khi đọc nhãn tập kiểm tra. Chỉ chạy khi final=True và chưa có khóa; xong tạo khóa.

    Muốn chạy lại để TÁI LẬP kết quả (không để chọn lại mô hình): xóa results/.test_used và nói với cả nhóm.
    """
    lock = Path(lock_path) if lock_path else DEFAULT_LOCK
    if not final:
        raise TestSetLockError("Tập kiểm tra chỉ mở với cờ --final (đề mục 3.1d).")
    if lock.exists():
        raise TestSetLockError(f"Tập kiểm tra đã dùng ({lock}). Không được chọn lại mô hình/ngưỡng sau khi xem kết quả.")
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text("tập kiểm tra đã được mở một lần\n", encoding="utf-8")
