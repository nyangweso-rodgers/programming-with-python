# Lambda Functions

## Example: Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
## Example: Multiply argument a with argument b and return the result:

x = lambda a, b: a * b
print(x(5, 6))

## Example: sum
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))

# Example
## The object created by a lambda expression is a first-class citizen, just like a standard function or any other object in Python. 
## You can assign it to a variable and then call the function using that name:
reverse = lambda s:s[::-1]
print(reverse('RODGERS'))


## Example
### it’s not necessary to assign a variable to a lambda expression before calling it. You can also call the function defined by a lambda expression directly:
print((lambda x:x[::-1])('RODGERS')) # SREGDOR
print((lambda x1, x2, x3:x1 + x2 + x3)(10, 20, 30)) # 60 # Anonymous function to calculate the sum of three numbers
(lambda x1, x2, x3: (x1 + x2 + x3) /3)(10, 20, 30) # Lambad function for calculating the average of three numbers