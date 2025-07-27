# Dog API

## Table Of Contents
- [Documentation](https://thedogapi.com/)


# API Description
* API All about Dogs

# Endpoints
* [Breeds Endpoint](https://api.thedogapi.com/v1/breeds)

# Using Query Parameters
* for the __TheDogAPI__, the documentation has a way for you to [filter the breeds endpoint](https://docs.thedogapi.com/api-reference/breeds/breeds-search) to return only the breeds that match a specific name. 

* For example, if you wanted to look for the Labradoodle breed, then you could do that with the query parameter q:

    ```py
        query_params = {"q": "labradoodle"}
        endpoint = "https://api.thedogapi.com/v1/breeds/search"
        requests.get(endpoint, params=query_params).json()
    ```