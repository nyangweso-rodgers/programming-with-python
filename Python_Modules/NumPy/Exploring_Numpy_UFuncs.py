# Exploring Numpy's UFuncs
'''
Ufuncs exist in two flavors: 
unary ufuncs, which operate on a single input, and 
binary ufuncs, which operate on two inputs. .
'''
# Array arithmetic
'''
NumPy’s ufuncs feel very natural to use because they make use of Python’s native arithmetic operators. 
The standard addition, subtraction, multiplication, and division can all be used:
'''

import numpy as np 
np.random.seed(0)

x = np.arange(4)
print("x   =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("5 - x =", 5 - x)
print("x * 5 =", x*5)
print("x / 5 =", x / 5)
print("x // 5 =", x // 2) # floor division

# There is also a unary ufunc for negation, a ** operator for exponentiation, and a % operator for modulus:
print("-x =", -x)
print("x ** 2 =", x**2)
print("x % 2 =", x%2)

# In addition, these can be strung together however you wish, and the standard order of operations is respected:
print(-(0.5*x) ** 2)

# All of these arithmetic operations are simply convenient wrappers around specific functions built into NumPy; 
# for example, the + operator is a wrapper for the add function:
print(np.add(x, 2)) # [2 3 4 5]

# Arithmetic operators implemented in NumPy
# Other ufunc include:
# np.subtract()
print(np.subtract(x, 5))

# np.negative()
print(np.negative(x))

# np.multiply()
print(np.multiply(x, 100))

# np.divide()
print(p.divide(x, 78))

# np.floor_divide()
print(np.floor_divide(x, 2))

# np.power()
print(np.power(x, 5))

# np.mod()
print(np.mod(x, 2))

# Absolute value
import numpy as np
np.random.seed(0) 
# Just as NumPy understands Python’s built-in arithmetic operators, it also understands Python’s built-in absolute value function:
y = np.array([-2, 3, -6, 7, -9])
print(abs(y))

# The corresponding NumPy ufunc is np.absolute, which is also available under the alias np.abs:
print(np.absolute(y), np.abs(y)) # [2 3 6 7 9]

# This ufunc can also handle complex data, in which the absolute value returns the magnitude:
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print(x, np.abs(x)) # [3.-4.j 4.-3.j 2.+0.j 0.+1.j] [5. 5. 2. 1.]


# Trigonometric functions
import numpy as np 
theta = np.linspace(0, np.pi, 3)
# Now we can compute some trigonometric functions on these values:
print("theta =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
# The values are computed to within machine precision, which is why values that should be zero do not always hit exactly zero.

# Inverse trigonometric functions are also available:
x = [-1, 0, 1]
print("x     =", x)
print("arcsin(x) =", np.arcsin(x))
print("arccos(x) =", np.arccos(x))
print("arctan(x) =", np.arctan(x))