# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'

url = 'https://webexapis.com/v1/people'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {
'email': 'john.andersen@example.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS81ZjE4YjI1MC04ZmIxLTQ5NDItYWI3Yi00NjAzMDg2NzFkOTg'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))