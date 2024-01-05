"""The module represents API client errors."""


class APIError(Exception):
    """Base class for API related exceptions."""


class APIRetryExceededError(APIError):
    """Class represents error by exceeded retry quantity requests."""

    def __init__(self, message='Provider API error. Max retries exceeded.'):
        """Initialize class APIRetryExceededError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIConnectionError(APIError):
    """Class represents error by connection to the API service."""

    def __init__(self, message='Provider API connection error.'):
        """Initialize class APIConnectionError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIIncorrectRequestError(APIError):
    """Class represents error by incorrect formatted requests to the API service."""

    def __init__(self, status_code, message):
        """Initialize class APIIncorrectRequestError instance with passed error message."""
        self.status_code = 'HTTPError {status_code}'.format(status_code=status_code)
        self.message = message['message']
        super().__init__(self.message, self.status_code)
