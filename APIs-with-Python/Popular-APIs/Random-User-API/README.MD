# Random User API

## Table Of Contents
- [Documentation - Random User Generator](https://randomuser.me/documentation)

# RANDOM USER GENERATOR
* [RANDOM USER GENERATOR](https://randomuser.me/), is a free, open-source API for generating random user data. Like Lorem Ipsum, but for people.

# Query Parameters

* _Remarks_:
    - _To avoid having to rebuild the URL over and over again, you can use the __params__ attribute to send in a dictionary of all query parameters to append to a URL:_

        ```py
            # example of passing a query parameter
            query_params = {"gender": "female", "nat": "de"}
            requests.get("https://randomuser.me/api/", params=query_params).json()
        ```