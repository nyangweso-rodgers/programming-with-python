# Writing Unit Tests for Python Functions

## Table Of Contents
- [Introduction to Unit Tests in Python](#Introduction-to-Unit-Tests-in-Python)
- [How to Use Python's unittest Module](#How-to-Use-Python-s-unittest-Module)
- [Further Reading]()
    - [How to Write Unit Tests for Python Functions](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/)

# Introduction to Unit Tests in Python
* __Unit tests__ let you check if small isolated units of code function correctly and enable you to fix inconsistencies that arise from updates and refactoring.

# How to Use Python's unittest Module
* __Python__ ships with the __unittest__ module that lets you configure automated tests for functions and classes in your application. The generic procedure to set up unit tests in Python is as follows:

    ```py
        # <module-name>.py
        
        import unittest
        from <module> import <function_to_test>
        # all entries within <> are placeholders

        class TestClass(unittest.TestCase):
            def test_<name_1>(self):
                # check function_to_test
            
            def test_<name_2>(self):
                # check function_to_test

            def test_<name_n>(self):
                # check function_to_test
    ```
