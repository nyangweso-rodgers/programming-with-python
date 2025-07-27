# Python Packages

## Table Of Contents

# Starting with Modules

- **Modules** are the building blocks of a **Python Package**. A **Module** is a single Python file that contains definitions and statements. They provide a way to structure your code into logical units and reuse code across multiple projects.
- To use a module in your code, you use the import statement.

  ```py
      import <modele_name>
  ```

* Once you have imported a **module**, you can access its functions and variables using the dot `(.)` notation.

  ```py
      import mymodule
      mymodule.greet("John")
  ```

- **From Modules to Packages**: As code grows, it can become difficult to manage and maintain all the code in a single **module**. **Packages** provide a way to organize and split your code into multiple **modules**, while still keeping everything organized and accessible.

# What is a Package?

- **Package** is a collection of files and dictionaries that include the code, documentation and other necessary files.
- We put a **Python Code** into **packages** to make it easy to share and reuse code.
- Think of a Python Package as a standalone "project". A _project_ can contain multiple `modules`, each of which contains a specific set of related `functions` and `variables`.
- **Why use a Python Package?**

  - We use **Python packages** instead of **script files** and **Jupyter notebooks** when we want to reuse complex code. With **script files**, code can become cluttered and difficult to maintain, while **notebooks** are often used for exploratory work but are not easily reusable.

- **How to create a Package**
  - To create a **package**, simply create a directory and place one or more **modules** in it.
  - The directory should contain a special file called `__init__.py`, which tells Python that this directory is a **package** and should be treated as such.
  - The `__init__.py` file can be left empty or it can contain code that will be executed when the package is imported.

# What is `__init__.py`?

- `__init__.py` is a special file in Python packages that serves as an entry point for the package. It is executed when the package is imported, and its code can be used to initialize the package or set up any necessary components. The file is optional, but is often used to define the public interface of the package, making it easier for other developers to understand and use the package.

- Here's an example of how you could use `__init__.py` package.

  ```python
      from .examplemodule import greet, add
      __all__ = [
          'greet',
          'add'
      ]
  ```

- In this example, the `__init__.py` file imports the `greet` and `add` functions from the `examplemodule.py` file and makes them part of the public interface of the package. The `__all__` variable is used to define the public interface of the package, and makes it easier for other developers to understand and use the package.

- With this setup, you can now import the `greet` and `add` functions from the `examplepackage` as follows:

  ```py
      import examplepackage
      examplepackage.greet("John")
      examplepackage.add(1, 2)
  ```

# How do you manage packages in Python?

