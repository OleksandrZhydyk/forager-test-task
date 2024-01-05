class APIError(Exception):
    """Base class for API related exceptions."""


class APIRetryExceededError(APIError):
    def __init__(self, message='Provider API error. Max retries exceeded.'):
        """Initialize class APIRetryExceededError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIConnectionError(APIError):
    def __init__(self, message='Provider API connection error.'):
        """Initialize class APIConnectionError instance with passed error message."""
        self.message = message
        super().__init__(self.message)


class APIIncorrectRequestError(APIError):
    def __init__(self, status_code, message):
        """Initialize class APIIncorrectRequestError instance with passed error message."""
        self.status_code = f'HTTPError {status_code}'
        self.message = message['message']
        super().__init__(self.message, self.status_code)
