# Python Virtual Environment

## Table of Contents
1. [Introduction to Virtual Environments](#Introduction-to-Virtual-Environments)
        - [Benefits of Python Virtual Environment](#Benefits-of-Python-Virtual-Environment)

2. [Components Of a Python Virtual Environment](#Components-Of-a-Python-Virtual-Environment)

3. [Benefits of Python Virtual Environment](#Benefits-of-Python-Virtual-Environment)

4. [Using Virtual Environments](#Using-Virtual-Environments)
        - [Creating Virtual Environments](#Creating-Virtual-Environments)
        - [Installing Packages](#Installing-Packages)

5. [Managing Environments](#Managing-Environments)
        - [Requirements File](#Requirements-File)
        - [Duplicating Environments](#Duplicating-Environments)
        - [Troubleshooting](#Troubleshooting)

6. [Further Reading]()
    - [freeCodeCamp](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
    - [A Guide to Python’s Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)

# Introduction to Virtual Environments
* A __virtual environment__ is a Python tool for __dependency management__ and __project isolation__. They allow Python __site packages__ (third party libraries) to be installed locally in an isolated directory for a particular project, as opposed to being installed globally (i.e. as part of a system-wide Python).

* At its core, the main purpose of __Python virtual environments__ is to create an isolated environment for Python projects. This means that each project can have its own __dependencies__, regardless of what dependencies every other project has. i.e., when you activate a virtual environment for your project, your project becomes its own self contained application, independent of the system installed Python and its modules.

* Your new __virtual environment__ has its own:
    - __pip__ to install libraries, 
    - __libraries__ folder, where new libraries are added, and its own 
    - __Python interpreter__ for the Python version you used to activate the environment.

# Components Of a Python Virtual Environment
1. A __site-packages/__ folder where third party libraries are installed
2. [Symlinks](https://en.wikipedia.org/wiki/Symbolic_link) to Python executables installed on your system.
3. [Scripts](https://en.wikipedia.org/wiki/Shell_script) that ensure executed Python code uses the Python interpreter and site packages installed inside the given virtual environment.

# Benefits of Python Virtual Environment
* development environment is contained within your project, becomes isolated, and does not interfere with your system installed Python or other virtual environments
* You can create a new virtual environment for multiple Python versions
* You are able to download packages into your project without admin privileges
* You can easily package your application and share with other developers to replicate
* You can easily create a list of dependencies and sub dependencies in a file, for your project, which makes it easy for other developers to replicate and install all the dependencies used within your environment
* Keep your global site-packages/ directory tidy by removing the need to install packages system-wide which you might only need for one project.

# Using Virtual Environments
# Creating Virtual Environments
* Say we wanted to create a virtual environment for a project we’re working on called __test-project/__, which has the following directory tree.

    test-project/

        |----date
        |----deliver # Final Analysis, code and presentations
        |----develop # Notebooks for exploratory analysis
        |----src # Scripts & Local projects modules
        |----tests

* All we need to do is execute the __venv__ module, which is part of the Python standard library.

    ```py
        cd test-project/
        python3 -m venv venv/ # Creates an environment called venv.
        # you can replace venv/ with a different name for your environment
    ```
* _Remark_: _A virtual environment is itself a directory._

* The only thing left to do is to “activate” our environment by running the scripts we mentioned earlier.

    ```py
        source venv/bin/activate
    ```

* At this point we would work on our project as usual, safe in the knowledge that our project is completely isolated from the rest of our system. Inside our environment we cannot access system-wide site packages and any packages we install will not be accessible outside of our environment.

* When we’re done working on our project, we can exit the environment with

    ```py
        deactivate
    ```
# Installing Packages
* By default, only __pip__ and __setuptools__ are installed inside a new environment.

    ```py
        pip list  # Inside an active environment
    ```

* If we want to install a specific version of a third party library, say v1.15.3 of __numpy__, we can just use __pip__ as usual.

    ```py
        pip install numpy==1.15.3
        pip list
    ```

* Now we can import __numpy__ in a script or active Python shell. For instance, say our project contains a script __tests/imports-test.py__ with the following lines.

    ```py
        #!/usr/bin/env python3       
        import numpy as np
    ```

* When we run this script directly from the command-line, we get:
    ```py
        tests/imports-test.py  
    ```

# Managing Environments

# Requirements File
* The easiest way to make our work reproducible by others is to include a requirements file in our project’s __root directory__ (top directory). To do so, we’ll run __pip freeze__, which lists installed third party packages along with their version numbers,

    ```py
        pip freeze
    ```
* And write the output to a file, which we’ll call __requirements.txt__.

    ```py
        pip freeze > requirements.txt
    ```
* We can use this same command to rewrite our requirements file whenever we update a package or install a new one.
* Now anyone we share our project with will be able to run our project on their system by duplicating our environment using our requirements.txt file.

# Duplicating Environments
* Imagine our teammate Sara has pulled down our __test-project/__ from our team’s GitHub repository. On her system the project’s directory tree looks like:

    test-project/

        |---data
        |---deliver
        |---develop
        |---requirements.txt
        |---src
        |---tests

* Notice anything slightly — unusual? Yep, that’s right. There’s no venv/ folder. We’ve excluded it from our team’s GitHub repository because including [it can cause headaches](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository)

* This is one reason having a __requirements.txt__ file is essential to reproducing your project’s code.

* To run our __test-project/__ on her machine, all Sara needs to do is to create a virtual environment inside the project’s root directory

    ```py
        Sara% cd test-project/
        Sara% python3 -m venv venv/
    ```

* And install the project’s dependencies inside an active virtual environment with the incantation __pip install -r requirements.txt__.

    ```py
        Sara% source venv/bin/activate
        (venv) Sara% pip install -r requirements.txt
    ```

# Troubleshooting
* Sadly, things don’t always go according to plan. Eventually you will run into problems. Maybe you’ve updated a particular site package by mistake and now find yourself in the ninth level of [Dependency Hell](https://en.wikipedia.org/wiki/Dependency_hell), unable to run a single line of your project’s code. Then again, maybe it’s not that bad. Maybe you only find yourself in the [seventh level](https://en.wikipedia.org/wiki/Inferno_(Dante)#Seventh_Circle_(Violence)).

* Whatever level you find yourself in, the easiest way to escape the flames and see the sun shine again is to __re-create__ your project’s virtual environment.

    ```py
        rm -r venv/   # Nukes the old environment
        % python3 -m venv venv/                 # Makes a blank new one
        % pip install -r requirements.txt       # Re-installs dependencies
    ```