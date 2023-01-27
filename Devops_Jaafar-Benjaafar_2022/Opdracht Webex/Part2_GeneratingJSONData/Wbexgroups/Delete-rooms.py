##please note that this code will delete all the rooms that match the title in the groups_struc file
import requests
from webex_groups import groups_struc

access_token = 'OThlMzdjMzctZDQ3YS00ZThjLTg1YTAtOWI4NjBlZDIzZGRhNmRhYzdlY2YtOTU5_P0A1_20362e1d-455c-42c1-af6b-9c9e124a6fab'
headers = {'Authorization': 'Bearer {}'.format(access_token)}

for rec in groups_struc["groups"]:
    group_name = rec["group"]["group_name"]
    # Get the rooms with the matching group name
    url = 'https://webexapis.com/v1/rooms?title=' + group_name
    res = requests.get(url, headers=headers)
    room_data = res.json()
    for room in room_data['items']:
        # Delete each room
        url = 'https://webexapis.com/v1/rooms/' + room['id']
        res = requests.delete(url, headers=headers)