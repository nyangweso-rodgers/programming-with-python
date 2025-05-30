# Python Development Environment

## Table of Contents

# Python Virtual Environments

- A **virtual environment** is a Python tool for **dependency management** and **project isolation**. They allow Python **site packages** (third party libraries) to be installed locally in an isolated directory for a particular project, as opposed to being installed globally (i.e. as part of a system-wide Python).

- At its core, the main purpose of **Python virtual environments** is to create an isolated environment for Python projects. This means that each project can have its own **dependencies**, regardless of what dependencies every other project has. i.e., when you activate a virtual environment for your project, your project becomes its own self contained application, independent of the system installed Python and its modules.

- Your new **virtual environment** has its own:

  - `__pip__` to install libraries,
  - `__libraries__`folder, where new libraries are added, and its own
  - `__Python interpreter__` for the Python version you used to activate the environment.

- **Benefits of Python Virtual Environment**

  1. development environment is contained within your project, becomes isolated, and does not interfere with your system installed Python or other virtual environments
  2. You can create a new virtual environment for multiple Python versions
  3. You are able to download packages into your project without admin privileges
  4. You can easily package your application and share with other developers to replicate\
  5. You can easily create a list of dependencies and sub dependencies in a file, for your project, which makes it easy for other developers to replicate and install all the dependencies used within your environment
  6. Keep your global site-packages/ directory tidy by removing the need to install packages system-wide which you might only need for one project.

- **How Python uses a Virtual Environment**

  - During start-up, **Python** automatically calls the `site.main()` function (unless you specify the `-S` flag). That function calls `site.venv()` which handles setting up your Python executable to use the virtual environment appropriately.
  - Specifically, the `site` module:
    1. Looks for **pyvenv.cfg** in either the same or parent directory as the running executable (which is not resolved, so the location of the symlink is used)
    2. Looks for **include-system-site-packages** in **pyvenv.cfg** to decide whether the system **site-packages** ends up on **sys.path**.
    3. Sets **sys.\_home** if **home** is found in **pyvenv.cfg** (**sys.\_home** is used by **sysconfig**)

