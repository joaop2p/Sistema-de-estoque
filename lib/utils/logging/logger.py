from __future__ import annotations
import logging
from typing import Optional
from ..constants.log_keys import LogKey

class AppLogger:
    def __init__(self, name: str = "sistema_estoque", level: int = logging.INFO) -> None:
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            self._logger.setLevel(level)
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)

    def log(self, key: LogKey, message: str, *, extra: Optional[dict] = None, level: int = logging.INFO) -> None:
        payload = {"key": key.value, **(extra or {})}
        self._logger.log(level, f"{key.value} - {message} | {payload}")

    def info(self, key: LogKey, message: str, *, extra: Optional[dict] = None) -> None:
        self.log(key, message, extra=extra, level=logging.INFO)

    def warning(self, key: LogKey, message: str, *, extra: Optional[dict] = None) -> None:
        self.log(key, message, extra=extra, level=logging.WARNING)

    def error(self, key: LogKey, message: str, *, extra: Optional[dict] = None) -> None:
        self.log(key, message, extra=extra, level=logging.ERROR)
