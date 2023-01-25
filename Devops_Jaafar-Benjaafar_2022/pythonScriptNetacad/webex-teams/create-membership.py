# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMDYxYTM2ZTAtMGUzYy0xMWViLTgxNGUtMTNkMGZmZDEzMWE3'
person_email = 'denys.slyvka@student.odisee.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())