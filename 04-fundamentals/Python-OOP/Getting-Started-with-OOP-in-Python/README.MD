# Getting Started with OOP in Python

## Table of Contents

# Introduction to OOP
* __OOP__ is a way of writing code that relies on the concepts of __classes__ and __objects__.

* __Class__ is a blueprint of an __object__. It contains all the details and methods of an object. Just like a string, integer, or float, a class is a custom type that has some special properties.

* An __object__ is an instance of a class. An __object__ has two _characteristics_:
    - __Attributes__: attribute of an object usually consists of a name and a value
    - __Behavior__: behavior of an object is its predefined functions

# Methods on a class
* You might be wondering why classes are useful – they seem like regular Python dictionaries but worse! What makes classes really cool is that they allow us to define custom [methods](https://en.wikipedia.org/wiki/Method_(computer_programming)) on them. A __method__ is a function that is associated with a class, and it has access to all the properties of the object.

* __Methods__: are functions defined inside the body of a class, used to determine the behaviors of an object.

# The special "self" value
* __Methods__ are nested within the class declaration. __Methods__ always take a special parameter as their first argument called __self__. The __self__ variable is a reference to the object itself, so by using it you can read and update the properties of the object.

* Notice that methods are called directly on an object using the dot operator.

    ```py
        object.method()
    ```

# Methods vs Functions
* A _function is a piece of code that is called by a name_. You can pass it data to operate on via parameters and it can optionally return data. All data that is passed to a function is explicitly passed through parameters.

* A _method is a piece of code that is called by a name that is associated with an object_. Methods and functions are similar but have two key differences:

    - A method is implicitly passed the object on which it was called. i.e., you won't see all the inputs in the parameter list

    - A method is able to operate on data that is contained within the class. i.e., you won't see all the outputs in the return statement.

# Constructors in Python
* It's quite rare in the real-world to see a class that defines properties in the following way:
    ```py
        class Car:
            color = white
    ```
* It's much more practical to use a __constructor__. In Python, a constructor is made with the __init__() method, and it is automatically called when a new object is created. So, with a constructor the code would look like this:
    ```py
        class Car:
            def __init__(self, color):
                self.color = color
    ```