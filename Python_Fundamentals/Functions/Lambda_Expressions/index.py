# Lambda Expressions

# Example 1: lamnda function
'''
   In this case, the parameter list consists of the single parameter s. 
   The subsequent expression s[::-1] is slicing syntax that returns the characters in s in reverse order. 
   So this lambda expression defines a temporary, nameless function that takes a string argument and returns the argument string with the characters reversed.
'''
lambda s: s[::-1] # <function __main__.<lambda>(s)>
print(callable(lambda s: s[::-1]))  # True
# The built-in Python function callable() returns True if the argument passed to it appears to be callable and False otherwise.

# Example 2: lambda functions
'''
    The object created by a lambda expression is a first-class citizen, just like a standard function or any other object in Python. 
    You can assign it to a variable and then call the function using that name:
'''
reverse = lambda s:s[::-1]
print(reverse('RODGERS'))

'''
    However, it’s not necessary to assign a variable to a lambda expression before calling it. You can also call the function defined by a lambda expression directly:
'''
print((lambda x:x[::-1])('RODGERS')) # SREGDOR
print((lambda x1, x2, x3:x1 + x2 + x3)(10, 20, 30)) # 60 # Anonymous function to calculate the sum of three numbers
(lambda x1, x2, x3: (x1 + x2 + x3) /3)(10, 20, 30) # Lambad function for calculating the average of three numbers

## Example 3 
"""
    A lambda expression will typically have a parameter list, but it’s not required. 
    You can define a lambda function without parameters. The return value is then not dependent on any input parameters:
"""
fifty_producer = lambda: 50
print(fifty_producer()) # 50