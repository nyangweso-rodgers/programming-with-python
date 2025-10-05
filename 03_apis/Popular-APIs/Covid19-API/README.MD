# Coronavirus COVID19 API

## Table Of Contents
- [Further Reading]()
    - [API Documentation](https://documenter.getpostman.com/view/10808728/SzS8rjbc)

# Description

# Endpoints
# countries: 'https://api.covid19api.com/countries'
- Returns all the available countries and provinces, as well as the country slug for per country requests.

# summary: 'https://api.covid19api.com/summary'
- A summary of new and total cases per country updated daily.

# Day One Cases: https://api.covid19api.com/dayone/country/south-africa/status/confirmed
* Returns all cases by case type for a country from the first recorded case. Country must be the Slug from /countries or /summary. Cases must be one of: confirmed, recovered, deaths

* __Example__:_Returns all cases by case type for a country from the first recorded case. Country must be the Slug from /countries or /summary. Cases must be one of: confirmed, recovered, deaths_