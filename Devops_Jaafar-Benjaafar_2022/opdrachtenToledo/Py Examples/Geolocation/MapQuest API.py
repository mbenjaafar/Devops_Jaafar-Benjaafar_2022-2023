#!/usr/bin/env python
# coding: utf-8
# Exported from Jupyter Notebook
# In[1]:


import json
import urllib.parse
import requests
print('MapQuest API Lab -- Get Route')
print('Hands-on lab using Get Route which is a part of the MapQuest API ecosystem')
print('Steps used below are different from the steps in the basic lab')
print('STEP 1: Import necessary libraries: urllib.parse and requests')
print('STEP 2: Define URL for the API to be called as well as the key to be given access')
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "th0o4YURLPy443wAxKekVk1OzaNOkJqm"
print('STEP 3: Key: ' + key)


# In[3]:


print('STEP 4: Request ORIGIN and DESTINATION')
orig = input("Starting Location: ")
if orig != "quit" or orig != "q" or orig != "":
    dest = input("Destination: ")
if dest != "quit" or dest != "q" or dest != "":
    print('STEP 5: Here are the origin and destination requested: ')
    print('START ==> ' + orig)
    print('FINISH ==> ' + dest)
else:
    print('No request for ORIGIN and DESTINATION')


# In[4]:


print('STEP 6: Combine the four variables main_api, orig, dest, and key to format the requested URL')
print('Use the urlencode method to properly format the address value')
url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
print('STEP 6b: New Request URL')
print('URL ==> ' + url)
print('STEP 6c: Sending API request')
json_data = requests.get(url).json()
print('STEP 6d: Printing JSON status')
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print('Status: 0 (OK)')
else:
    print('Status: not OK')
print('STEP 6e: Printing raw JSON data')
print('HERE ARE THE JSON DATA ...')
print('==============================================================')
print(json_data)
print('==============================================================')


# In[5]:


print('STEP 6b: Pretty Output of previous step')
print(json.dumps(json_data, indent=4))


# In[6]:


print('STEP 7: Calculating duration and distance')
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("=============================================")
    print("Directions from  " + (orig) + " to " + (dest))
    print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
    print("Kilometers: " + str((json_data["route"]["distance"])*1.61))
    print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))

    print("=============================================")
else:
    print('Unfortunately, JSON request not succesfull')
    print('JSON status: ' + str(json_status))


# In[7]:


if json_status == 0:
    print('STEP 8: List of maneuvers from start to finish ...')
    print("=============================================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" +
              str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================================\n")
elif json_status == 402:
    print("**********************************************")
    print("Status Code: " + str(json_status) +
          "; Invalid user inputs for one or both locations.")
    print("**********************************************\n")
else:
    print("************************************************************************")
    print("For Status Code: " + str(json_status) + "; Refer to:")
    print("https://developer.mapquest.com/documentation/directions-api/status-codes")
    print("************************************************************************\n")
