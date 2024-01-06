"""Represent all available classes to make a HTTP requests."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from sdk.exceptions import APIConnectionError, APIRetryExceededError
from sdk.utils import check_response_on_errors


class BaseClient(ABC):
    """Represent the required interface for classes that will implement HTTP request feature."""

    @abstractmethod
    def get(
        self,
        url: str,
        request_params: Dict[str, str | int | None] | None = None,
        headers: Dict[str, str] | None = None,
        timeout: Union[int, None] = None,
    ) -> Any:
        """Represent the required interface method for HTTP GET request."""

    @abstractmethod
    def post(
        self,
        url: str,
        body_params: Dict[str, str | int | None] | None = None,
        headers: Dict[str, str] | None = None,
        timeout: Union[int, None] = None,
    ) -> Any:
        """Represent the required interface method for HTTP POST request."""

    @abstractmethod
    def patch(self) -> None:
        """Represent the required interface method for HTTP PATCH request."""

    @abstractmethod
    def delete(self) -> None:
        """Represent the required interface method for HTTP DELETE request."""


class RequestClient(BaseClient):
    """Implementation HTTP request client by requests library."""

    default_timeout = 5  # seconds
    retry_interval = 0.3  # seconds

    def __init__(self, token: str) -> None:
        """Initialize the request session."""
        self.token = token
        self.session = self._get_session()

    def get(
        self,
        url: str,
        request_params: Dict[str, str | int | None] | None = None,
        headers: Dict[str, str] | None = None,
        timeout: Union[int, None] = default_timeout,
    ) -> Dict[str, Any] | None:
        """
        Send HTTP GET request to the source.

        :param url: Requested url.
        :param request_params: Needed query parameters.
        :param headers: Needed request headers.
        :param timeout: Needed request timeout in seconds.
        :return: Requested data or errors: (APIRetryExceededError, APIConnectionError, APIIncorrectRequestError)
        """
        try:
            res = self.session.get(
                url,
                params=request_params,
                headers=headers,
                timeout=timeout,
            )
        except requests.exceptions.RetryError:
            raise APIRetryExceededError()
        except requests.exceptions.ConnectionError:
            raise APIConnectionError()
        return check_response_on_errors(res)

    def post(
        self,
        url: str,
        body_data: Dict[str, Any | None] | None = None,
        headers: Dict[str, str] | None = None,
        timeout: Union[int, None] = None,
    ) -> Dict[str, Any] | None:
        """
        Send HTTP POST request to the source.

        :param url: Requested url.
        :param body_data: Request payload.
        :param headers: Needed request headers.
        :param timeout: Needed request timeout in seconds.
        :return: Requested data or errors: (APIRetryExceededError, APIConnectionError, APIIncorrectRequestError)
        """
        try:
            res = self.session.post(
                url,
                json=body_data,
                headers=headers,
                timeout=timeout,
            )
        except requests.exceptions.RetryError:
            raise APIRetryExceededError()
        except requests.exceptions.ConnectionError:
            raise APIConnectionError()
        return check_response_on_errors(res)

    def patch(self) -> None:
        """Represent the required interface method for HTTP PATCH request."""
        raise NotImplementedError

    def delete(self) -> None:
        """Represent the required interface method for HTTP DELETE request."""
        raise NotImplementedError

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
        return self._set_default_params(session)

    def _set_default_params(self, session: requests.Session) -> requests.Session:
        default_params = {
            'api_key': self.token,
        }
        session.params = default_params
        return session
