"""The module represents available HTTP methods and route configuration."""

import enum
from typing import Any, Callable, Type

from pydantic import BaseModel

from sdk.models.request_dto.base_params import RequestParams
from sdk.models.request_dto.base_payload import RequestPayload
from sdk.models.response_dto.base_response_dto import BaseResponseDTO
from sdk.typings import RequestInputs


class HTTPMethod(enum.Enum):
    """API available HTTP methods."""

    get = 'GET'
    post = 'POST'
    put = 'PUT'
    patch = 'PATCH'
    delete = 'DELETE'


class APIRoute(BaseModel):
    """Class represents config point for specific API route."""

    method: HTTPMethod
    endpoint: str
    response_dto: Type[BaseResponseDTO]
    request_params: Type[RequestParams] | None = None
    request_payload: Type[RequestPayload] | None = None
    requester: Callable

    def __call__(
        self,
        request_params: RequestInputs | None = None,
        request_payload: RequestInputs | None = None,
    ) -> Any:
        """Make a request when attribute call."""
        return self.requester(self, request_params, request_payload)
