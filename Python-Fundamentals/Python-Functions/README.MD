# Python Functions

## Table Of Contents

# Parameters or Arguments?
* From a function's perspective:
    - A __parameter__ is the variable listed inside the parentheses in the function definition.
    - An __argument__ is the value that is sent to the function when it is called.

# Arbitrary Arguments, *args
* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:

* __Arbitrary Arguments__ are often shortened to __*args__ in Python documentations.

# Keyword Arguments
* You can also send arguments with the _key = value_ syntax. This way the order of the arguments does not matter.

* The phrase __Keyword Arguments__ are often shortened to __kwargs__ in Python documentations.

# Arbitrary Keyword Arguments, **kwargs
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: __**__ before the parameter name in the function definition.

* This way the function will receive a _dictionary of arguments_, and can access the items accordingly:

# Default Parameter Value
* If we call the function without argument, it uses the default value:

# Passing a List as an Argument
* You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function. E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Return Values
* To let a function return a value, use the __return__ statement:

# The pass Statement
* __function__ definitions cannot be empty, but if you for some reason have a __function__ definition with no content, put in the pass statement to avoid getting an error.