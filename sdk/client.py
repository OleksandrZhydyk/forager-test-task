"""Module for interaction with API clients"""

from config import conf
from sdk.filter import ConfidenceMoreThanFilter, ConfidenceLessThanFilter
from sdk.models import EmailVerifierInput, DomainSearchInput
from sdk.requester import BaseClient, RequestClient


class HunterIOClient:
    """Represents the API for working with hunter.io site."""

    _base_url = 'https://api.hunter.io/'
    _api_version = 'v2'

    def __init__(self, requester: BaseClient):
        """Initialize class HunterIOClient instance and passed HTTP requester."""
        self.session = requester

    def verify_email(self, email: str) -> EmailVerifierInput:
        """
        Verify email validation by requesting hunter.io endpoint.

        :param email: Email that has to be verified.
        :return: EmailVerifierInput.
        """
        res = self.session.get(
            f'{self._base_url}{self._api_version}/email-verifier',
            params={
                'api_key': conf.hunterio_key,
                'email': email,
            },
        )
        return EmailVerifierInput(**res)

    def get_email_by_domain(
        self,
        domain: str = None,
        company: str = None,
        limit: int = None,
        offset: int = None,
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
            f'{self._base_url}{self._api_version}/domain-search',
            params={
                'api_key': conf.hunterio_key,
                'domain': domain,
                'company': company,
                'limit': limit,
                'offset': offset,
            },
        )
        return DomainSearchInput(**res)


if __name__ == '__main__':
    requester = RequestClient()
    client = HunterIOClient(requester)
    data = client.get_email_by_domain('intercom.io')
    data.update_item('christine.curtin@intercom.io', 'value', 'a@a.com')
    filter_confidence1 = ConfidenceMoreThanFilter(90)
    filter_confidence2 = ConfidenceLessThanFilter(93)
    filtered_data = data.get_items(filter_confidence1, filter_confidence2)
    print(filtered_data)
