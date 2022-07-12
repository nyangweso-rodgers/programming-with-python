# Python and REST APIs: Interacting with Web Services
By using __Python__ and __REST APIs__, you can _retrieve_, _parse_, _update_, and _manipulate_ the data provided by any __web service__ you’re interested in.

# Requests
A __request__ is made up of four different pieces:
1. An __endpoint__ — which looks like the __URL__ to the data
2. A __method__ — either _GET_, _PUT_, _POST_, or _DELETE_.
3. The __headers__ — which provide information such as _authentication keys_.
4. The __data/body__ — which isn’t part of a GET request.

When we run a request using the __requests__ library, it returns a __request object__, which includes the data we’re hoping to extract, but also a requests status code. The status code tells us what happened with the request and they are a part of every request that we make.



# References
1. [Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/)
2. [Benefits of REST API](https://www.freecodecamp.org/news/benefits-of-rest/)