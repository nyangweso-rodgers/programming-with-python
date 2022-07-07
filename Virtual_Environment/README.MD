# Python Virtual Environment

## Table of Contents
1. [Introduction to Virtual Environments](#Introduction-to-Virtual-Environments)
2. 

# Introduction to Virtual Environments
At its core, the main purpose of __Python virtual environments__ is to create an isolated environment for Python projects. This means that each project can have its own __dependencies__, regardless of what dependencies every other project has.

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

# References
1. https://realpython.com/python-virtual-environments-a-primer/