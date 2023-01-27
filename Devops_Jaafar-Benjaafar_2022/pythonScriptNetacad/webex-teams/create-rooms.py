# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
access_token = 'M2VjMGVlY2UtZjJiYi00YTU5LTlmMDQtZGRkM2Y4NDdjMjE1ZThkOWViYzMtNmI2_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}

params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())