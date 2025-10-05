import requests
import json
import pandas as pd
#from pandas.io.json import json_normalize #package for flattening json in pandas df

# Random User Generator allows you to fetch up to 5,000 generated users in one request using the results parameter.
url = "https://randomuser.me/api/"

response = requests.get(url)
json_response = response.json()

# .keys() to see what the top level of the json is
print(json_response.keys())

# save the keys to pandas data frame
## response_csv = pd.DataFrame(json_response['results'])
## response_csv.to_csv("random_multiple_users_csv_file.csv")

# check data type
## print(type(json_response)) # <class 'dict'>

# convert to string
json_string_response = json.dumps(json_response)
## print(type(json_string_response)) # <class 'str'>



# write the result to a json file
with open("random_multiple_users_json_file.json", "w") as outfile:
    outfile.write(json_string_response) # write() argument must be str, not dict

df = pd.json_normalize("random_multiple_users_json_file.json", max_level=0)
print(df)
#random_multiple_users_df = pd.DataFrame(json_response['results'][0])
#print(random_multiple_users_df.head())
#random_multiple_users_df.to_csv("random_multiple_users_df.csv", index=True)

#csv_response = pd.read_json("random_multiple_users.json")
#csv_response.to_csv('random_multiple_users_file.csv', index=False)

# data = json.dumps(json_response)

#random_multiple_users = pd.read_json(random_multiple_users.json)
#random_multiple_users.to_csv("random_multiple_users", index = None)


