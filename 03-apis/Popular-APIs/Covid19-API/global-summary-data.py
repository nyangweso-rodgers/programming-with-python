import requests
import json
import pandas as pd

# endpoint
summary_url = 'https://api.covid19api.com/summary'
global_summary_data = requests.get(summary_url).json()


# writing the output data to a local json file
with open('global_summary_data.json', 'w') as c:
    json.dump(global_summary_data, c)
    
    
# preview
print(pd.DataFrame(global_summary_data['Global'], index=[0]).stack())