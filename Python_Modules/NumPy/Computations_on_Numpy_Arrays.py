# Computations on Numpy Arrays
'''
# Attributes of arrays: 
# Determining the size, shape, memory consumption, and data types of arrays

# Indexing of arrays: 
Getting and setting the value of individual array elements

# Slicing of arrays
Getting and setting smaller subarrays within a larger array

# Reshaping of arrays
Changing the shape of a given array

Joining and splitting of arrays:
Combining multiple arrays into one, and splitting one array into many
'''
import numpy as np
from numpy import random
from numpy.core.fromnumeric import size 
np.random.seed(0) # seed for reproducability
x1 = np.random.randint(10, size = 6) # one dimensional array
x2 = np.random.randint(10, size = (3, 4)) # Two - dimensional array
x3 = np.random.randint(10, size = (3, 4, 5)) # three-dimensional array

# Each array has attributes ndim (the number of dimensions), 
# shape (the size of each dimension), 
# and size (the total size of the array):
print("x3 ndim: ", x3.ndim) # x3 ndim:  3
print("x3 shape: ", x3.shape) # x3 shape:  (3, 4, 5)
print("x3 size: ", x3.size) # x3 size:  60

# Another useful attribute is the dtype, the data type of the array
print("x3 dtype: ", x3.dtype) # x3 dtype:  int32


# Other attributes include itemsize, which lists the size (in bytes) of each array element,
# and nbytes, which lists the total size (in bytes) of the array:
print("itemsize: ", x3.itemsize, 'bytes') # itemsize:  4 bytes
print("nbytes: ", x3.nbytes, 'bytes') # In general, we expect that nbytes is equal to itemsize times size. # bytes:  240 bytes


## Array Indexing: Accessing Single Elements
'''
If you are familiar with Python’s standard list indexing, indexing in NumPy will feel
quite familiar. In a one-dimensional array, you can access the ith value (counting from
zero) by specifying the desired index in square brackets, just as with Python lists:
'''
print(x1) # [5 0 3 3 7 9]
print(x1[0], x1[4]) # 5 7
# To index from the end of the array, you can use negative indices:
print(x1[-1], x1[-2]) # 9 7

# In a multidimensional array, you access items using a comma-separated tuple of indices:
print(x2)
print(x2[0, 0], x2[1, 3], x2[2, -1]) # 3 8 7

# You can also modify values using any of the above index notation:
x2[0, 0] = 12
print(x2)

# Keep in mind that, unlike Python lists,NumPy arrays have a fixed type. 
# This means,for example, that if you attempt to insert a floating-point value to an integer array, the value will be silently truncated. 
# Don’t be caught unaware by this behavior!
x2[0, 1] = 12.55
print(x2)


### Array Slicing: Accessing Subarrays
'''
Just as we can use square brackets to access individual array elements, we can also use
them to access subarrays with the slice notation, marked by the colon (:) character.
The NumPy slicing syntax follows that of the standard Python list; to access a slice of
an array x, use this:

x[start:stop:step]

If any of these are unspecified, they default to the values start=0, stop=size of
dimension, step=1. We’ll take a look at accessing subarrays in one dimension and in
multiple dimensions.
'''

import numpy as np  
x = np.arange(10)
print(x) # [0 1 2 3 4 5 6 7 8 9]
# first 3 elements
print(x[:3]) # [0 1 2]
# last 3 elements
print(x[-3:]) # [7 8 9]
# middle sub-array
print(x[4:7]) # [4 5 6]
# every other element
print(x[::2]) # [0 2 4 6 8]
# every other elemnt starting at index 1
print(x[1::2]) # [1 3 5 7 9]

# A potentially confusing case is when the step value is negative. 
# In this case, the defaults for start and stop are swapped. 
# This becomes a convenient way to reverse an array:
print(x[::-1], x[::-2], x[::-3], x[::-4], x[::-5], x[::-6]) # [9 8 7 6 5 4 3 2 1 0] [9 7 5 3 1] [9 6 3 0] [9 5 1] [9 4] [9 3]

# reverse every other elemnt from index 5
print(x[5::-1]) # [5 4 3 2 1 0]

## Multi-dimensional Arrays

import numpy as np
np.random.seed(0)
x2 = np.random.randint( 10, size = (3,4))
print(x2)
# two rows, 3 columns
print(x2[:2,:3])
# two rows, 3 columns
print(x2[0:2, 0:3])
# 2 rows, every other column
print(x2[::2, 2::2])
# Finally, subarray dimensions can even be reversed together:
print(x2[::-1, ::-1])


