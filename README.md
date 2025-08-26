# Python

## Table of Contents

# Python

- **Is Python a compiled language or an interpreted language?**

  - **Python** does not fall completely into just one category. Instead, it uses a mix of both.
  - **How Python Code is executed**:

    - **Step 1**: Compilation into Bytecode

      - **Python** does not directly run the code we write.
      - First, **Python** translates your code into something called **bytecode**.
      - **Bytecode** is a lower-level form of your code that is easier for the computer to understand but still not the machine code your CPU runs.
      - This compiled **bytecode** is often saved in `.pyc` files inside a folder named `__pycache__`.

    - **Step 2**: Execution by the Interpreter
      - Once Python has the **bytecode**, it passes it to the **Python Virtual Machine** (**PVM**).
      - The **PVM** is part of the **Python interpreter**. It reads the **bytecode** and executes it line by line.
      - This is why **Python** is often called an **interpreted language**.

  - **Compiled vs Interpreted Languages**

    - **Compiled Languages (like C, C++)**

      - The code is directly converted into machine code that the CPU can run.
      - Programs run very fast once compiled.
      - You must compile the program before running it.

    - **Interpreted Languages (like JavaScript, Ruby)**

      - The code is read and executed line by line by an **interpreter**.
      - They are usually slower compared to compiled languages.
      - Easier for developers to test and debug since they don’t need a full compile step.

    - **Python** combines both approaches because it first **compiles** into **bytecode** and then **interprets** that **bytecode**

- **Different Python Implementations**

  - There are different versions (implementations) of **Python**, and they may execute code differently.

    1. **CPython** (default)

       - This is the version of **Python** that most people use.
       - It compiles **Python** code into **bytecode** and then interprets it using the **PVM**.

    2. **PyPy**

       - This version uses something called **Just-In-Time** (**JIT**) compilation.
       - It speeds up Python by converting **bytecode** into **machine code** while the program is running.

    3. **Jython**

       - Runs Python code on the **Java Virtual Machine** (**JVM**).
       - Compiles **Python** code into **Java bytecode**.

    4. **IronPython**
       - Runs **Python** code on the **.NET framework**.
       - Compiles Python code into **.NET bytecode**.

  - These shows that Python’s behavior depends on which version (implementation) we are using.

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

# Python `main` Program

- When the Python interpreter reads a source file, it does two things:
  1. First, it sets a few special variables like `__name__`
  2. Then it executes all of the code it finds in the file
- Example:

  - Let’s have a look at the following example where we correctly use the `if __name__ == "__main__"` statement:

    ```py
      # main.py
      def functionA():
         print("Function A")

      if __name__ == "__main__":
         print("Running foo")
         functionA()
    ```

  - **Case 1**: (Run it as the main program with `python main.py`):
    - The Python interpreter will assign the hard-coded string `"__main__" to the __name__` variable, thus the code in the if statement is executed:
      ```sh
         $ python main.py
         Running foo
         Function A
      ```
  - **Case 2**: Import foo in another module

    - The interpreter will assign "foo" to the `__name__` variable in the foo module. Thus, the code in the if statement is not executed, and functionA will not run.

      ```py
         # This is bar.py
         import foo

         if __name__ == "__main__":
            print("Running bar")
      ```

      ```sh
         $ python bar.py
         Running bar
      ```

  - Without the if `__name__ == "__main__"` in `main.py`, the output would be the following:
    ```sh
      $ python bar.py
      Running foo
      Function A
      Running bar
    ```
  - Usually this is not what we want. So if you want to run code in a file, it’s good practice to wrap all of this code into a if `__name__ == "__main__" `statement.

# Resources and Further Reading

- [Building modern Python API backends in 2022](https://sanjeevan.co.uk/blog/modern-python-backends)
- [Python Project Ideas to Improve Your Résumé](https://www.freecodecamp.org/news/python-project-ideas-to-improve-your-resume/)
- [140 Python Projects with Source Code](https://medium.datadriveninvestor.com/140-python-projects-with-source-code-fa12c9e2aeac)
- [Backend Web Development with Python - Full Course](https://www.freecodecamp.org/news/backend-web-development-with-python-full-course/)
