# Python Frameworks

## Table Of Contents

# Introduction to Python Frameworks

- In general, all **frameworks** from different programming languages have the same functions―to fast track development. **Python frameworks** are no different; they are a collection of modules and packages.

- These frameworks automate common processes and implementation. For instance, developers can focus on application logic rather than dealing with routinary processes.

# Python: Framework vs. Libraries

- The major difference between **frameworks** and **libraries** is complexity. **Libraries** offer fewer complexities, and **frameworks** are the opposite. A **library** is a _collection of packages that performs specific operations_.

- On the other hand, **frameworks** _contain the basic flow and architecture of the application. But, developers need to build the rest of the functionalities_.

- _Control is also a key difference between these two_. When a developer calls a method from a library, the developer is in control of the development process. With frameworks, it is the one calling. It means that the frameworks call the processes, and the control lies in the framework.

- However, frameworks are often used because of their key advantage―flexibility. They are extensible and provide the necessary tools to extend their features. Unlike libraries, developers need to learn each functionality to perform certain operations.

# Python Web Frameworks

## 1. FastAPI

- **FastAPI** is a **web development framework** for **Python 3.6** and newer versions. It was released in **2018** as an open source framework built on [Starlette](https://starlette.io/) and uses standard Python type hints. The framework is used primarily for building fast **web applications** and **Rest APIs**.
- **FastAPI** is built on the **Asynchronous Server Gateway Interface** (**ASGI**) web server **Uvicorn**, but you can also mount **Web Server Gateway Interface** (**WSGI**) applications using relevant middleware.
- **Pros of FastAPI**:

  1. **High performance with Asynchronous Programming**:

     - It's the quality by which **FastAPI** beats **Flask**.
     - This superior performance is enabled precisely by **ASGI**, thanks to which **FastAPI** supports **concurrency** and **asynchronous** code. This is achieved by declaring the endpoints with `async def` syntax.

  2. **Native Concurrency Support**:

     - Async I/O was added with **Python 3.4**. With **FastAPI**, **concurrency** can be easily implemented without worrying about Event loop or async/await management.
     - Developers can simply declare the first path function as coroutines via the async def function wherever they deem appropriate and then declare specific points aws awaitable through await.

  3. **Simple to use dependency injection**:

     - FastAPI offers a simple and easy-to-use dependency injection system.
     - **Dependency injection** is a compositional way of declaring the necessary components required for the code to run properly.
     - In **FastAPI**, developers can simply declare relevant dependencies in the path operation functions assigned to the API endpoints.

  4. **Inbuilt documentation support**

     - **FastAPI** offers an extremely handy automatic documentation system. It provides a browser-based user interface that interactively documents an API, powered by Swagger UI GUI.
     - Alternatively, developers can simply type in /redoc to obtain the alternative documentation consisting of all the endpoints listed. The documentation will always allow developers to easily explain the program to others, make it easier for front-end engineers to use your backend and add convenience when it comes to testing the API endpoints.

  5. **Inbuilt data validation**:
     - inbuilt data validation allows developers to create a compact code through skipping the validation. It can detect invalid datatypes during the run and returns the reason for bad input in JSON format.
     - **FastAPI** makes use of the [Pydantic](https://docs.pydantic.dev/latest/) library for this purpose, which greatly simplifies the validation process and ensures faster typing than it would have been by hand.

- **Cons of FastAPI**

  1. **Lack of inbuilt security system**
     - **FastAPI** doesn't offer a built-in security system. Instead, it provides a `fastapi.security` module for security mechanisms. At the same time, it does support **OAuth2.0**.

- **Features**:
  1. **Web-Server Integration**: Supports **ASGI** (**Asynchronous Sever Gateway Interface**.) But you can mount WSGI application using Middleware
  2. **REST Development**: Faster development of REST APIs
  3. **Templating Engine**: FastAPI supports **Jinja2** and **alofiles**
  4. **Security**: Less secure compared to Django. Provides `fastapi.security` module for security mechanisms
  5. **ORM Availability**: Doesn't come with any built-in ORM. But you can use **Flask-SQLAlchemy**, **Flask-Pony** e.t.c, with it.
  6. **Modern and High-Performance Web Framework**: FastAPI is designed for speed and efficiency, leveraging modern Python features.
  7. **Built on Standard Python Type Hints**: It uses Python type hints to provide better code clarity and automatic data validation.
  8. **Supports Asynchronous Tasks and Programming**: FastAPI natively supports asynchronous programming, making it ideal for high-performance applications.
  9. **Built-In Support for Data Validation**: FastAPI uses Pydantic for automatic data validation, reducing the need for manual checks.
  10. **Automatic Generation of OpenAPI Documentation**: It automatically generates interactive API documentation, simplifying the development and testing process.
  11. **Multiple HTTP Methods**: Like Flask, FastAPI supports various HTTP methods, offering flexibility in API design.

# 2. Flask

- **Flask** is a micro framework written for Python. It’s lightweight, open source and offers a small and easily extensible core. It’s used primarily to develop minimalistic web applications and Rest APIs.
- **Flask** was released in 2010 as a framework based on **Werkzeug** and **Jinja2**. It’s built on **Web Server Gateway Interface** (**WSGI**). You can use an **ASGI** server with **Flask**, but you’d need to utilize **WSGI** to **ASGI** middleware.
- The framework supports REST development through extensions, eg. **Flask-RESTful**, **Flask-Classful**, **Flask-RESTPlus**, etc. It’s perfect for building e-commerce systems, social media bots or static sites. It’s not suitable for high-load enterprise software.
- **Pros of Flask**

  1. **Great for building scalable solutions**

     - **Flask** applications are easily and extensively scalable. The framework supports the creation of complex applications by allowing developers to easily add new functionalities and use cases as needed. Flask is thus a great option for businesses that are starting small and intend to grow their new solution in the coming years.

  2. **Ample resources available**

  3. **Great flexibility**:

     - Developers will certainly enjoy the fact that most parts of **Flask** can be changed, which is rather rare in case of most other development frameworks. This is one of the greatest advantages of **Flask**

  4. **Security**:
     - **Flask** may be a minimalist framework, but it's well equipped to handle common security concerns like CSRF, XSS or JSON security. Developers can benefit from 3rd party extensions like [Flask-Security](https://pythonhosted.org/Flask-Security/) as well, but they should be aware that adding these can result in performance drop.

- **Cons of Flask**

  1. **Lack of support for asynchronicity**:

     - **Flask** is developed for **WSGI services** like **Gunicorn**, and so it doesn't offer native async support. This means that long-running queries may actually block the application. A **REST API** built with Flask will be able to handle a smaller number of users. All in all, every request will be handled in turns, which takes more time.

  2. **Modules**

     - **Flask** makes use of third-party modules and that increases the risk of security breaches. Applying modules means that the development process isn't solely between the developer and the framework. If a malicious module is implemented, the consequences can be grave, so programmers must pay extra attention to security mechanisms.

  3. **Lack of data validation**
     - Validation of the data format is absent in **Flask**, which means that developers can pass any type of data, including strings or integers. There are extensions that can compensate for this shortcoming, eg. Flask-Marshmallow or Flask-inputs. Alternatively, developers can add a validation script for data inputs, but this will require additional effort.

- **Features**:
  1. **Web-Server Integration**: Supports **WSGI** (Web** Server Gateway Intrface**). But if you would like to use an **ASGI server** you will need to utilise **WSGI to ASGI middleware**
  2. **Rest Development**: REST development is supported through extensions e.g., Flask-RESTful, Flask-Classful, Flask-RESTPlus e.t.c.,
  3. **Templating Engine**: Flask uses **Jinja2**
  4. **Security**: Less secure compared to **Django** but can handle common security comcerns like **CSRF**, **XSS**, **JSON Security** e.t.c., However, developer intervention is required for addressing security loopholes and vulnerabilities
  5. **ORM Availability**: Doesn't come with any built-in ORM. But you can use:
     1. Flask-SQLAlchemy,
     2. Flask-Pony e.t.c, with it.
  6. **Micro Web Framework**: **Flask** is a lightweight and easy-to-use micro web framework that provides the essentials for web development.
  7. **Lightweight and Flexible**: Its minimalistic core allows developers to build applications quickly and extend them as needed.
  8. **Extensible**: Flask supports a wide range of extensions, enabling developers to add functionalities like database integration, form validation, and more.
  9. **Multiple HTTP Methods**: It supports various HTTP methods, making it versatile for different types of web applications.
  10. **No Built-In Support for Asynchronous Tasks**: Flask does not natively support asynchronous programming, which can be a limitation for high-performance applications.
  11. **No Built-In Support for Data Validation**: Developers need to rely on third-party libraries for data validation.

## 3. Django

- **Features**:
  1. **Web-Server Integration**: Supports both **WSGI** (**Web Server Gateway Intrface**) & **ASGI**
  2. **Rest Development**: REST development is not built-in. But is supported through DRF- Django REST Framework project
  3. **Templating Engine**: Have it's own template engine. Also configurable with **Jinja2**
  4. **Security**: Comparatively more secure than other two frameworks. Because of Django's built in system, it can prevent security breach to a good extent
  5. **ORM Availability**: Comes with a built-in ORM framework out of the box

# Resources and Further Reading

1. [FastAPI vs Flask: Which Should You Choose?](https://www.netguru.com/blog/python-flask-versus-fastapi?ref=dailydev)
