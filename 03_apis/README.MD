# APIs - Python

## Table Of Contents
- [Further Reading]()
    - []()

# Query Parameters
* In the API world, __query parameters__ are used as filters you can send with your API request to further narrow down the responses.

* Using query parameters, you can start fetching more specific data from an API, making the whole experience a bit more tailored to your needs.

# Custom Headers
* These usually start with X-, but they’re not required to. API developers typically use __custom headers__ to send or request additional custom information from clients. You can use a dictionary to define headers, and you can send them along with your request using the headers parameter of __.get()__.

* _For example_, say you want to send some request ID to the API server, and you know you can do that using X-Request-Id:

    ```py
        headers = {"X-Request-Id": "<my-request-id>"}
        response = requests.get("https://example.org", headers=headers)
        response.request.headers
    ```

* If you go through the request.headers dictionary, then you’ll find X-Request-Id right at the end, among a few other headers that come by default with any API request.

* There are many useful headers a response might have, but one of the most important ones is __Content-Type__, which defines the kind of content returned in the response.

# Content Type
* These days, most __APIs__ use __JSON__ as the default __content type__, but you might need to use an API that returns XML or other media types, such as images or video. In that case, the content type will differ.

* If, for example, you try to fetch an image of a goat from the PlaceGOAT API, then you’ll notice that the content type is no longer application/json, but instead it’s defined as __image/jpeg__:

    ```py
        response = requests.get("http://placegoat.com/200/200")
        response.headers.get("Content-Type") # 'text/html; charset=utf-8'
    ```

# Response Content
* the type of content you find in the API response will vary according to the __Content-Type__ header. To properly read the response contents according to the different __Content-Type__ headers, the requests package comes with a couple of different __Response__ attributes you can use to manipulate the response data:

- __.text__ returns the response contents in __Unicode__ format.
- __.content__ returns the response contents in __bytes__.

* for some specific types of data, like images and other nontextual data, using __.content__ is typically a better approach, even if it returns a very similar result to .text: