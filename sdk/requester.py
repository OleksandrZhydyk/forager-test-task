"""Represent all available classes to make a HTTP requests."""
from abc import ABC, abstractmethod
from dataclasses import asdict
from typing import Any, Type

from requests import PreparedRequest, Request, Session, adapters
from urllib3 import Retry

from sdk.models.api_call_dto import APIRoute
from sdk.models.request_dto.base_params import RequestParams
from sdk.models.request_dto.base_payload import RequestPayload
from sdk.typings import RequestInputs


class BaseClient(ABC):
    """Represent the required interface for classes that will implement HTTP request feature."""

    @abstractmethod
    def call_api(
        self,
        api_route: 'APIRoute',
        request_params: RequestInputs | None = None,
        request_payload: RequestInputs | None = None,
    ) -> Any:
        """Represent the required interface method for HTTP GET request."""


class RequestClient(BaseClient):
    """Implementation HTTP request client by requests library."""

    default_timeout = 5  # seconds
    retry_interval = 0.3  # seconds

    def __init__(self, api_key: str | None) -> None:
        """Initialize the request session."""
        if not isinstance(api_key, str):
            raise ValueError('The token argument has to be a <class: str>')
        self.api_key = api_key
        self.session = self._get_session()

    def call_api(
        self,
        api_route: 'APIRoute',
        request_params: RequestInputs | None = None,
        request_payload: RequestInputs | None = None,
    ) -> Any | None:
        """
        Check incoming request data and make corresponding request to the API.

        :param api_route: Instance of :class: APIRoute that contains all needed info to process the request.
        :param request_params: Query parameters for the request.
        :param request_payload: Body payload for the request.
        :return: Correspond to APIRoute DTO or requests.exceptions.HTTPError.
        """
        processed_params = None
        processed_payload = None
        if request_params and api_route.request_params:
            processed_params = self._check_request_inputs(api_route.request_params, request_params)
        if request_payload and api_route.request_payload:
            processed_payload = self._check_request_inputs(api_route.request_payload, request_payload)
        prepared_request = self._build_request(
            api_route.method.value, api_route.endpoint, processed_params, processed_payload,
        )
        res = self.session.send(prepared_request, timeout=self.default_timeout)
        res.raise_for_status()
        return api_route.response_dto(**res.json())

    def _build_request(
        self,
        method: str,
        url: str,
        request_params: RequestInputs | None = None,
        request_payload: RequestInputs | None = None,
    ) -> PreparedRequest:
        """
        Create request object before API call.

        :param method: One from HTTP request method.
        :param url: Requested url.
        :param request_params: Url query parameters for the request.
        :param request_payload: Request body payload.
        :return: Requests lib PreparedRequest object.
        """
        req = Request(method=method, url=url, params=request_params, json=request_payload)
        return self.session.prepare_request(req)

    def _check_request_inputs(
        self,
        request_inputs_dto: Type[RequestParams] | Type[RequestPayload],
        request_inputs: RequestInputs,
    ) -> RequestInputs:
        request_inputs_dict = request_inputs_dto(**request_inputs)
        return asdict(request_inputs_dict)

    def _get_session(self) -> Session:
        session = Session()
        retries = Retry(
            total=3,
            backoff_factor=self.retry_interval,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=['GET'],
        )
        session.mount('https://', adapters.HTTPAdapter(max_retries=retries))
        session.mount('http://', adapters.HTTPAdapter(max_retries=retries))
        return self._set_default_params(session)

    def _set_default_params(self, session: Session) -> Session:
        default_params = {
            'api_key': self.api_key,
        }
        session.params = default_params
        return session
