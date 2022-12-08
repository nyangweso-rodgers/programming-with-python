# Python Frameworks

## Table Of Contents
- [Introduction to Python Frameworks](#Introduction-to-Python-Frameworks)
    - [Python: Framework vs. Libraries](#Python:-Framework-vs.-Libraries)
    
- [Django vs Flask vs FastAPI Framework Differences](#Django-vs-Flask-vs-FastAPI-Framework-Differences)

- [Further Reading]()
    - [Django vs Flask vs FastAPI Framework Differences](https://gankrin.org/django-vs-flask-vs-fastapi-framework-differences/)

# Introduction to Python Frameworks
* In general, all __frameworks__ from different programming languages have the same functions―to fast track development. __Python frameworks__ are no different; they are a collection of modules and packages.

* These frameworks automate common processes and implementation. For instance, developers can focus on application logic rather than dealing with routinary processes.

# Python: Framework vs. Libraries
* The major difference between __frameworks__ and __libraries__ is complexity. __Libraries__ offer fewer complexities, and __frameworks__ are the opposite. A __library__ is a _collection of packages that performs specific operations_.

* On the other hand, __frameworks__ _contain the basic flow and architecture of the application. But, developers need to build the rest of the functionalities_.

* _Control is also a key difference between these two_. When a developer calls a method from a library, the developer is in control of the development process. With frameworks, it is the one calling. It means that the frameworks call the processes, and the control lies in the framework.

* However, frameworks are often used because of their key advantage―flexibility. They are extensible and provide the necessary tools to extend their features. Unlike libraries, developers need to learn each functionality to perform certain operations.
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