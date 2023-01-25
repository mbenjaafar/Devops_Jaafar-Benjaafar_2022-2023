###############################################################
# This program:
# 1. Asks the user to enter an access token or use the hard coded access token
# 2. Lists the users Spark rooms
# 3. Asks the user which Spark room to monitor for "/location" requests (e.g. /San Jose)
# 4. Periodically monitors the selected Spark room for "/location" messages
# 5. Discovers GPS coordinates for the "location" using Google Maps API
# 6. Discovers the date and time of the next ISS flyover over the "location" using the ISS location API
# 7. Sends the results back to the Spark room
#
# The student will:
# 1. Enter the Cisco Spark room API endpoint (URL)
# 2. Provide the code to prompt the user for their access token else
#    use the hard coded access token
# 3. Provide the Google Maps API Key
# 4. Extracts the longitude from the Google Maps API response using the specific key
# 5. Convers Unix Epoch timestamp to a human readable format
# 6. Enter the Cisco Spark messages API endpoint (URL)
###############################################################

# Libraries

import requests
import json
import time

#######################################################################################
#     Ask the user to use either the hard-coded token (access token within the code)
#     or for the user to input their access token.
#     Assign the hard-coded or user-entered access token to the variable accessToken.
#######################################################################################

# Student Step #2
#    Following this comment and using the accessToken variable below, modify the code to
#    ask the user to use either hard-coded or user entered access token.

<!!!REPLACEME with code to ask user for the Cisco Spark Access Token or use a hard-coded one!!!>


#######################################################################################
#     Using the requests library, create a new HTTP GET Request against the Spark API Endpoint for Spark Rooms:
#     the local object "r" will hold the returned data.
#######################################################################################

#  Student Step #3
#     Modify the code below to use the Cisco Spark room API endpoint (URL)
r = requests.get(   "<!!!REPLACEME with URL for Cisco Spark Rooms API!!!>",
                    headers = {"Authorization": accessToken}
                )
#######################################################################################
# Check if the response from the API call was OK (r. code 200)
#######################################################################################
if not r.status_code == 200:
    raise Exception("Incorrect reply from Cisco SPARK API. Status code: {}. Text: {}".format(r.status_code, r.text))


#######################################################################################
# Displays a list of rooms.
#
# If you want to see additional key/value pairs such as roomID:
#	print ("Room name: '" + room["title"] + "' room ID: " + room["id"])
#######################################################################################
print("List of rooms:")
rooms = r.json()["items"]
for room in rooms:
    print (room["title"])

#######################################################################################
# Searches for name of the room and displays the room
#######################################################################################

while True:
    # Input the name of the room to be searched 
    roomNameToSearch = input("Which room should be monitored for /location (e.g. /San Jose) messages? ")

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


# run the "bot" loop until manually stopped or an exception occurred
while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Cisco Spark GET parameters
    #  "roomId" is is ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    sparkGetParameters = {
                            "roomId": roomIdToGetMessages,
                            "max": 1
                         }
    # run the call against the messages endpoint of the Cisco Spark API using the HTTP GET method
    r = requests.get("https://api.ciscospark.com/v1/messages", 
                         params = sparkGetParameters, 
                         headers = {"Authorization": accessToken}
                    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception( "Incorrect reply from Cisco SPARK API. Status code: {}. Text: {}".format(r.status_code, r.text))
    
    # get the JSON formatted returned data
    json_data = r.json()
    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")
    
    # store the array of messages
    messages = json_data["items"]
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)
    
    # check if the text of the message starts with the magic character "/" followed by a location name
    #  e.g.  "/San Jose"
    if message.find("/") == 0:
        # name of a location (city) where we check for GPS coordinates using the Google Maps APIs
        #  message[1:]  returns all letters of the message variable except the first "/" character
        #   "/San Jose" is turned to "San Jose" and stored in the location variable
        location = message[1:]
        
        #  Student Step #4
        #     Add the Google Maps API key (from Chapter 1)
        # the Google MAPS API GET parameters
        #  "address" is the the location to lookup
        #  "key" is the secret API KEY you generated at https://console.cloud.google.com
        mapsAPIGetParameters = { 
                                "address": location, 
                                "key": "<!!!REPLACEME with your Google Maps API Key!!!>"
                               }
        # Get location information using the Google MAPS API geocode service using the HTTP GET method
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", 
                             params = mapsAPIGetParameters
                        )
        # Verify if the returned JSON data from the Google Maps API service are OK
        json_data = r.json()
        # check if the status key in the returned JSON data is "OK"
        if not json_data["status"] == "OK":
            raise Exception("Incorrect reply from Google MAPS API. Status code: {}. Text: {}".format(r.status_code, r.text))

        # store the location address as received from the Google MAPS API in a variable
        locationAddress = json_data["results"][0]["formatted_address"]
        # print the location address
        print("Location address: " + locationAddress)

        #  Student Step #5
        #     Set the longitude key as retuned by the Google Maps API
        # store the GPS latitude and longitude of the location as received from the Google MAPS API in variables
        locationLat = json_data["results"][0]["geometry"]["location"]["lat"]
        locationLng = json_data["results"][0]["geometry"]["location"]["<!!!REPLACEME with the longtitude key!!!>"]
        # print the location address
        print("Location GPS coordinates: " + str(locationLat) + ", " + str(locationLng))
        
        # documentation of the ISS flyover API: http://open-notify-api.readthedocs.io/en/latest/iss_pass.html
        # the ISS flyover API GET parameters
        #  "lat" is the Latitude of the location
        #  "lon" is the longitude of the location
        issAPIGetParameters = { 
                                "lat": locationLat, 
                                "lon": locationLng
                              }
        # Get IIS flyover information over the specified GPS coordinates using the HTTP GET method
        r = requests.get("http://api.open-notify.org/iss-pass.json", 
                             params = issAPIGetParameters
                        )
        # get the json formatted retuned data
        json_data = r.json()
        # Verify if the returned JSON data from the API service are OK and contains the "response" key
        if not "response" in json_data:
            raise Exception("Incorrect reply from open-notify.org API. Status code: {}. Text: {}".format(r.status_code, r.text))

        # store the risetime and duration of the first flyover in a variable
        risetimeInEpochSeconds = json_data["response"][0]["risetime"]
        durationInSeconds      = json_data["response"][0]["duration"]

        #  Student Step #6
        #     Use the time.????? function to convert the risetime in Epoch timestamp to human readable time
        # convert the risetime returned by the API service in Unix Epoch time
        # to a human readable date and time
        risetimeInFormattedString = str(<!!!REPLACEME with a function that convers Epoch timestamp to human readable time!!!>(risetimeInEpochSeconds))

        # assemble the response message
        responseMessage = "In {} the ISS will flight over on {} for {} seconds.".format(locationAddress, risetimeInFormattedString, durationInSeconds)
        # print the response message
        print("Sending to Spark: " +responseMessage)
        
        
        # the Cisco Spark HTTP headers, including the Content-Type header for the POST JSON data
        sparkHTTPHeaders = { 
                             "Authorization": accessToken,
                             "Content-Type": "application/json"
                           }
        # the Cisco Spark POST JSON data
        #  "roomId" is is ID of the selected room
        #  "text": is the responseMessage assembled above
        sparkPostData = {
                            "roomId": roomIdToGetMessages,
                            "text": responseMessage
                        }
        # run the call against the messages endpoint of the Cisco Spark API using the HTTP POST method
        #  Student Step #7
        #     Modify the code below to use the Cisco Spark messages API endpoint (URL)
        r = requests.post( "<!!!REPLACEME with URL for Cisco Spark messages API!!!>", 
                              data = json.dumps(sparkPostData), 
                              headers = sparkHTTPHeaders
                         )
        if not r.status_code == 200:
            raise Exception("Incorrect reply from Cisco SPARK API. Status code: {}. Text: {}".format(r.status_code, r.text))


    