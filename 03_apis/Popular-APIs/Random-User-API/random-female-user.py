import requests
import json

# getting a female random user using a query parameter
url = "https://randomuser.me/api/?gender=female"
female_response = requests.get(url)


# json response
json_response = female_response.json()
json_response_formatted = json.dumps(json_response, indent=0)
print(json_response_formatted)

print(json_response_formatted)