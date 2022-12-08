# args and kwargs in Python

# Example 1

def add(*args):
    return sum(args)

# It will return the sum of as many arguments you want.
print(add(1,2, 3, 4, 5, 6, 7, 8, 9, 10))

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

# *kwargs
# Example 4: - Usage of **kwargs
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

print(greet_me(name = 'John'))

# Example 5: - Usage of **kwargs
def my_function(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# Driver code
print(my_function(first_name ='Rodgers', middle_name ='Omondi', last_name='Nyangweso'))