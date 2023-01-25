# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests
access_token = 'MTgzMDRlNjMtZTFhNS00NDQ1LWI4NzQtMWE0YmQ2MGFlYjViZDQ2ODM4ODAtMzkw_PF84_consumer'
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())