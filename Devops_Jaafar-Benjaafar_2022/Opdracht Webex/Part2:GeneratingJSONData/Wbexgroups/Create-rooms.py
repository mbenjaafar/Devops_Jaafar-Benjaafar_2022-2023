# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
import json
from webex_groups import groups_struc
access_token = 'YzM3ODNhMmMtMjBlYy00OWNkLTkyYWQtMjZmMzdjMzc2MjMxMzJkYTI3NDktODcz_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}

for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    params={'title': create_group_name}
    res = requests.post(url, headers=headers, json=params)
    if res.status_code != 200:
        print(res.status_code)
        print(res.text)
    else:
        response_data = json.loads(res.text)
        NEW_SPACE_ID = response_data["id"]
        for mbr in rec["group"]["members"]:
            person_email = mbr["email"]
            url2 = 'https://webexapis.com/v1/memberships'
            payload_member = {'roomId': NEW_SPACE_ID, 'personEmail': person_email}
            res_member = requests.post(url2, headers=headers, json=payload_member)

print(res.json())