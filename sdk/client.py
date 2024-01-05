"""Module for interaction with API clients."""

from config import conf

from sdk.models.domain_search_models import DomainSearchInput
from sdk.models.verify_email_models import EmailVerifierInput
from sdk.requester import BaseClient


class HunterIOClient(object):
    """Represents the API for working with hunter.io site."""

    _base_url = 'https://api.hunter.io/'
    _api_version = 'v2'

    def __init__(self, requester: BaseClient) -> None:
        """Initialize class HunterIOClient instance and passed HTTP requester."""
        self.session = requester

    def verify_email(self, email: str) -> EmailVerifierInput:
        """
        Verify email validation by requesting hunter.io endpoint.

        :param email: Email that has to be verified.
        :return: EmailVerifierInput.
        """
        res = self.session.get(
            '{base_url}{api_version}/email-verifier'.format(base_url=self._base_url, api_version=self._api_version),
            request_params={
                'api_key': conf.hunterio_key,
                'email': email,
            },
        )
        return EmailVerifierInput(**res)

    def get_email_by_domain(
        self,
        domain: str | None = None,
        company: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> DomainSearchInput:
        """
        Allow to get list of emails by specified criteria.

        :param domain: Domain where email was registered.
        :param company: Company where email was registered.
        :param limit: Limit quantity of emails by page.
        :param offset: Pagination offset parameter.
        :return: DomainSearchInput
        """
        res = self.session.get(
            '{base_url}{api_version}/domain-search'.format(base_url=self._base_url, api_version=self._api_version),
            request_params={
                'api_key': conf.hunterio_key,
                'domain': domain,
                'company': company,
                'limit': limit,
                'offset': offset,
            },
        )
        return DomainSearchInput(**res)
