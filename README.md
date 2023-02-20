# Python
## Table of Contents
1. [Python - Getting Started]()

2. [Programming Paradigms in Python](#Programming-Paradigms-in-Python)

- [References]()
    - [Building modern Python API backends in 2022](https://sanjeevan.co.uk/blog/modern-python-backends)
    - [Python Project Ideas to Improve Your Résumé](https://www.freecodecamp.org/news/python-project-ideas-to-improve-your-resume/)
    - [140 Python Projects with Source Code](https://medium.datadriveninvestor.com/140-python-projects-with-source-code-fa12c9e2aeac)
    - [Backend Web Development with Python - Full Course](https://www.freecodecamp.org/news/backend-web-development-with-python-full-course/)

# Setting Up Virtual Environment
1. Navigate to the root directory of your project using the terminal or command prompt.

2. Run the following command to create a new virtual environment: This will create a new directory called __env__ in your project directory, which contains the virtual environment.

    ```sh
        python -m venv venv
    ```
3. Activate the virtual environment by running the following command: This will activate the virtual environment and change your shell's prompt to indicate that you're working within the virtual environment.

    ```sh
        source env/bin/activate  # For Linux or macOS
        source venv/Scripts/activate  # For Windows
    ```

4. You can now install any required modules using pip, which will install them within the virtual environment. For example:

    ```sh
        pip install numpy
    ```

    This will install the numpy module within the virtual environment, making it available for use in your project.

# Remarks
* _When you're done working on your project, you can deactivate the virtual environment by running the deactivate command in the terminal._

* _By creating a virtual environment within your project directory, you can easily share your project with others, since they can create their own virtual environment and install the required dependencies using the __requirements.txt__ file (which lists the required packages and versions) that you can provide along with your code._

* _it's a best practice to use a separate file, usually called __requirements.txt__ or __Pipfile__, to list the required dependencies for your project. You can generate this file automatically using __pip freeze__, which will list all of the installed packages and their versions within your virtual environment. Here's an example of how to generate a __requirements.txt__ file:_

    ```sh
        pip freeze > requirements.txt
    ```

    This will create a requirements.txt file in your project directory that lists all of the installed packages and their versions. Commit the __requirements.txt__ file to your git repository.

* _With this approach, others can create their own virtual environment and install the required dependencies using the __requirements.txt__ file, by running the following command:_

    ```sh
        pip install -r requirements.txt
    ```

* _The __requirements.txt__ file should sit in the root directory of your project, outside of the virtual environment folder._ Here's an example of what the file might look like:

    ```txt
        numpy==1.20.1
        pandas==1.2.2
        matplotlib==3.3.4
    ```

* _Once you've created the __requirements.txt__ file, you should commit it to your git repository, along with your project files. When someone else wants to use your project, they can create a new virtual environment, activate it, and then run the following command:_

    ```sh
        pip install -r requirements.txt
    ```