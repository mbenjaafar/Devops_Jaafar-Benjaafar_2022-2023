# Fill in this file with the membership code from the Webex Teams exercise
import requests
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMDYxYTM2ZTAtMGUzYy0xMWViLTgxNGUtMTNkMGZmZDEzMWE3'
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())