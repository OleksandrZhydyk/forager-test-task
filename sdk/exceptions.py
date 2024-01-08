"""The module represents APIError, DataManager clients errors."""
from typing import Dict


class APIError(Exception):
    """Base class for API related exceptions."""


class APIRetryExceededError(APIError):
    """Class represents error by exceeded retry quantity requests."""

    def __init__(self, message: str = 'Provider API error. Max retries exceeded.') -> None:
        """Initialize class APIRetryExceededError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIConnectionError(APIError):
    """Class represents error by connection to the API service."""

    def __init__(self, message: str = 'Provider API connection error.') -> None:
        """Initialize class APIConnectionError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIIncorrectRequestError(APIError):
    """Class represents error by incorrect formatted requests to the API service."""

    def __init__(self, status_code: int, message: Dict[str, str]) -> None:
        """Initialize class APIIncorrectRequestError instance with passed error message."""
        self.status_code = 'HTTPError {status_code}'.format(status_code=status_code)
        super().__init__(message, self.status_code)


class DataManagerError(Exception):
    """Base class for DataManager related exceptions."""


class KeyAlreadyExistsError(DataManagerError):
    """Class represents error by duplicate key in storage."""

    def __init__(self, message: str = 'Provided key already exists in the storage.') -> None:
        """Initialize class KeyAlreadyExistsError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class KeyNotFoundError(DataManagerError):
    """Class represents error by absence of key in storage."""

    def __init__(self, message: str = 'Current key does not exist in the storage.') -> None:
        """Initialize class KeyNotFoundError instance with passed error message."""
        self.message = message
        super().__init__(self.message)
