"""Module for interaction with API clients."""

from sdk.api_client.requester import RequestClient


class HunterIOClient(RequestClient):
    """Represents the API for working with hunter.io site."""

    def __init__(self, token: str) -> None:
        """Initialize class HunterIOClient instance and passed HTTP base_client."""
        super().__init__(token=token)
