# Python - Getting Started

## Table Of Contents


# Introduction to Python
* __Python__ was originally designed as a scripting language and is still used that way. To make small programs that do small but necessary tasks such as _automation_ or _data science_.

# How Python Works
* The python __source code__ is first compiled into __Byte Code__. Though Python is an __interpreted language__, it first gets compiled into __byte code__. This byte code is then interpreted and executed by the __Python Virtual Machine__.

* This compilation and execution are what make Python slower than other low-level languages such as C/C++. In languages such as C/C++, the __source code__ is compiled into __binary code__ which can be directly executed by the CPU thus making their execution efficient than that of Python.

# Cons of using Python
* __Slow__: python is an __interpreted language__. i.e., it's source code gets executed without first compiling a program into machine-language instructions.

* __Dynamic Type Checking__: i.e., type checking is performed at run time, and this increase memory consumption and slows down the operations.

# Pip vs Conda: an in-depth comparison of Python’s two packaging systems
* __pip__ is a package manager for Python. That means it’s a tool that allows you to _install_ and _manage_ additional _libraries_ and _dependencies_ that are not distributed as part of the standard library.__JavaScript__ uses __npm__ for package management, __Ruby__ uses __gem__, and __.NET__ use __NuGet__. In __Python__, __pip__ has become the __standard package manager__.

* The fundamental difference between __pip__ and __Conda__ packaging is what they put in packages. __Pip packages__ are _Python libraries_ like NumPy or matplotlib. __Conda packages__ include Python libraries (NumPy or matplotlib), C libraries (libjpeg), and executables (like C compilers, and even the Python interpreter itself).