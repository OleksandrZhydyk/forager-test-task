from config import conf
from sdk.filter import ConfidenceMoreThanFilter, ConfidenceLessThanFilter
from sdk.models import EmailVerifierInput, DomainSearchInput
from sdk.requester import BaseClient, RequestClient


class HunterIOClient:
    _base_url = 'https://api.hunter.io/'
    _api_version = 'v2'

    def __init__(self, requester: BaseClient):
        self.session = requester

    def verify_email(self, email: str) -> EmailVerifierInput:
        res = self.session.get(
            f'{self._base_url}{self._api_version}/email-verifier',
            params={
                'api_key': conf.HUNTERIO_KEY,
                'email': email,
            },
        )
        return EmailVerifierInput(**res)

    def get_email_by_domain(
            self,
            domain: str = None,
            company: str = None,
            limit: int = None,
            offset: int = None
    ) -> DomainSearchInput:
        res = self.session.get(
            f'{self._base_url}{self._api_version}/domain-search',
            params={
                'api_key': conf.HUNTERIO_KEY,
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
