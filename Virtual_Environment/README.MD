# Python Virtual Environment

## Table of Contents
1. [Introduction to Virtual Environments](#Introduction-to-Virtual-Environments)
2. [Benefits of Python Virtual Environment](#Benefits-of-Python-Virtual-Environment)
3. [How Does a Virtual Environment Work?](#How-Does-a-Virtual-Environment-Work?)
4. [Requirements File](#Requirements-File)
5. [References](#References)
    - [](https://realpython.com/python-virtual-environments-a-primer/)
    - [freeCodeCamp](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

# Introduction to Virtual Environments
At its core, the main purpose of __Python virtual environments__ is to create an isolated environment for Python projects. This means that each project can have its own __dependencies__, regardless of what dependencies every other project has. i.e., when you activate a virtual environment for your project, your project becomes its own self contained application, independent of the system installed Python and its modules.

* Your new virtual environment has its own pip to install libraries, its own libraries folder, where new libraries are added, and its own Python interpreter for the Python version you used to activate the environment.

# Benefits of Python Virtual Environment
* development environment is contained within your project, becomes isolated, and does not interfere with your system installed Python or other virtual environments
* You can create a new virtual environment for multiple Python versions
* You are able to download packages into your project without admin privileges
* You can easily package your application and share with other developers to replicate
* You can easily create a list of dependencies and sub dependencies in a file, for your project, which makes it easy for other developers to replicate and install all the dependencies used within your environment
# How Does a Virtual Environment Work?
* To explain how this works, let’s first check out the locations of the different python executables. With the environment “deactivated,” run the following:
```shell
    which python # /c/Python/Python38-32/python
```

* Now, activate it and run the command again:
```shell
    # activate 
    source env/Scripts/activate
    which pyhton # /c/Users/RodgersNyangweso/Downloads/projects/Computer_Science_Concepts/Virtual_Environments/python_virtual_environments/\Users\RodgersNyangweso\Downloads\projects\Computer_Science_Concepts\Virtual_Environments\python_virtual_environments\env/Scripts/python
```
* After activating the environment, we’re now getting a different path for the python executable because, in an active environment, the $PATH environment variable is slightly modified.

# Requirements File
* Why is a requirements file important to your project? Consider that you package your project in a zip file (without the env folder) and you share with your developer friend.
* To recreate your development environment, your friend will just need to follow the above steps to activate a new virtual environment.
* Instead of having to install each dependency one by one, they could just run the code below to install all your dependencies within their own copy of the project:
```shell
    ~ pip install -r requirements.txt
```