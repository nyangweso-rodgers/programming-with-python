# Arbitrary Arguments, *args

* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a _tuple_ (not a list) of arguments, and can access the items accordingly:

* __Arbitrary Arguments__ are often shortened to __*args__ in Python documentations.

* Python doesn't have the concept of __function overloading__ because as soon as you create another function with the same name it discards the previous one and consider only the second defined function as the only one. Because you can pass as many arguments you want with the help of __*args__.