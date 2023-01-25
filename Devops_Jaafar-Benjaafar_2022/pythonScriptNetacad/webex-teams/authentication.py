# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'
url = 'https://webexapis.com/v1/people/me'

headers = {
'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
