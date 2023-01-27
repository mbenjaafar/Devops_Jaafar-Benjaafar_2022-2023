# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json
access_token = 'M2VjMGVlY2UtZjJiYi00YTU5LTlmMDQtZGRkM2Y4NDdjMjE1ZThkOWViYzMtNmI2_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'

url = 'https://webexapis.com/v1/people'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {
'email': 'jaafar.benjaafar@student.odisee.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yMDM2MmUxZC00NTVjLTQyYzEtYWY2Yi05YzllMTI0YTZmYWI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))