import requests

# using query parameters
query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
print(requests.get(endpoint, params=query_params).json())