# using Permutations to work with Prime Numbers

from sympy import *
from itertools import permutations

# check methods
# print(dir(permutations))

xsp = []
xspp = []

for x in range(100):
    if is_prime(x) == False:
        xsp = []
        xs = str(x)
        perms = ([
            ''.join(l) for i in range(len (xs))
            for l in permutations(xs, i + 1)
        ])
        for s in perms:
            xsp.append(is_prime(int(s)))
        if all(xsp) == False:
            xspp.append(x)
print(xspp)