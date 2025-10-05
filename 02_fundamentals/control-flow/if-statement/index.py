# if statement

# Example: Square Root
## The following fragment will first check to see if the value of a variable n is negative. 
## If it is, then it's modified by the absolute value function. Regardless, the next action is to compute the square root.
import math
n = -9
if n < 0:
    n = abs(n)
print(math.sqrt(n))