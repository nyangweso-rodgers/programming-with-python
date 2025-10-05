import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers.get("Content-Type")) # application/json; charset=utf-8

# Placegoadt API
another_response = requests.get("http://placegoat.com/200/200")
print(another_response.headers.get("Content-Type")) # text/html; charset=utf-8