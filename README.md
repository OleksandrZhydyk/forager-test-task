## Python SDK for interacting with the Hunter API.

### Requirements
* Python >= 3.11

### Installation
```shell
pip install 'package_name'
```

### Obtain an API key
For obtaining of api key for HunterIO interaction please follow the [instruction](https://help.hunter.io/en/articles/1970978-what-is-and-where-i-can-find-my-api-secret-key).


### Quickstart

#### Create API client
Initialize a `RequestClient` instance with an API key and pass it to `HunterIOClient`.

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
    domain_emails = client.call_api(api_route=GET_EMAILS_BY_DOMAIN, request_inputs={'domain': 'intercom.io'})
    return domain_emails
```

In order to save and make further data modification, you may use `DataManager`.

```python
import uuid 

from 'package_name'.sdk.data_manager import DataManager


some_data = 'some_data'
data_manager = DataManager()
unique_key = uuid.uuid4()

# Add data to storage
data_manager.add_data(key=unique_key, data_to_store=some_data)

# Get specific data
specific_data = data_manager.read(key=unique_key)

# Modify data
data_manager.update(key=unique_key, new_data_to_store='new data to store')

# Delete specific data
deleted_data_key = data_manager.delete(key=unique_key)

# Get all data from storage
storage_data = data_manager.get_all_stored_data()
```