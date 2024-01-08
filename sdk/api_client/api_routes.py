"""The module represents base class for all request payload objects."""

from sdk.api_client.models.api_call_dto import APIRoute, HTTPMethod
from sdk.api_client.models.request_dto.params import EmailsByDomain, VerifyEmail
from sdk.api_client.models.response_dto.domain_search_dto import DomainSearchResponse
from sdk.api_client.models.response_dto.verify_email_dto import EmailVerifierResponse

_BASE_URL = 'https://api.hunter.io/'
_API_VERSION = 'v2'

GET_EMAILS_BY_DOMAIN = APIRoute(
    method=HTTPMethod.get,
    endpoint='{base_url}{api_version}/domain-search'.format(base_url=_BASE_URL, api_version=_API_VERSION),
    response_dto=DomainSearchResponse,
    request_params=EmailsByDomain,
)
VERIFY_EMAIL = APIRoute(
    method=HTTPMethod.get,
    endpoint='{base_url}{api_version}/email-verifier'.format(base_url=_BASE_URL, api_version=_API_VERSION),
    response_dto=EmailVerifierResponse,
    request_params=VerifyEmail,
)
