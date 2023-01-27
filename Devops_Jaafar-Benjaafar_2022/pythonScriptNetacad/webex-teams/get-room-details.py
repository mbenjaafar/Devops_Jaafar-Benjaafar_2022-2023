# Fill in this file with the code to get room details from the Webex Teams exercise
import requests
access_token = 'M2VjMGVlY2UtZjJiYi00YTU5LTlmMDQtZGRkM2Y4NDdjMjE1ZThkOWViYzMtNmI2_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjlhMzcyMjAtOWNiNy0xMWVkLWEyYTgtNzMyMzY3ZGVhMjI2'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())