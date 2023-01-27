import json

with open('docker_json') as docker_json:
    # Use the json.load() function to parse the JSON data in the file
    data = json.load(docker_json)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict = json.loads(docker_json)
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])
