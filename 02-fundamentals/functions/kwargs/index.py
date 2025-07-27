# kwargs

# Example: Arbitrary Keyword Arguments, **kwargs
## If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_siblings(**sib):
    print("His las name is " + sib["last_name"])
    
my_siblings(first_name = 'Robert', last_name = 'Okoth')
print("########################################################################")

# Example 1: - Usage of **kwargs
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

print(greet_me(name = 'John'))
###########################################################################

# Example 2: - Usage of **kwargs
def my_function(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# Driver code
print(my_function(first_name ='Rodgers', middle_name ='Omondi', last_name='Nyangweso'))