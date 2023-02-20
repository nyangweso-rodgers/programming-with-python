# Python Modules

## Table Of Contents

# Installing Modules in VS Code
* When you run __pip install numpy__, the numpy module will be installed locally on your machine, typically in the site-packages directory of your Python installation or virtual environment. The specific location of the site-packages directory may depend on your operating system and Python installation.

* If you want to install the module globally, so that it is available to all Python projects on your machine, you can use the __--user__ flag when running the __pip install__ command. This will install the module in the user-specific site-packages directory, which is typically located in the user's home directory. For example:

    ```sh
        pip install numpy --user
    ```

* If you need to use the same module in another repo, you can install it in the same way as described above. If you're working on multiple projects that require different versions of the same module, it's often a good idea to use a virtual environment for each project. A virtual environment allows you to isolate the Python environment and dependencies for each project, so that they don't interfere with each other.