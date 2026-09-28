"""Shared screenshot helper (used by both the PyTest and Unittest suites)."""
import re
from datetime import datetime
from pathlib import Path

SCREENSHOT_DIR = Path(__file__).resolve().parent.parent / "screenshots"


def save_screenshot(driver, test_name: str):
    """Save a PNG in /screenshots and return its path (None if it failed)."""
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    # Test ids like test_x[a/b] contain characters Windows does not allow in file names.
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", test_name)[:120]
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOT_DIR / f"{safe_name}_{stamp}.png"
    try:
        driver.save_screenshot(str(path))
        return path
    except Exception:
        return None