- The most common way developers distribute their **packages** is by uploading them to a public repository called the [Python Package Index (PyPI)](https://pypi.org/)
- We use a system called `pip` (**Pip Installs Packages**). It is a command-line tool that allows users to install and manage packages from **PyPI** and other package indexes.
- Package management systems like `pip` make it easy to **install**, **update**, and **remove packages**, as well as manage dependencies (packages that are required for other packages to function properly) in a project.

- **How `pip` work?**

  - `pip install` is the command we use to download and install different packages from a library called **PyPI** or even from your own computer. When you run this command, it will check if the package is available on **PyPI** and if so, it will download and install it on your computer. In addition, it will check on - and if needed install - all the dependencies listed in the package metadata. Finally, `pip` will keep track of all the packages you install to help you **upgrade** or **uninstall** them later.
  - By default, `pip` install installs the latest version of the package, but you can choose to install a specific version if you need to by using `pip install <PACKAGE>==<VERSION>` e.g., `pip install numpy==1.23.5`
  - Have you ever noticed that when you use `pip install` to add a feature to your Python code, the name you use to install it is different from the name you use when you import it? This happens because there are two types of names:
    - the **distribution name**, which is the name you use to install the package `using pip install`
    - the **package name**, which is the name you use when you import the package in your code.
    - The **distribution name** is unique and guaranteed to be different from other package names by **PyPI**, the library where you get your packages from. On the other hand, the **package name** is chosen by the person who created the package, so it may not be unique.
    - This is why you might install a package "`scikit-learn`" using `pip install`, but import it in your code using the name "`sklearn`".

# What are relative vs. absolute imports?

- When writing a package, there may be times when we want to import code from another module within the same package. We’ll need to choose between two different ways of importing modules or packages in Python, either _relative imports_ or _absolute imports_.

- [Relative imports](https://docs.python.org/3/reference/import.html#package-relative-imports) consist of either _explicit_ or _implicit_ imports, but you really only need to know about _explicit relative imports_ as _implicit relative imports are not supported in Python 3_.

- **Relative imports** allow you to import modules _relative to the current module_. They use the keyword "`from`" followed by the name of the current package and the name of the module or package being imported. For example, if you have a package named `examplepackage` with two modules, `module1.py` and `module2.py`, you can import the code from `module1.py` into `module2.py` using a _relative import_ as follows:

  ```py
      # examplepackage/module2.py

      from .module1 import greeting
      def greet(name):
          print(greeting + " " + name)
  ```

- Here, the relative import `from .module1 import greeting` is used to import the `greeting` variable from the `module1.py` file into the `module2.py` file. The `.` before `module1` indicates that the import should be _relative_ to the current module.

- **Absolute imports** allow you to import modules using their full name, regardless of their location relative to the current module. They use the the full path of the module or package being imported. For example, you could use an absolute import to access the `greeting` variable from the `module1.py` file into the `module2.py` file as follows:

  ```py
      # examplepackage/module2.py

      from examplepackage.module1 import greeting
      def greet(name):
          print(greeting + " " + name)
  ```

- Here, the _absolute import_ `from examplepackage.module1 import greeting` is used to import the `greeting` variable from the `module1.py` file into the `module2.py` file. The full name of the module, `examplepackage.module1`, is used to specify the location of the module.

- In **Python 3**, relative imports must be explicit and the absolute imports are the default behavior.

# Dependencies

- **Dependencies** are other packages that your package relies on to work correctly.
- One of the tools to help with in managing dependencies is **Python Package Index(PyPI)**, which is a central repository of open-source Python packages. You can use **PyPI** to search for packages that you can include in your project and to make your own packages available to others.

- **Managing Dependencies the Old Way**: `setup.py`

  - `setup.py` is a file that you include in the root of your project, which contains information about your package and its dependencies. The file is used by `pip`, the package installer for Python, to install your package and its dependencies.
  - Here is an example of a `setup.py` file:

    ```py
        from setuptools import setup, find_packages

        setup(
            name="your package name",
            version="0.0.1",
            description="your package description of your package",
            author="your name",
            author_email="your email",
            packages=find_packages(),
            install_requires=[
                'dependency1',
                'dependency2',
            ],
        )
    ```

    - `name` and `version` are required fields that specify the `name` and `version` of your package.
    - `description` field provides a brief `description` of your package.
    - `author` and `author_email` fields specify the name and email address of the person responsible for the package.The `packages` field specifies the packages that are included in your project. The `find_packages()` function is used to automatically find all packages in your project.
    - The `install_requires` field is a list of dependencies that your package needs in order to run correctly. In this example, the package depends on two other packages, dependency1 and dependency2.

  - To install the **dependencies** of your package, you can run the following command:

    ```sh
        # install dependencies
        pip install -e .
    ```

    - The `-e `option tells pip to perform an "editable" install, which allows you to make changes to your package without having to reinstall it. The `.` at the end of the command specifies the current directory, which is the root of your package.
    - It is important to note that when you run the above command, pip will install the dependencies in the **global** environment which can create issues when you are working on multiple projects. This is addressed by **virtual environments**

- **Managing Dependencies the New Way**: `pyproject.toml`

  - `pyproject.toml` is a new file format introduced to replace `setup.py` for managing dependencies in Python projects. It was introduced as part of **PEP 518** and **PEP 621**.
  - It’s a configuration file that is used by pip to install your package and its dependencies. It has a simpler format compared to `setup.py` and is easier to read and maintain.
  - Here is an example of the `pyproject.toml`

    ```py
        [project]
        name = "your-project-name"
        version = "0.0.1"
        description = "A brief description of your package"
        authors = ["Your Name <your.email@example.com>"]

        [project.dependencies]
        dependency1 = "^1.0"
        dependency2 = "^2.0"
    ```

    - `name` and `version` fields are required, and specify the name and version of your package.
    - `description` field provides a brief description of your package.
    - `authors` field specifies the name and email address of the person responsible for the package.
    - `dependencies` section specifies the dependencies that your package needs in order to run correctly. In this example, the package depends on two other packages, `dependency1` and `dependency2`.

  - you can run the following command to perform an editable install:

    ```sh
        # install dependencies
        pip install -e .
    ```

# Resources and Further Reading
