# Python

## Table of Contents

1. [Python - Getting Started]()

2. [Programming Paradigms in Python](#Programming-Paradigms-in-Python)

- [References]()
  - [Building modern Python API backends in 2022](https://sanjeevan.co.uk/blog/modern-python-backends)
  - [Python Project Ideas to Improve Your Résumé](https://www.freecodecamp.org/news/python-project-ideas-to-improve-your-resume/)
  - [140 Python Projects with Source Code](https://medium.datadriveninvestor.com/140-python-projects-with-source-code-fa12c9e2aeac)
  - [Backend Web Development with Python - Full Course](https://www.freecodecamp.org/news/backend-web-development-with-python-full-course/)

# Introduction to Python Programming Language

## How Python Works

- The python **source code** is first compiled into **Byte Code**. Though Python is an **interpreted language**, it first gets compiled into **byte code**. This byte code is then interpreted and executed by the **Python Virtual Machine**.

- This compilation and execution are what make Python slower than other low-level languages such as C/C++. In languages such as C/C++, the **source code** is compiled into **binary code** which can be directly executed by the CPU thus making their execution efficient than that of Python.

## `Pip` vs `Conda`: an in-depth comparison of Python’s two packaging systems

- `pip` is a package manager for Python. That means it’s a tool that allows you to install and manage additional libraries and dependencies that are not distributed as part of the standard library. JavaScript uses `npm` for package management, Ruby uses `gem`, and **.NET** use `NuGet`.
- In **Python**, `pip` has become the **standard package manager**.

- The fundamental difference between **pip** and **Conda** packaging is what they put in packages. **Pip packages** are **Python librarie** like `NumPy` or `matplotlib`. **Conda packages** include Python libraries (NumPy or matplotlib), C libraries (libjpeg), and executables (like C compilers, and even the Python interpreter itself).

# How to Configure VS Code for Python Development Environment

## Python Extensions

1. Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Microsoft.

   - This is actually an extension pack that contains two extensions.
     - The first extension is the Python extension. It lays the foundation for Python development in Visual Studio Code.
     - The other one is [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), which is a very performant language server for Python.

2. **Ruff Linter**

   - Ruff is an extremely fast Python linter written in Rust that imposes stricter linting rules than Pylint.
   - Install [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

3. **Isort**:

   - Like a linter, [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) is another utility that's sole purpose is sorting import statements.
   - The utility sorts all the imports alphabetically, while also dividing them into sections.

4. **InteiCode**

   - [InteiCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) provides AI assisted code completion in Visual Studio Code.

5. **Error Lens**

   - While not related to Python specifically, [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) is a great extension that embeds errors right by the side of the line of code.

6. **Indent Rainbow**
   - [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) adds some color to the identation.

# Resources
