import requests
import json
import pandas as pd


url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

headers = {
    "X-RapidAPI-Key": "a166e4462aa2e81ac1fdcd2a31a5992a",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
leagues_response = requests.request("GET",url, headers=headers)

json_leagues_response = leagues_response.json()
print(json_leagues_response)

# writing the output data to a local json file
with open('leagues_data_in_json.json', 'w') as c:
    json.dump(json_leagues_response, c)
    
# Transforming the json object to a Pandas DataFrame
leagues_summary_df = pd.DataFrame(json_leagues_response["response"])
leagues_summary_df.to_excel('leagues_data_in_excel.xlsx')