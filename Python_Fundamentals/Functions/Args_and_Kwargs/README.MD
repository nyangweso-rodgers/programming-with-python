# Args and Kwargs in Python

## Table Of Contents
- [Further Reading]()
    - [*args and **kwargs in Python](https://www.geeksforgeeks.org/args-kwargs-python/)

# *args
* __*args__ is called ‘__arbitrary arguments__’. It is useful in the cases where you don’t know how many arguments you need for your function. This way, you will have a tuple (not a list) of arguments.

* Python doesn't have the concept of function overloading because as soon as you create another function with the same name it discards the previous one and consider only the second defined function as the only one. Because you can pass as many arguments you want with the help of __*args__.

# *kwargs
* __**kwargs__ is called ‘__arbitrary keyword arguments__’. It is the same thing speaking about not knowing the number of arguments needed etc. But the difference here is that you will have a __dictionary__ of arguments instead of a __tuple__. So, we are using the key = value syntax, then, inside the function, you might use kwargs[key].

* It is used where you want the user to enter the parameter name also followed by argument. 