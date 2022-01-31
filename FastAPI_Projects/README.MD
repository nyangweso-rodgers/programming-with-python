# FastAPI

# Contents
- [Introduction](#Introduction)
- [Features of FastAPI](#Features-of-FastAPI)
- [Installation](#Installation)
- [References](#References)

# Introduction
__FastAPI__ is a modern, fast and performance web framework for building API's with Python. __FastAPI__ supports __concurrency and coroutines__ without importing asyncio package.

__FastAPI__ is one of the _fastest Python frameworks_ available. Faster than __Express__ or __Nest JS__.

__FastAPI__ uses (__ASGI__),__Asynchronous Server Gateway Interface__ which is the standard interface between __FastAPI app__ and the __server__. __UVICORN__ is the fast ASGI server implementation. __ASGI__ helps enable an ecosystem of Python web frameworks that are highly competitive against __Node__ and __Go__.

# Features of FastAPI
* __OpenAPI for API creation__, including declarations of path operations, parameters, body requets e.t.c.,
* Automatic data model documentation with __JSON Schema__ (as OpenAPI itself is based on JSON Schema)
* __Automatic docs:__ Interactive API documentation.
* No new stntax to learn. Just standard modern Python.

# Installation
Because __firstAPI__ is a Python framework, we're gonna use the Python package manager, which is __Pip__.
1. On the command prompt, type:
```pip
python -m pip install fastapi
```

Because working with __fastAPI__ is a very light library, So you need like an external library just to run that file on the __web server__. So this __UV con__ is going to allow us to run our __firstAPI__ project or file on the web server.

2. Install __uvicorn__:
```
pip install uvicorn
```
Now, if you work with other libraries, like for example, __Django__,you don't need to install any external team to run it or your web server.

# References
1. [](https://www.freecodecamp.org/news/fastapi-helps-you-develop-apis-quickly/)