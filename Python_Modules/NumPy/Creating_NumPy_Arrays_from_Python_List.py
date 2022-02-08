# Creating Numpy Arrays from Pthon List

import numpy as np 
# First, we can use np.array to create arrays from Python lists:
# integer array
print(np.array([1, 4, 2, 5, 3])) # [1 4 2 5 3]

# Remember that unlike Python lists, NumPy is constrained to arrays that all contain the same type. 
# If types do not match, NumPy will upcast if possible 
# (here, integers are upcast to floating point):
print(np.array([3.14, 5, 8, 6])) # [3.14 5.   8.   6.  ]

# If we want to explicitly set the data type of the resulting array, we can use the dtype keyword:
print(np.array([4.14, 7.8, 5, 8], dtype = 'float32')) # [4.14 7.8  5.   8.  ]

# Finally, unlike Python lists, NumPy arrays can explicitly be multidimensional; 
# here’s one way of initializing a multidimensional array using a list of lists:
print(np.array([range(i, i + 3) for i in[2, 4, 6]]))