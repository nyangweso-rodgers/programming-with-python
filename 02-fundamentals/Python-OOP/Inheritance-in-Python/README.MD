# Inheritance in Python

# Inheritance in Python – Syntax
* In Python, one class can inherit from another using the following syntax:
    ```py
        class Animal():
            # parent animal class
        class Cow(Animal):
            # child class "Cow" inherits "Animal"
    ```

* In order to use the constructor of the parent class, we can use Python's built in __super()__ method.