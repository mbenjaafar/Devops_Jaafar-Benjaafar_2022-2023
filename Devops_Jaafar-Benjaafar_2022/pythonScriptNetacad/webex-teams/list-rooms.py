# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests
access_token = 'M2VjMGVlY2UtZjJiYi00YTU5LTlmMDQtZGRkM2Y4NDdjMjE1ZThkOWViYzMtNmI2_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())