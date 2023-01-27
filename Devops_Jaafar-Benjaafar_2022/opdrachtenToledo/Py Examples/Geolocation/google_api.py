import urllib.parse
import requests
import datetime
import json
print("Current date and time: ")
print(datetime.datetime.now())
print('Imported libraries for the script')
print('STARTING Google API Geolocation')

print("Current date and time: ")
print(datetime.datetime.now())
print('Getting input')
#####
address = input("Town or City? ")

url = "https://maps.googleapis.com/maps/api/geocode/json"
key = "AIzaSyCnTxO5K6ShhCaf04LUlRB6ZuXJDfpol6w"
uri = url+"?"+"address"+"="+address+"&"+"key"+"="+key
print("Current date and time: ")
print(datetime.datetime.now())
print('Creating full request')
json_data = requests.get(uri).json()
print(uri)

print("Current date and time: ")
print(datetime.datetime.now())
print('Success  of the request')
print("STATUS")
print('--------------')
json_status = json_data["status"]
print("API Status: " + json_status)
print('--------------')

print("Current date and time: ")
print(datetime.datetime.now())
print('Raw result of the request')
if json_status == "OK":
    print("FULL RESULT IN JSON")
    print('--------------')
    print(json_data)
    print('--------------')
    print("Current date and time: ")
print(datetime.datetime.now())

print('Filtered result of the request')
if json_status == "OK":
    print("SELECTED RESULT 1 ")
    print('--------------')
    selection = json_data['results'][0]['formatted_address']
    print(selection)
    print('--------------')
    print("Current date and time: ")
print(datetime.datetime.now())

if json_status == "OK":
    print("SELECTED RESULT 2 ")
    print('--------------')
    selection1 = json_data['results'][0]['address_components'][0]['long_name']
    selection2 = json_data['results'][0]['address_components'][1]['long_name']
    selection3 = json_data['results'][0]['address_components'][2]['long_name']
    selection4 = json_data['results'][0]['address_components'][3]['long_name']
    print(selection1)
    print(selection2)
    print(selection3)
    print(selection4)
    print('--------------')
print("Current date and time: ")
print(datetime.datetime.now())

if json_status == "OK":
    print("LOOPING THROUGH RESULT")
    for each in json_data["results"][0]["address_components"]:
        print(each["long_name"])
