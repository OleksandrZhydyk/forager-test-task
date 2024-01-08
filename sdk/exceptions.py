"""The module represents DataManager client errors."""


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
