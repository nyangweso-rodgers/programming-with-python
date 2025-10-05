import requests
import json

# calling the base url
base_url = 'https://api.thedogapi.com/'
breeds_url = "https://api.thedogapi.com/v1/breeds"

response = requests.get(base_url)
response_from_breeds = requests.get(breeds_url)

print(response) # <Response [200]> 
print(response.text) # {'message': 'The Dog API', 'version': '1.2.0'}

"""
In this case, when calling the base URL, you get this generic message saying The Dog API. 
This is because you’re calling the base URL, which is typically used for very basic information about an API, not the real data.
"""

# Response and Requests Attributes

# response
print(response_from_breeds) # <Response [200]>

# request
request = response_from_breeds.request
print(request) # <PreparedRequest [GET]>

# url
print(request.url) # https://api.thedogapi.com/v1/breeds

# path url
print("Path URL: ", request.path_url) # /v1/breeds


# method
print("Method: ", request.method) # GET

# request headers
print("Requests Headers ", request.headers) #

# response headers
print("Response Headers: ", response_from_breeds.headers)

# response status code
print("Response Status Code: ", response_from_breeds.status_code)

# response status code reason
print("Response Status Code: ", response_from_breeds.reason)