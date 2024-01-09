"""Module for interaction with API clients."""
from sdk.api_routes import HunterIOAPIRoutes
from sdk.requester import RequestClient


class HunterIOClient(RequestClient, HunterIOAPIRoutes):
    """Represents the API for working with hunter.io site."""

    def __init__(self, token: str) -> None:
        """Initialize class HunterIOClient instance and passed HTTP base_client."""
        super().__init__(token=token)
