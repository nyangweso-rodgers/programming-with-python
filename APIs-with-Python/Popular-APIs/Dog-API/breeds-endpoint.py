# breeds endpoint
import json
import requests

breeds_endpoint = 'https://api.thedogapi.com/v1/breeds'
response = requests.get(breeds_endpoint)

# json data
json_response = response.json()
##print(json_response)

# string data
json_string_response = json.dumps(json_response)

# write results into a json file
with open("breeds_sample_payload.json", "w") as outfile:
    outfile.write(json_string_response)