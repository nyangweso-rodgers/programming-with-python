# Python Functions

## Table of Contents
- [Introduction to Python Functions](#Introduction-to-Python-Functions)
    - [Pure Functions](#Pure-Functions)
    - [Callback Functions](#Callback-Functions)
    - [Recursion Functions](#Recursion-Functions)

- [Lambda Expressions](#Lambda-Expressions)

# Introduction to Python Functions

# Pure Functions
* A __pure function__ is a function whose output value follows solely from its input values, without any observable side effects.

* In Python, functions are __first-class citizens__. That means functions have the same characteristics as values like _strings_ and _numbers_. Anything you would expect to be able to do with a string or number you can do with a function as well.

# Callback Functions
* When you pass a function to another function, the passed-in function sometimes is referred to as a __callback__ because a call back to the inner function can modify the outer function’s behavior. Examples include:
    * sorted()

# Recursion Functions
* In Python, it’s also possible for a function to call itself! A function that calls itself is said to be __recursive__, and the technique of employing a recursive function is called __recursion__.

* __Why Use Recursion?__: Most programming problems are solvable without recursion. So, strictly speaking, __recursion__ usually isn’t necessary. However, some situations particularly lend themselves to a self-referential definition. __Factors to consider include:__
    * For some problems, a recursive solution, though possible, will be awkward rather than elegant.
    * Recursive implementations often consume more memory than non-recursive ones.
    * In some cases, using recursion may result in slower execution time.

* Typically, the readability of the code will be the biggest determining factor. But it depends on the circumstances.

# Lambda Expressions
* Functional programming is all about calling functions and passing them around, so it naturally involves defining a lot of functions. You can always define a function in the usual way, using the __def__ keyword. Sometimes, though, it’s convenient to be able to define an __anonymous__ function on the fly, without having to give it a name. In Python, you can do this with a _lambda_ expression.

* The value of a lambda expression is a callable function, just like a function defined with the def keyword. It takes arguments, as specified by <parameter_list>, and returns a value, as indicated by <expression>.

# map(), filter() and reduce()
* Python offers two built-in functions, __map()__ and __filter()__, that fit the functional programming paradigm. A third, __reduce()__, is no longer part of the core language but is still available from a module called __functools__. Each of these three functions takes another function as one of its arguments.

* With __map()__, you can apply a function to each element in an iterable in turn, and __map()__ will return an iterator that yields the results. This can allow for some very concise code because a __map()__ statement can often take the place of an explicit loop.

* __filter()__: _allows you to select or filter items from an iterable based on evaluation of the given function. It’s called as follows:_