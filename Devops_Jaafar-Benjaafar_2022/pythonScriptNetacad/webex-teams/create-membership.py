# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests
access_token = 'M2VjMGVlY2UtZjJiYi00YTU5LTlmMDQtZGRkM2Y4NDdjMjE1ZThkOWViYzMtNmI2_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjlhMzcyMjAtOWNiNy0xMWVkLWEyYTgtNzMyMzY3ZGVhMjI2'
person_email = 'denys.slyvka@student.odisee.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())