"""Represent all available classes to make a HTTP requests."""
from abc import ABC, abstractmethod
from typing import Dict, Any

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from sdk.exceptions import APIRetryExceededError, APIConnectionError, APIIncorrectRequestError


class BaseClient(ABC):
    """Represent the required interface for classes that will implement HTTP request feature."""

    @abstractmethod
    def get(self, *args, **kwargs):
        """Represent the required interface method for HTTP GET request."""
        ...


class RequestClient(BaseClient):
    """Implementation HTTP request client by requests library."""

    default_timeout = 5  # seconds
    retry_interval = 0.3  # seconds

    def __init__(self):
        """Initialize the request session."""
        self.session = self._get_session()

    def get(
        self,
        url: str,
        params: Dict[str, str] = None,
        headers: Dict[str, str] = None,
        proxies: Dict[str, str] = None,
        timeout: int = default_timeout,
    ) -> Dict[Any] | None:
        """
        Send HTTP GET request to the source.

        :param url: Requested url.
        :param params: Needed query parameters.
        :param headers: Needed request headers.
        :param proxies: Needed request proxies.
        :param timeout: Needed request timeout in seconds.
        :return: Requested data or errors: (APIRetryExceededError, APIConnectionError, APIIncorrectRequestError)
        """
        try:
            res = self.session.get(
                url,
                params=params,
                headers=headers,
                proxies=proxies,
                timeout=timeout,
            )
        except requests.exceptions.RetryError:
            raise APIRetryExceededError()
        except requests.exceptions.ConnectionError:
            raise APIConnectionError()
        if res.ok:
            return res.json()
        raise APIIncorrectRequestError(res.status_code, res.json())

    def _get_session(self) -> requests.Session:
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=self.retry_interval,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=['GET'],
        )
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))
        return session
