# Callback Functions

## Example 1:  You can pass a function to another function as an argument:
def inner():
    print('I am function inner()!')

def outer(function):
    function()

outer(inner)

## Example 2: Callback function
## A good example of this is the Python function __sorted()__. Ordinarily, if you pass a list of string values to sorted(), then it sorts them in lexical order:
animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals))

## However, sorted() takes an optional key argument that specifies a callback function that can serve as the sorting key. So, for example, you can sort by string length instead:
animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=len))

## sorted() can also take an optional argument that specifies sorting in reverse order. 
animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=len, reverse=True)) # ['ferret', 'gecko', 'vole', 'dog']

## But you could manage the same thing by defining your own callback function that reverses the sense of len():
def reverse_len(s):
    return -len(s)
sorted(animals, key=reverse_len) # ['ferret', 'gecko', 'vole', 'dog']