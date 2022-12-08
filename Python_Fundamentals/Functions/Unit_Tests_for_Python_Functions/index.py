'''
     To focus on how to set up unit tests, we'll consider a simple function is_prime(), that takes in a number and checks whether or not it is prime.
'''
import math
#print(dir(math))

def is_prime(num):
    '''check if a number is prime or not'''
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % 2 == 0:
            return False
    return True

import unittest
print(dir(unittest))