# Recursive Functions

## Example 1: Finding Python's recursion limit from the sys module
from sys import getrecursionlimit 
print(getrecursionlimit())

# You can change it,too, with setrecursionlimit
# Example 2: change the recursion limit 
from sys import setrecursionlimit 
from sys import getrecursionlimit
setrecursionlimit(4000)
print(getrecursionlimit())

# Example 3: Countdown to Zero
## The function takes a positive number as an argument and prints the numbers from the specified number down to zero
def countdown(n):
    print(n)
    if n == 0:
        return # Terminate Recursion
    else:
        countdown(n - 1) # Recursive call        
countdown(5)

# The version of countdown() shown above clearly highlights the base case and the recursive call, but there’s a more concise way to express it:
## Example 4:
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)
countdown(5)

# Example 5
## This is a case where the non-recursive solution is at least as clear and intuitive as the recursive one, and probably more so.
def countdown(n):
    while n>= 0:
        print(n)
        n-=1     
countdown(5)