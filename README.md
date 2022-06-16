# Python Projects
## Table of Contents
1. [Introduction to Python](#Introduction-to-Python)
    - [How Python Works](#How-Python-Works)
    - [Pros of using Python](#Pros-of-using-Python)
    - [Cons of using Python](#Cons-of-using-Python)
- [pip](#PIP)
- [References](#References)
# Introduction to Python
__Python__ was originally designed as a scripting language and is still used that way. To make small programs that do small but necessary tasks such as _automation_ or _data science_.

# How Python Works
The python __source code__ is first compiled into __Byte Code__. Though Python is an __interpreted language__, it first gets compiled into __byte code__. This byte code is then interpreted and executed by the __Python Virtual Machine__.

This compilation and execution are what make Python slower than other low-level languages such as C/C++. In languages such as C/C++, the __source code__ is compiled into __binary code__ which can be directly executed by the CPU thus making their execution efficient than that of Python.

# Pros of using Python
* __Code Readability__: with simple and elegant syntax
* __Object Oriented__: Python supports several programming paragigms:
    - Object-oriented
    - Procedural programming
    - Functional programming
* __Huge standard library__: more than 200,000 third party packages to offer, most popular ones being:
    - Django (Django Rest Framework)
    - Flask
    - FastAPI
    - Keras
    - TensorFlow
* Community and Sustainability
* Development Efficiency

# Cons of using Python
* __Slow__: python is an __interpreted language__. i.e., it's source code gets executed without first compiling a program into machine-language instructions.
* __Dynamic Type Checking__: i.e., type checking is performed at run time, and this increase memory consumption and slows down the operations.

# Pip vs Conda: an in-depth comparison of Python’s two packaging systems
__pip__ is a package manager for Python. That means it’s a tool that allows you to _install_ and _manage_ additional _libraries_ and _dependencies_ that are not distributed as part of the standard library. The concept of a __package manager__ might be familiar to you if you are coming from other languages. __JavaScript__ uses __npm__ for package management, __Ruby__ uses __gem__, and __.NET__ use __NuGet__. In __Python__, __pip__ has become the __standard package manager__.

The fundamental difference between __pip__ and __Conda__ packaging is what they put in packages. __Pip packages__ are _Python libraries_ like NumPy or matplotlib. __Conda packages__ include Python libraries (NumPy or matplotlib), C libraries (libjpeg), and executables (like C compilers, and even the Python interpreter itself).


# Django vs Flask vs FastAPI Framework Differences
** | Django | Flask | FastAPI
|:------:|:---------:|:----------:|:----------:|
Definition | Cross - Platform, open -source Web frameworks based on Python | Open - source, Light-weight micro web framework - based on Python - with small and easily extensible core | Open Source and fast - Comparatively newer web framework based on Python 3.6+ onwards. (Doesn't work with Python3.5 or earlier versions)
Use Case | Used to develop Full-stack, web applications and REST APIs | Used to develop minimilistic web applications and REST APIs | Used to develop fast web applications and REST APIs
Web-Server Integration | Supports both WSGI (Web Server Gateway Intrface) & ASGI | Supports WSGI (Web Server Gateway Intrface). But if you would like to use an ASGI server you will need to utilise WSGI  to ASGI middleware | Supports ASGI (Asynchronous Sever Gateway Interface.) But you can mount WSGI application using Middleware
REST Development | __REST__ development is not built-in. But is supported through __DRF- Django REST Framework__ project | __REST__ development is supported through extensions e.g., Flask-RESTful, Flask-Classful, Flask-RESTPlus e.t.c., | Faster development of __REST APIs__
Data Validation | Data validation facility available | No data validation | data va;idation facility available - even for nested JSON Requests
*** | Django follows an MVT (Model View-Template) format that involves adhering to some specific pathways which renders lesser flexibility to the developers | More flexible than Django | Very flexible for development. Lesser restriction on the code layout - hence is also flexible code-wise
Templating Engine | Have it's own template engine. Also configurable with Jinja2 | Flask uses Jinja2 | FastAPI supports Jinja2 and alofiles
Security | Comparatively more secure than other two frameworks. Because of Django's built in system, it can prevent security breach to a good extent | Less secure compared to Django but can handle common security comcerns like CSRF, XSS, JSON Security e.t.c., However, developer intervention is required for addressing security loopholes and vulnerabilities | Less secure compared to Django. Provides fastapi.security module for security mechanisms
Uses | Used for both frontend and backend development. Hence robust full-stack apps with several functionalities could be built. Django woeks quite well in production | Good choice - if a simple micro-service with couple of API endpoints - is the need. Also used for building Data Science - Machine Learning models Web applications Prototypes within much lesser time | FastAPI cab be chosen when speed and performance is of primary importance
ORM Availability | Comes with a built-in ORM framework out of the box | Doesn't come with any built-in ORM. But you can use Flask-SQLAlchemy, Flask-Pony e.t.c, with it. | Doesn't come with any built-in ORM. But you can use Flask-SQLAlchemy, Flask-Pony e.t.c, with it.
Database support | Supports usage of NoSQL through open-source projects - PynamoDB | Supports NoSQL databases through open source libraries - PyMongo, Flask-CQLAlchemy etc., | Can be integrated with any NoSQL. Supports MongoDB, Cassandra, CouchDB, ElasticSearch, e.t.c.,
Performance | Not as fast as the other two frameworks. However, the differences could be noticeable to negligible based on real-world use cases. | Comparatively faster than Django for minimilistic projects. However, extension could result in a performance drop. | It is the fastest -  Beats the other two frameworks in its High Performance aspect. 
Testing | we can use Python's unittest framework | For testing, we can use Python's unittest and pytest framework | For testing, we can use Starlette and pytest frameworks

# References
1. [Getting Started with pip](https://realpython.com/what-is-pip/)
2. [Django vs Flask vs FastAPI Framework Differences](https://gankrin.org/django-vs-flask-vs-fastapi-framework-differences/)
3. [pip vs conda](https://pythonspeed.com/articles/conda-vs-pip/)
4. [asyc and wait in Python](https://www.quora.com/)
5. [Python Documentation](https://www.python.org/doc/)
6. [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
