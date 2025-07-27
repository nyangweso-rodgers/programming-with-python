import pandas as pd
import requests
import json

# a summary of new and total cases per cointry updated daily
summary_url = 'https://api.covid19api.com/summary' # summary endpoint
global_summary_data = requests.get(summary_url).json()

    
# Transforming the json object to a Pandas DataFrame
countries_summary_data = pd.DataFrame(global_summary_data["Countries"])
countries_summary_data.to_csv("countries_summary_data.csv")

##print(countries_summary_data.info())
print(countries_summary_data.head())