##### WEBEX TEAMS API - USER ACCOUNTS - SPACES/ ROOMS - MEMBERS - MESSAGES
### ACCESS TOKEN REQUESTED THROUGH LOGIN IN WEBEX DEVELOPER WEBSITE
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
##### BEGIN #####
import requests
import json
current_access_token = "OThlMzdjMzctZDQ3YS00ZThjLTg1YTAtOWI4NjBlZDIzZGRhNmRhYzdlY2YtOTU5_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path 
headers = {
    'Authorization': 'Bearer {}'.format(current_access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
##### END #####
#
### PRINTING RELEVANT DEBUGGING INFORMATION REGARDING THE API REQUEST
print("Access Token: " + current_access_token)
print('--------------------------------')
print('Request URI: ' + url)
print('Request Header: ' + json.dumps(headers))
print("API Return Code: " + str(res.status_code))  
user_name = res.json()['displayName']
print("Username: " + user_name)
print('--------------------------------') 
headers = {
'Authorization': 'Bearer {}'.format(current_access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4)) 