# Creating Numpy Array from Scratch
import numpy as np

# Create a length - 10 integer array filled with zeros
zeros_arrays = np.zeros(10, dtype = 'int')
print(zeros_arrays) # [0 0 0 0 0 0 0 0 0 0]

# Create a 3 * 5 floating - point array filled with ones
ones_array = np.ones((3, 5), dtype = 'float') 
print(ones_array)

# Create a 3 * 5 array filled with 3.14
full_array = np.full((3, 5), 3.14)
print(full_array)

# Create an array filled with a linear sequence
# (this is similar to the built-in range() function)
arange_array = np.arange(0, 20, 2) # Starting at 0, ending at 20, stepping by 2
print(arange_array) # [ 0  2  4  6  8 10 12 14 16 18]

# Create an array of five values evenly spaced between 0 and 1
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)

# Create a 3x3 array of uniformly distributed
random_array = np.random.random((3, 3)) # random values between 0 and 1
print(random_array)

# Create a 3x3 array of normally distributed random values
normal_array = np.random.normal(0, 1, (3, 3)) # with mean 0 and standard deviation 1
print(normal_array)

# Create a 4x4 array of random integers in the interval [0, 10)
random_integer_array = np.random.randint(0, 10, (4, 4))
print(random_integer_array)

# Create a 4x4 identity matrix
identity_array = np.eye(4)
print(identity_array)

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location
empty_array = np.empty(4)
print(empty_array)