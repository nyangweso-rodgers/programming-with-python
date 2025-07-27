# day one cases in Kenya

import requests
import pandas as pd

kenya_url = 'https://api.covid19api.com/dayone/country/kenya'
kenya_daily_cases = requests.get(kenya_url).json()

kenya_daily_cases_df =pd.DataFrame(kenya_daily_cases)

# save results to a csv file
kenya_daily_cases_df.to_csv("day_one_cases_data.csv")

# preview the data
print(kenya_daily_cases_df.head())