# Lambda Functions

## Table Of Contents

# Introduction to Python Lambda
* A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

# Syntax
```py
    lambda arguments: expression
```

# Why Use Lambda Functions?
* The power of lambda is better shown when you use them as an anonymous function inside another function.

* Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

    ```py
        def my_func(n):
            return lambda a: a * n
    ```

* Use that function definition to make a function that always doubles the number you send in:
    ```py
        def myfunc(n):
            return lambda a : a * n

        mydoubler = myfunc(2)

        print(mydoubler(11))
    ```

* Or, use the same function definition to make a function that always triples the number you send in:
    ```py
        def myfunc(n):
            return lambda a : a * n

        mytripler = myfunc(3)

        print(mytripler(11))
    ```
* Or, use the same function definition to make both functions, in the same program:
    ```py
        def myfunc(n):
            return lambda a : a * n

        mydoubler = myfunc(2)
        mytripler = myfunc(3)

        print(mydoubler(11))
        print(mytripler(11))
    ```

# Remarks:
* _Use lambda functions when an anonymous function is required for a short period of time._

* _you can only define fairly rudimentary functions with lambda. The return value from a lambda expression can only be one single expression. A lambda expression can’t contain statements like assignment or return, nor can it contain control structures such as for, while, if, else, or def._

* _a function defined with def can effectively return multiple values. If a return statement in a function contains several comma-separated values, then Python packs them and returns them as a tuple:_

* _A lambda expression will typically have a parameter list, but it’s not required._

    ```py
        # You can define a lambda function without parameters. The return value is then not dependent on any input parameters:
        fifty_producer = lambda: 50
        print(fifty_producer()) # 50
    ```