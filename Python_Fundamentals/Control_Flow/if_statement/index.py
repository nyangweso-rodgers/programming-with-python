# if statement

# Example 1
### _The following fragment will first check to see if the value of a variable _n_ is negative. 
### If it is, then it's modified by the __absolute__ value function. Regardless, the next action is to compute the square root._
import math
n = -9
if n < 0:
    n = abs(n)
print(math.sqrt(n))