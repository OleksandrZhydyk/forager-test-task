"""Module for interaction with API clients."""
from sdk.api_routes import HunterIOAPIRoutes


class HunterIOClient(object):
    """Represents the API for working with hunter.io site."""

    def __init__(self, api_key: str) -> None:
        """Initialize class HunterIOClient instance and passed HTTP base_client."""
        self.email_verification_handler = HunterIOAPIRoutes(api_key)
