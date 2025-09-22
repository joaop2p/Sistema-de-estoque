from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from ..constants.exception_keys import ExceptionKey

@dataclass
class AppException(Exception):
    key: ExceptionKey
    message: str
    cause: Optional[BaseException] = None

    def __str__(self) -> str:  # pragma: no cover
        base = f"[{self.key}] {self.message}"
        return f"{base} | cause={self.cause}" if self.cause else base

class NetworkException(AppException):
    def __init__(self, message: str = "Network error", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.NETWORK_ERROR, message, cause)

class TimeoutException(AppException):
    def __init__(self, message: str = "Timeout error", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.TIMEOUT_ERROR, message, cause)

class AuthException(AppException):
    def __init__(self, message: str = "Authentication error", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.AUTH_ERROR, message, cause)

class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.NOT_FOUND, message, cause)

class ValidationException(AppException):
    def __init__(self, message: str = "Validation error", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.VALIDATION_ERROR, message, cause)

class ConflictException(AppException):
    def __init__(self, message: str = "Conflict error", cause: Optional[BaseException] = None):
        super().__init__(ExceptionKey.CONFLICT_ERROR, message, cause)
