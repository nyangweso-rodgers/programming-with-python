# Factorial Function using a for loop

## Example 1: using for loop for factorial implementation
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i 
    return return_value 
print(factorial(5))