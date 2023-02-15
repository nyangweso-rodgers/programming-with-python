# args

# Arbitrary Arguments, *args
## If the number of arguments is unknown, add a * before the parameter name:
def my_kids(*kids):
    print("The Youngest Child is " + kids[2])
my_kids("Rodgers", "Omondi", "Nyangweso")
print("###############################################")

## Example: sum
def add(*args):
    return sum(args)
print(add(1,2, 3, 4, 5, 6, 7, 8, 9, 10))
print("###############################################")

# Example 2
def my_function(*argv):
    for arg in argv:
        print(arg)

print(my_function("Hello", "learning", "*args", "and", "**kwargs"))

# Example 3
def my_function(arg1, *argv):
    print('First Argument: ', arg1)
    for arg in argv:
        print("Next Argument though *argv :", arg)

print(my_function("Hello,", "I", "am", "learning", "*args and **kwargs"))