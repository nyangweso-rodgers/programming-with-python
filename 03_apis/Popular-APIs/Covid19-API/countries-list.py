import requests
import pandas as pd
import json

# Getting List of Countries Under the API
# Returns all the available countries and provinces, as well as the country slug for per country requests.

# getting lists of Countries
countries_url = 'https://api.covid19api.com/countries' # endpoint
countries_data = requests.get(countries_url).json()

# writing the output data to a local json file
with open('countries_lists_in_json.json', 'w') as c:
    json.dump(countries_data, c)

# transforming the json file to Excel using Pandas
pd.read_json("countries_lists_in_json.json").to_csv("countries_lists_in_csv.csv")