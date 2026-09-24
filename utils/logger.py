"""Simple file logger shared by the whole framework.

Every log line goes to logs/framework.log, for both the PyTest and Unittest suites.
"""
import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
_ROOT_NAME = "framework"


def _setup():
    root = logging.getLogger(_ROOT_NAME)
    if root.handlers:  # already configured - avoids duplicate lines
        return root
    LOG_DIR.mkdir(exist_ok=True)
    handler = logging.FileHandler(LOG_DIR / "framework.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"))
    root.addHandler(handler)
    root.setLevel(logging.INFO)
    root.propagate = False
    return root


def get_logger(name: str) -> logging.Logger:
    _setup()
    return logging.getLogger(f"{_ROOT_NAME}.{name}")
