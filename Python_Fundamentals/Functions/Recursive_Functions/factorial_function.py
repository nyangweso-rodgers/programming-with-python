# factorial function

## Example 1: Factorial function using a recursive function
## Recusrsive definition of Factorial function
def factorial(n):
     return 1 if n <= 1 else n * factorial(n - 1)
print(factorial(5))