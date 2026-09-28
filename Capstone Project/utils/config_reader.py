"""Reads settings from config/config.ini.

pathlib is used so paths work on Windows (backslashes) and macOS/Linux alike.
"""
import configparser
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config" / "config.ini"

_parser = configparser.ConfigParser()
_parser.read(CONFIG_FILE, encoding="utf-8")


def get_base_url() -> str:
    return _parser.get("app", "base_url").rstrip("/")


def get_browser() -> str:
    return _parser.get("browser", "name").strip().lower()


def is_headless() -> bool:
    # An environment variable (HEADLESS=true) overrides the config file.
    env_value = os.environ.get("HEADLESS")
    if env_value is not None:
        return env_value.strip().lower() in ("1", "true", "yes")
    return _parser.getboolean("browser", "headless")


def get_explicit_wait() -> int:
    return _parser.getint("timeouts", "explicit_wait")


def get_page_load_timeout() -> int:
    return _parser.getint("timeouts", "page_load")
