"""The module represents available routes of API."""

from sdk.models.api_call_dto import APIRoute, HTTPMethod
from sdk.models.request_dto.params import EmailsByDomain, VerifyEmail
from sdk.models.response_dto.domain_search_dto import DomainSearchResponse
from sdk.models.response_dto.verify_email_dto import EmailVerifierResponse
from sdk.requester import RequestClient


class HunterIOAPIRoutes(RequestClient):
    """The class represents HunterIO API routes."""

    _base_url = 'https://api.hunter.io/'
    _api_version = 'v2'

    def __init__(self, api_key: str):
        """Initialize HunterIOAPIRoutes."""
        super().__init__(api_key)

        self.get_email_by_domain = APIRoute(
            method=HTTPMethod.get,
            endpoint='{base_url}{api_version}/domain-search'.format(
                base_url=self._base_url, api_version=self._api_version,
            ),
            response_dto=DomainSearchResponse,
            request_params=EmailsByDomain,
            requester=self.call_api,
        )
        self.verify_email = APIRoute(
            method=HTTPMethod.get,
            endpoint='{base_url}{api_version}/email-verifier'.format(
                base_url=self._base_url, api_version=self._api_version,
            ),
            response_dto=EmailVerifierResponse,
            request_params=VerifyEmail,
            requester=self.call_api,
        )
