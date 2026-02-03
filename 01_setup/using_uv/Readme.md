# `uv` Package Manager

## Table Of Contents

## `uv`

- `uv` is a **Rust-based package manager** that aims to transform Python dependency management with unmatched performance and simplicity.
- It was developed by **Astral** (the company behind the [popular Ruff linter](https://github.com/astral-sh/ruff)), and is designed to be the comprehensive solution for Python package management.
- With `uv`, you can replace a wide range of traditional tools in your workflow, such as:
  1.  `pip` for installing packages.
  2.  `pip-tools` for dependency locking.
  3.  `virtualenv/venv` for environment management.
  4.  `pyenv` for managing Python versions.
  5.  `pipx` for installing CLI tools.
  6.  `poetry` for project configuration and publishing.
  7.  `twine` for distributing packages.

- **Remarks**
  - `uv` also embraces modern packaging standards. It uses `pyproject.toml` for configuration and introduces a reliable lock file that ensures consistent environments across systems.

## Installing `uv`

- On **Linux** and **macOS**, run
  ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- On **Windows**, use **PowerShell**
  ```sh
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- After installation, confirm that it's working by checking the version:
  ```sh
    uv --version
  ```
- To update `uv`, run:
  ```sh
    uv self update
  ```

## Managing Virtual Environments with `uv` for Python

- `uv` can serve as a direct replacement for tools like `virtualenv` and `venv` to create isolated Python environments.
- Previously, you might run:
  ```sh
    python -m venv .venv
  ```
- With `uv`, the equivalent is:

  ```sh
    uv venv # used .venv by default
  ```

  - By default, this creates a virtual environment in `.venv`, but you can specify a custom path if needed:
    ```sh
      uv venv <path/to/environment>
    ```

## Replacing `Pip` with `uv` for Dependency Management

- `uv` provides a `pip`-compatible interface for managing project dependencies. You only need to prefix specific `pip` commands with `uv`.
- For example, you can install dependencies with:
  ```sh
    uv pip install flask requests
  ```
- There's no need to activate a virtual environment beforehand, as `uv` automatically detects and uses the nearest environment in your current or parent directory.
- If no environment is found, it will prompt you to create one or suggest using the --system flag to install it globally:
- Installing dependencies from existing project files works the same way:
  ```sh
    uv pip install -r requirements.txt
  ```
  ```sh
    uv pip install -r pyproject.toml
  ```

## Managing Python Versions with `uv`

- One of `uv`'s key advantages is that it doesn't rely on Python to run. Instead, it automatically detects existing Python installations and uses them for any Python-specific tasks.
- If a project requires a version of Python that isn't already installed, uv will also download and manage it for you.
- You can install Python versions directly like this:
  ```sh
    uv python install # the latest version
    uv python install 3.13 # a specific version
    uv python install 3.13 3.12 # multiple versions
  ```
- To check which versions are available on your system, run:

  ```sh
    uv python list --only-installed
  ```

  - This will lists all Python versions installed by `uv`, as well as any others already on your system, regardless of how they were installed:

- With `uv`, you don't need to install Python ahead of time. If a command requires a version you don't yet have, uv will fetch and install it automatically before proceeding. This on-demand behavior eliminates the need for separate tools like pyenv.

- **Creating and Managing Python Projects with `uv`**
  - One of `uv`'s core goals is to manage the entire lifecycle of a **Python project**, from **creating the project itself**, to **managing its dependencies**, **running commands or scripts**, and even preparing it for distribution.
  - To start a new project, run:
    ```sh
      uv init <project_name>
    ```
  - By default, this sets up an application-style project. To create a library project instead, use:
    ```sh
      uv init --lib <project_name>
    ```
  - An initialized application project has the following structure:
    - .
      - .git
      - .gitignore
      - main.py
      - pyproject.toml
      - .python-version
      - README.md
    - `uv` sets up version control with Git, includes `pyproject.toml` for project **metadata** and **dependencies**, and creates a basic script (`main.py`) along with a `.python-version` file. It's ready to run out of the box.
    - Execute the script with:
      ```sh
        uv run main.py
      ```
    - The first time you run this, `uv` will select the appropriate Python version, create a virtual environment, and then execute the script:
      - At this point, `uv` generates a `uv.lock` file, which records the full, resolved dependency graph — ensuring consistent environments across different machines.
      - While `pyproject.toml` defines intended dependencies (like `requirements.in`), `uv.lock` captures the exact installed versions, effectively replacing `requirements.txt` for reproducibility.
    - **Managing Dependencies to a `uv` Project**
      - It's simple to add dependencies to a `uv` project. To add a package, use:
        ```sh
          uv add requests
        ```
      - For development dependencies or tools, append the `--dev` flag:
        ```sh
          uv add --dev black
        ```
      - These changes are reflected in your `pyproject.toml`:

        ```toml
          # pyproject.toml
          . . .
          dependencies = [
              "requests>=2.32.3",
          ]

          [dependency-groups]
          dev = [
              "black>=25.1.0",
          ]
        ```

      - You can create custom dependency groups using the `--group` flag:

        ```sh
          uv add --group tools black
          uv add --group production gunicorn
          uv add --group dev pytest # same as uv add --dev
        ```

        - Resulting in:
          ```toml
            [dependency-groups]
            dev = [
                "pytest>=8.3.5",
            ]
            production = [
                "gunicorn>=23.0.0",
            ]
            tools = [
                "black>=25.1.0",
            ]
          ```
        - This structure makes it easy to install only the dependencies needed for a given environment. For example, to install just the base and production dependencies, run:
          ```sh
            uv sync --no-group dev --no-group tools --group prod
          ```
        - Dependencies are always installed into the project's virtual environment, so there's no need to activate it manually. Once installed, you can run any tool using:
          ```sh
            uv run <tool>
          ```

      - **Upgrading and Removing Dependencies**
        - `uv` provides straightforward commands for updating and removing packages as your project evolves.
          ```sh
            uv add --upgrade requests
          ```
        - Removing packages is equally simple:

          ```sh
            uv remove requests
          ```

          - `uv` will clean up the `pyproject.toml`, remove unneeded transitive dependencies, and regenerate the uv.lock file automatically.

- **Migration Guide: From `Pip` to `uv`**
  - If your project currently uses `pip` and `requirements.txt`, you can migrate it to `uv` in just a few steps.
    1. **Step 1**: Initialize uv in the existing project directory:

       ```sh
        uv init .
       ```

       - This creates a `pyproject.toml` file and sets up the project structure, without replacing any existing files.

    2. **Step 2**: Remove the old virtual environment:
       ```sh
        rm -rf .venv
       ```
    3. **Step 3**: Install dependencies from `requirements.txt`:

       ```sh
        uv add -r requirements.txt
       ```

       - This installs the dependencies listed in your `requirements.txt` file in a virtual environment, and updates the `pyproject.yml` and `uv.lock` files accordingly.

    4. **Step 4**: Create a new uv-managed environment:
       ```sh
        uv sync
       ```
    5. **Step 5**: Verify that everything works — for example (assuming you have a Django project):
       ```sh
        uv run manage.py migrate
       ```
       ```sh
        uv run manage.py runserver
       ```

# Resources and Further Reading

1. [blog.appsignal.com - Switching from Pip to uv in Python: A Comprehensive Guide](https://blog.appsignal.com/2025/09/24/switching-from-pip-to-uv-in-python-a-comprehensive-guide.html?ref=dailydev)
2. [uv is the best thing to happen to the Python ecosystem in a decade](https://emily.space/posts/251023-uv?utm_source=tldrnewsletters)
