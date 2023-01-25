# Fill in this file with the messages code from the Webex Teams exercise
import requests
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMDYxYTM2ZTAtMGUzYy0xMWViLTgxNGUtMTNkMGZmZDEzMWE3'
message = 'Test'
url = 'https://webexapis.com/v1/messages'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())