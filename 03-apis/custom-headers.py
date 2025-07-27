import requests

headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
print(response.request.headers)