- **Components Of a Python Virtual Environment**

  1. A `__site-packages/__` folder where third party libraries are installed
  2. [Symlinks](https://en.wikipedia.org/wiki/Symbolic_link) to Python executables installed on your system.
  3. [Scripts](https://en.wikipedia.org/wiki/Shell_script) that ensure executed Python code uses the Python interpreter and site packages installed inside the given virtual environment.

- **Structure of Python Virtual Environment**

  1. `bin` (`Scripts` on Windows) on Unix.
  2. `include` (`Include` on Windows) on Unix: The `include` directory is for any header files that might get installed for some reason from a project.
  3. `lib/pythonX.Y/site-packages` where `X`, `Y` is the Python version (`Lib/site-packages` on Windows) on Unix: The `site-packages` directory is where projects get installed into the virtual environment (including `pip` if you choose to have it installed into the virtual environment).
  4. `lib64` symlinked to `lib` if you're using a `64-bit` build of Python that's on a POSIX-based OS that's not macOS: The `lib64` symlink is for consistency on those Unix OSs where they have such directories.
  5. The configuration file is `pyvenv.cfg` and it lives at the top of your virtual environment directory (e.v. **.venv/pyvenv.cfg**). As of Python 3.11, it contains a few entries:
     - **home** (the directory where the executable used to create the virtual environment lives; **os.path.dirname(sys.\_base_executable)**)
     - **include-system-packages** (should the global **site-packages** be included, effectively turning off isolation?)
     - **version** (the Python version down to the micro version, but not with the release level, e.g. 3.12.0, but not 3.12.0a6)

# Setup Python Virtual Environment

## 1. Setting Up Virtual Environment (Windows)

1. **Step 1**: Navigate to the root directory of your project using the terminal or command prompt.
2. **Step 2**:

   - Run the following command to create a new virtual environment: This will create a new directory called **env** in your project directory, which contains the virtual environment.
     ```bash
       python -m venv <virtual-env-name>
     ```

3. **Step 3**:

   - Activate the virtual environment by running the following command:

   ```sh
       source env/bin/activate  # For Linux or macOS
       source venv/Scripts/activate  # For Windows
   ```

   - This will activate the virtual environment and change your shell's prompt to indicate that you're working within the virtual environment.

4. **Step 4**: Installing Packages

   - You can now install any required modules using `pip`, which will install them within the virtual environment.
   - For example:

     ```sh
      pip install numpy
      # or, install a specific package
      pip install numpy==1.15.3
     ```

   - By default, only `pip` and `setuptools` are installed inside a new environment.

5. **Step 5**: Managing Environments Using `requirements.txt` File

   - The easiest way to make our work reproducible by others is to include a requirements file in our project’s **root directory** (top directory). To do so, we’ll run `pip freeze`, which lists installed third party packages along with their version numbers

     ```sh
      pip freeze
     ```

   - And write the output to a file, which we’ll call `requirements.txt`.

     ```py
       pip freeze > requirements.txt
     ```

   - We can use this same command to rewrite our requirements file whenever we update a package or install a new one.
   - Now anyone we share our project with will be able to run our project on their system by duplicating our environment using our `requirements.txt` file.

6. **Step 6**: Installing project dependencies from the `requirements.txt` File:
   ```bash
    pip install -r requirements.txt
   ```

## 2. Setting Up Virtual Environment on Ubuntu

1. **Step 1**: Verify `python3` Installation:

   - The latest **Ubuntu** versions come with **Python 3** installation, so to verify its installation, run the following command:

     ```sh
      python3 --version
     ```

   - In case this returns an error, you can install/re-install the package by running:
     ```sh
       sudo apt-get install python3
     ```

2. **Step 2**: **Install** `pip`:

   - Next, you need to install the `pip` to install Python packages and their dependencies in a secure manner.
     ```sh
      sudo apt-get install python3-pip
     ```

3. **Step 3**: **Create Virtual Environment**

   - Here, you will create a virtual environment for your project that will isolate your project’s dependencies to avoid potential conflicts between different package versions. Run the following set of commands in the terminal:
     ```sh
      sudo apt-get install python3-venv
     ```
   - This will install the required `venv` package required to create a virtual environment.
   - Create a virtual environment by:

     ```sh
      python3 -m venv <name>
     ```

   - This command will create a virtual environment `<name>` inside your working directory. To start working inside this environment, you need to activate it by:
     ```sh
       source <name>/bin/activate
     ```

4. **Step 4**: **Install Required Libraries and Packages**

5. **Step 5**: **Deactivate the Virtual Environment**

   - Deactivate the virtual environment by:
     ```sh
      deativate
     ```

6. **Step 6**: **Delete the Virtual Environment Folder**
   - Use the `rm` command to remove the entire folder.
     ```sh
      rm -rf <name>
     ```
   - `rm` is the remove command.
   - `-r` (recursive) ensures all contents of the folder are deleted.
   - `-f` (force) prevents prompts for confirmation.

# Dockerize Python Application

- Define `Dockerfile` in thr root directory with the following contents:

  ```Dockerfile
      # Use an official Python runtime as the base image
      FROM python:3.12.0

      # Set the working directory inside the container
      WORKDIR /app

      # Copy the current directory contents into the container at /app
      COPY . /app

      # Install any needed packages specified in requirements.txt
      RUN pip install -r requirements.txt

      # Define the default command to run when the container starts
      CMD ["python", "app.py"]
  ```

- Where:
  - `FROM:` Specifies the base image, in this case, Python 3.12.0
  - `WORKDIR:` Sets the working directory within the container to `/app`.
  - `COPY:` Copies the local files and directories into the container.
  - `RUN:` Installs Python dependencies defined in `requirements.txt`.
  - `CMD:` Specifies the default command to run the Python application when a container is started.

# Resources

1. [freeCodeCamp](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
2. [A Guide to Python’s Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)
3. [How virtual environments work](https://snarky.ca/how-virtual-environments-work/)
