import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers.get("Content-Type"))

print(response.content)

print(response.json())
print(response.json()["name"])