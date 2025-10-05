# Python Dictionary

## Table Of Contents
- [Further Reading]()
  - [Python Dictionary – How to Create a Dict in Python (Hashmap)](https://www.freecodecamp.org/news/python-dictionary-how-to-create-a-dict-in-python/)

# Overview Of Python's Dictionary
* A __dictionary__ is a type of data structure that allows us to store __key-value__ pairs.
* Dictionaries are useful when we want to store data in a way that is easily accessible and modifiable. To create dictionaries in Python, we use curly braces, the __dict()__ constructor, and the __fromkeys()__ method.


# How to create a dict using the dict() constructor
* The constructor __dict()__ produces a dictionary from an iterable of key-value pairs as input. Both a list of tuples and arguments can be used to pass in the key-value pairs.
* The __dict()__ constructor can also be used to create an empty dictionary by not passing any arguments. For example, __MyDict = dict()__ creates an empty dictionary MyDict.

# How to create a dict using the fromkeys() method
* You can also use the built-in __fromkeys()__ method to create a dictionary by selecting keys from a sequence and setting values to default values.
* The first argument to the __fromkeys()__ method is a list of keys, and the second (optional) argument is the value that will be assigned to each key after it has been set. The values will automatically be set to None if the second argument is not provided.