"""Module for interaction with API clients."""

from sdk.models.api_call_dto import APIRoute
from sdk.models.response_dto.base_response_dto import BaseResponseDTO
from sdk.requester import BaseClient
from sdk.typings import RequestInputs


class HunterIOClient(object):
    """Represents the API for working with hunter.io site."""

    def __init__(self, base_client: BaseClient) -> None:
        """Initialize class HunterIOClient instance and passed HTTP base_client."""
        self.base_client = base_client

    def call_api(
        self,
        api_route: APIRoute,
        request_inputs: RequestInputs | None = None,
    ) -> BaseResponseDTO | None:
        """
        Allow to make request to the API.

        :param api_route: Instance of :class: APIRoute that contains all needed info to process the request.
        :param request_inputs: Query parameters or body payload for the request, depends on HTTP method.
        :return: Correspond to APIRoute DTO or requests.exceptions.HTTPError.
        """
        return self.base_client.call_api(api_route, request_inputs)
