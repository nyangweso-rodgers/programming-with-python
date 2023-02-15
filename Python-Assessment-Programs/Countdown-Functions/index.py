def countdown(n):
    print(n)
    if n == 0:
        return # Terminate Recursion
    else:
        countdown(n - 1) # Recursive call        
countdown(5)
print("################")

# Method 2
## The version of countdown() shown above clearly highlights the base case and the recursive call, but there’s a more concise way to express it:
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)
countdown(5)
print("################")

# Method 3
## This is a case where the non-recursive solution is at least as clear and intuitive as the recursive one, and probably more so.
def countdown(n):
    while n >= 0:
        print(n)
        n-=1     
countdown(5)