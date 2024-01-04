import requests

from abc import ABC, abstractmethod
from typing import Dict

from requests.adapters import HTTPAdapter
from urllib3 import Retry

from sdk.exceptions import APIRetryExceededError, APIConnectionError, APIIncorrectRequestException


class BaseClient(ABC):

    @abstractmethod
    def get(self, *args, **kwargs):
        pass


class RequestClient(BaseClient):

    DEFAULT_TIMEOUT = 5  # seconds
    RETRY_INTERVAL = 0.3  # seconds

    def __init__(self):
        self.session = self._get_session()

    def get(
        self,
        url: str,
        params: Dict[str, str] = None,
        headers: Dict[str, str] = None,
        proxies: Dict[str, str] = None,
        timeout: int = DEFAULT_TIMEOUT,
    ):
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
        raise APIIncorrectRequestException(res.status_code, res.json())

    def _get_session(self) -> requests.Session:
        session = requests.Session()
        retries = Retry(
            total=3, backoff_factor=self.RETRY_INTERVAL,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=['GET'],
        )
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))
        return session
