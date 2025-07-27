import requests
import json

url = "https://randomuser.me/api/"
response = requests.get(url)

print(response)

# getting a text reqponse
text_response = response.text
# print(text_response)

# getting a json response
json_response = response.json()
json_response_formatted = json.dumps(json_response, indent=0)
print(json_response_formatted)

# writing to sample.json
with open("random_user.json", "w") as outfile:
    outfile.write(json_response_formatted)
    
# using  query parameters
# getting only a female random user
requests.get("https://randomuser.me/api/?gender=female").json()