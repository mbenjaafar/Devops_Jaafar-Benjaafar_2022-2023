#################################################################################
# This program:
# 1. Asks the user for their access token or to use the hard-coded access token
# 2. Displays a list of the user's Spark rooms
# 3. Asks the user to choose one of their rooms
# 4. Asks the user to enter text of a message(s) for that room
# 5. Displays all the messages in that room that contains that text
#
# The student will:
# 1. Provide the code to prompt the user for their access token else
#    use the hard-coded access token
# 2. Enter the Cisco Spark room API endpoint (URL)
# 3. Add the following information regarding for each message:
# - From (email) 
# - Date/time message was created
# 4. Add a message counter to:
# - If messages were found, display the number of messages found using this criteria
# - Else display a message stating no messages were found using this criteria.
# 5. Display a message that verifies the room and text searched.
#################################################################################


import requests
import json
import time

#######################################################################################
#     Ask the user to use either the hard-coded token (access token within the code)
#     or for the user to input their access token.
#     Assign the hard-coded or user entered access token to the variable accessToken.
#######################################################################################

# Student Step #1
# Following this comment and using the accessToken variable below, modify the code to
# ask the user to use either hard-coded or user entered access token.

<!!!REPLACEME with code to ask user for the Cisco Spark Access Token or use a hard-coded one!!!>

#######################################################################################
#     Using the requests library, create a new HTTP GET Request against the Spark API Endpoint for Spark Rooms:
#     the local object "r" will hold the returned data.
#######################################################################################

#  Student Step #2
#     Modify the code below to use the Cisco Spark room API endpoint (URL)
resp = requests.get(   "<!!!REPLACEME with URL for Cisco Spark Rooms API!!!>",
                    headers = {"Authorization": accessToken}
                )
#######################################################################################
# Check if the response from the API call was OK (resp. code 200)
#######################################################################################

if not resp.status_code == 200:
    raise Exception("Incorrect reply from Cisco SPARK API. Status code: {}. Text: {}".format(resp.status_code, resp.text))

#######################################################################################
# If you want to see what is in the JSON data for Spark Rooms remove # from these statements:
#
#jsonData = resp.json()
#
#print(
#    json.dumps(
#        jsonData,
#        indent=4
#    )
#)
#######################################################################################

#######################################################################################
# Displays a list of rooms.
#
# If you want to see additional key/value pairs such as roomID:
#	print ("Room name: '" + room["title"] + "' room ID: " + room["id"])
#######################################################################################

print("List of rooms:")
rooms = resp.json()["items"]
for room in rooms:
    print (room["title"])

#######################################################################################
# Searches for name of the room and displays the room
#######################################################################################

while True:
    # Input the name of the room to be searched 
    roomNameToSearch = input("Which room are you looking for? (Can use partial name of the room.) ")

    # Defines a variable that will hold the roomId 
    roomIdToGetMessages = None
    
    for room in rooms:
        # Searches for the room "title" using the variable roomNameToSearch 
        if(room["title"].find(roomNameToSearch) != -1):

            # Displays the rooms found using the variable roomNameToSearch (additional options included)
            print ("Found rooms with the word " + roomNameToSearch)
            print(room["title"])

            # Stores room id and room title into variables
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room : " + roomTitleToGetMessages)
            break

    if(roomIdToGetMessages == None):
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
    else:
        break

#######################################################################################
# Define the mandatory or optional GET parameters for the `messages` API endpoint
# max is the number of messages to be displayed
#######################################################################################

getMessagesUrlParameters = {
            # mandatory parameter - the room ID
            "roomId": roomIdToGetMessages,
            # optional parameter - number of the last messages to return
            "max": 50
}

#######################################################################################
# Using the requests library, create a new HTTP GET Request against the Spark API Endpoint
# for Spark Messages. The local object "r" will hold the returned data.
#######################################################################################

resp = requests.get(   "https://api.ciscospark.com/v1/messages",
                    params = getMessagesUrlParameters,
                    headers = {"Authorization": accessToken}
                )

if not resp.status_code == 200:
    raise Exception("Incorrect reply from Cisco SPARK API. Status code: {}. Text: {}".format(resp.status_code, resp.text))

#######################################################################################
# Data is converted to JSON format and held in jsonData
#######################################################################################

jsonData = resp.json()

#######################################################################################
# To see what is in the JSON data remove the # from the statements below:
#
#print(
#    json.dumps(
#        jsonData,
#        indent=4
#    )
#)
#######################################################################################

#######################################################################################
#    Add a message counter and initialize the variable to 0
#    - If messages were found, display the number of messages found using this criteria
#    - Else display a message stating no messages were found using these criteria.
#
#    Search for message text and display:
#     - Message text
#
#    Add the following information regarding for each message:
#    - From (email) 
#    - Date/time message created
#
#######################################################################################

messages = jsonData["items"]
messageText = input("What text are you searching for? ")
# Student Step #3a: Following this comment, create a variable for a message counter
# and initialize it to 0.
<!!!REPLACEME with a messageCounter variable set to 0 !!!>

for message in messages:
    if message["text"].find(messageText) != -1:
        # Student Step #3b: Following this comment, increment message counter variable by 1
        <!!!REPLACEME with incrementing the messageCounter by one!!!>
        
        messageId = message["id"]
        print("Found a message with: " + messageText)
        print("Message: " + message["text"])
        # Student Step #4: Following this comment, display email address of the message 
        # creator and the date/time the message was created
        print(<!!!REPLACEME!!!>)
        print(<!!!REPLACEME!!!>)
        
# Student Step #5:
#     Following these comments: 
#     Add if-else statements to display message counter information
#     - If no messages were found using this criteria (if messageCounter is 0) display a message that informs the uses of this
#     - Else display a message with the number of messages found (messageCounter) using this criteria

<!!!REPLACEME with if statements checking for messageCounter value!!!>
    <!!!REPLACEME with print function printing the number of found messages!!!>


print("Thank you for using this program and think API + Python!")

#######################################################################################
# End of program
#######################################################################################

