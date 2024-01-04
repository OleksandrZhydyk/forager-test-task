class APIError(Exception):
    """Base class for API related exceptions."""
    pass


class APIRetryExceededError(APIError):
    def __init__(self, message='Provider API error. Max retries exceeded.'):
        self.message = message
        super().__init__(self.message)


class APIConnectionError(APIError):
    def __init__(self, message='Provider API connection error.'):
        self.message = message
        super().__init__(self.message)


class APIIncorrectRequestException(APIError):
    def __init__(self, status_code, message):
        self.status_code = f'HTTPError {status_code}'
        self.message = message['message']
        super().__init__(self.message, self.status_code)