# Accessing array rows and columns. 
'''
One commonly needed routine is accessing single rows or columns of an array. 
You can do this by combining indexing and slicing, using an empty slice marked by a single colon (:):
'''

import numpy as np 
np.random.seed(0)
x = np.random.randint(10, size = (3, 4))
print(x)
# first column
print(x[:, 0]) # [5 7 2]
# first row
print(x[0, :]) # [5 0 3 3]
# In the case of row access, the empty slice can be omitted for a more compact syntax:
print(x[0]) #  a more compact syntax # [5 0 3 3]


# Subarrays as no-copy views
'''
One important—and extremely useful—thing to know about array slices is that they return views rather than copies of the array data. 
This is one area in which NumPy array slicing differs from Python list slicing: 
in lists, slices will be copies. Consider our two-dimensional array from before:
'''

import numpy as np  
np.random.seed(0)
x = np.random.randint(10, size = (3, 4))
print(x)
# let'e extract a 2x2 subarray from this
x_sub = x[:2, :2]
print(x_sub)
# Now if we modify this subarray, we’ll see that the original array is changed! Observe:
x_sub[0, 0] = 999999
print(x_sub)
print(x)

'''
REMARK:
This default behavior is actually quite useful: it means that when we work with large
datasets, we can access and process pieces of these datasets without the need to copy
the underlying data buffer.
'''

#Creating copies of arrays
'''
Despite the nice features of array views, it is sometimes useful to instead explicitly
copy the data within an array or a subarray. This can be most easily done with the
copy() method:
'''

import numpy as np
np.random.seed(0) 
x = np.random.randint(10, size=(3,4))
print(x)
x_sub_copy = x[:2, :2].copy()
print(x_sub_copy)
# If we now modify this subarray, the original array is not touched:
x_sub_copy[0, 0] = 111
print(x_sub_copy)
print(x)


# Reshaping of Arrays
'''
Another useful type of operation is reshaping of arrays. The most flexible way of doing this is with the reshape() method. 
For example, if you want to put the numbers 1 through 9 in a 3×3 grid, you can do the following:
'''

import numpy as np
grid = np.arange(1, 10)
print(grid) # [1 2 3 4 5 6 7 8 9]
# reshape to 3x3
print(grid.reshape(3, 3))
# column vector via reshape method
print(grid.reshape(9, 1))
# column vector vis newaxis
print(grid[:, np.newaxis])


# Array Concatenation and Splitting
'''
All of the preceding routines worked on single arrays. It’s also possible to combine
multiple arrays into one, and to conversely split a single array into multiple arrays.
'''

# Concatenation of arrays
'''
Concatenation, or joining of two arrays in NumPy, is primarily accomplished through the routines np.concatenate, np.vstack, and np.hstack. 
np.concatenate takes a tuple or list of arrays as its first argument, as we can see here:
'''

import numpy as np 
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))

# np.concatenate can also be used for two-dimensional arrays:
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(np.concatenate([grid, grid]))

# concatenate along the second axis (zero-indexed)
print(np.concatenate([grid, grid], axis = 1))

# For working with arrays of mixed dimensions, it can be clearer to use the np.vstack (vertical stack) and  np.hstack (horizontal stack) functions:
import numpy as np
x = np.array([1, 2, 3])
grid = np.array([[1, 2, 3], 
                 [4, 5, 6]])
# vertically, stack the arrays
print(np.vstack([x, grid]))

# horizontally, stack the arrays
z = np.array([[99], 
              [100]])
print(np.hstack([grid, z]))

# Similarly, np.dstack will stack arrays along the third axis.
import numpy as np 
x3 = np.array([[10, 11, 12],
              [13, 14, 15]])
y3 = np.array([[16, 17, 18],
              [19, 20, 21]])
print(np.dstack([x3, y3]))

# Splitting of arrays
'''
The opposite of concatenation is splitting, which is implemented by the functions np.split, np.hsplit, and np.vsplit. 
For each of these, we can pass a list of indices giving the split points:
'''

import numpy as np
x = [1,2,3,99,99,3,2,1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3) # [1 2 3] [99 99] [3 2 1]
# Notice that N split points lead to N + 1 subarrays. The related functions np.hsplit and np.vsplit are similar:

grid = np.arange(16).reshape(4,4)
print(grid)
# upper, lower
upper, lower = np.vsplit(grid, [2])
print(upper, lower)
# left, right
left, right = np.hsplit(grid, [3])
print(left, right)

# Similarly, np.dsplit will split arrays along the third axis.