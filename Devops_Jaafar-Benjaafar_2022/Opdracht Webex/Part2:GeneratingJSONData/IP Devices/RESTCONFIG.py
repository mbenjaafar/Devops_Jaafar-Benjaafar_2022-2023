import json
import requests

# Load JSON data into a variable
rack_struc = json.loads("<JSON data>")

# Define base URL for RESTCONF server
base_url = 'http://<RESTCONF-server-IP-address>:<port>/restconf/'

# Iterate through devices in JSON data
for device in rack_struc['rack']:
    dev_name = device['device']['dev_name']
    role = device['device']['role']
    interfaces = device['device']['interfaces']
    
    # Iterate through interfaces for each device
    for interface in interfaces:
        intf_name = interface['interface']
        ip_address = interface['ipaddress']
        subnet_mask = interface['subnetmask']
        
        # Construct URL for interface configuration
        url = base_url + 'config/native/interface/' + intf_name
        
        # Define payload for HTTP PUT request
        payload = {
            "interface": {
                "name": intf_name,
                "ip": {
                    "address": {
                        "primary": {
                            "address": ip_address,
                            "mask": subnet_mask
                        }
                    }
                }
            }
        }
        
        # Make HTTP PUT request to configure interface
        response = requests.put(url, json=payload, auth=('<username>', '<password>'))
        
        # Print response
        print(f"Device: {dev_name}, Interface: {intf_name}")
        print("Status code: ", response.status_code)
        print("Response: ", response.json())