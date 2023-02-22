import requests

# get information for a specifc GitHub User, e.g., Rodgers Nyangweso
github_url = "https://api.github.com/users/nyangweso-rodgers"
github_response = requests.get(github_url)

# view the data in jason
print(github_response.json())