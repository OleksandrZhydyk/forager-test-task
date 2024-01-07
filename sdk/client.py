"""Module for interaction with API clients."""
from typing import Dict

from sdk.models.api_call_dto import APIRoute
from sdk.models.response_dto.base_response_dto import BaseResponseDTO
from sdk.requester import BaseClient


class HunterIOClient(object):
    """Represents the API for working with hunter.io site."""

    def __init__(self, base_client: BaseClient) -> None:
        """Initialize class HunterIOClient instance and passed HTTP base_client."""
        self.base_client = base_client

    def call_api(
        self,
        api_route: APIRoute,
        request_params: Dict[str, str | int | float] | None = None,
        request_payload: Dict[str, str | int | float] | None = None,
    ) -> BaseResponseDTO | None:
        """
        Allow to make request to the API.

        :param api_route: Instance of :class: APIRoute that contains all needed info to process the request.
        :param request_params: Query parameters for the request.
        :param request_payload: Body payload for the request.
        :return: Correspond to APIRoute DTO or errors:
            APIRetryExceededError, APIConnectionError, APIIncorrectRequestError.
        """
        return self.base_client.call_api(api_route, request_params, request_payload)
