import requests
import json

# getting a male random user using a query parameter
url = "https://randomuser.me/api/?gender=male"
male_response = requests.get(url)

# json response
json_response = male_response.json()

# check the data type
print(type(json_response)) # <class 'dict'>

json_response_formatted = json.dumps(json_response, indent=0)
print(json_response_formatted)