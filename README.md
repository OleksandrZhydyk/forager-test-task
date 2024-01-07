## Python SDK for interacting with the Hunter API.

### Requirements
* Python >= 3.11

### Installation
```shell
pip install 'package_name'
```

### Obtain an API key
To obtain api key for HunterIO interaction please follow the [instruction](https://help.hunter.io/en/articles/1970978-what-is-and-where-i-can-find-my-api-secret-key).


### Quickstart

#### Create API client
To make a request, initialize a `RequestClient` instance with an API key and pass it to `HunterIOClient`.

#### Call API route
To trigger a specific API route, call the `call_api` method of the client with the relevant `api_routes` setting and the required request parameters or payloads.


```python
import os

from 'package_name'.sdk.api_routes import GET_EMAILS_BY_DOMAIN
from 'package_name'.sdk.client import HunterIOClient
from 'package_name'.sdk.models.response_dto.domain_search_dto import DomainSearchResponse
from 'package_name'.sdk.requester import RequestClient

# Initialize API client
base_client = RequestClient(token=os.environ["HUNTERIO_API_KEY"])
client = HunterIOClient(base_client)

# Request API endpoint
def get_email_by_domain() -> DomainSearchResponse:
    domain_emails = client.call_api(api_route=GET_EMAILS_BY_DOMAIN, request_params={'domain': 'intercom.io'})
    return domain_emails
```