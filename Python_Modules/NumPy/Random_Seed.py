# NUMPY RANDOM SEED

## NUMPY RANDOM SEED IS FOR PSEUDO-RANDOM NUMBERS IN PYTHON
'''
NumPy random seed is simply a function that sets the random seed of the NumPy pseudo-random number generator. 
It provides an essential input that enables NumPy to generate pseudo-random numbers for random processes.
'''

### A QUICK INTRODUCTION TO PSEUDO-RANDOM NUMBERS
'''
A pseudo-random number is a number. A number that’s sort-of random -- Pseudo-random.
So essentially, a pseudo-random number is a number that’s almost random, but not really random.

Pseudo-random numbers are computer generated numbers that appear random, but are actually predetermined.
'''

### PSEUDO-RANDOM NUMBERS APPEAR TO BE RANDOM
'''
For example, here we’ll create some pseudo-random numbers with the NumPy randint function:
'''
import numpy as np
np.random.seed(1)
np.random.randint(low = 1, high = 10, size = 50)
'''
I can assure you though, that these numbers are not random, and are in fact completely determined by the algorithm. 
If you run the same code again, you’ll get the exact same numbers.
'''

## GENERATE PSEUDO-RANDOM INTEGERS
'''
Here, we’ll create a list of 5 pseudo-random integers between 0 and 9 using numpy.random.randint.
'''
np.random.seed(0)
np.random.randint(10, size = 5) # array([5, 0, 3, 3, 7])

## Remark
### NUMPY.RANDOM.SEED PROVIDES AN INPUT TO THE PSEUDO-RANDOM NUMBER GENERATOR
'''
The numpy.random.seed function provides the input (i.e., the seed) to the algorithm that generates pseudo-random numbers in NumPy.

The np.random.seed function provides an input for the pseudo-random number generator in Python.
That’s all the function does!

It allows you to provide a “seed” value to NumPy’s random number generator.

# NUMPY RANDOM SEED IS DETERMINISTIC
-- pseudo-random number generators are completely deterministic. They operate by algorithm.
-- What this means is that if you provide the same seed, you will get the same output.
-- And if you change the seed, you will get a different output.
-- The output that you get depends on the input that you give it.

# NUMPY RANDOM SEED MAKES YOUR CODE REPEATABLE
-- There are times when you really want your “random” processes to be repeatable.
-- Code that has well defined, repeatable outputs is good for testing.
-- Essentially, we use NumPy random seed when we need to generate pseudo-random numbers in a repeatable way.
'''

## GENERATE A RANDOM NUMBER WITH NUMPY.RANDOM.RANDOM
### generate a random number between zero and one. 
np.random.seed(0) # Essentially, if you execute a NumPy function with the same seed, you’ll get the same result.
np.random.random()  # 0.5488135039273248 # Note that the output is a float. It’s a decimal number between 0 and 1.

## GENERATE A RANDOM INTEGER WITH NUMPY.RANDOM.RANDINT
### use NumPy to generate 5 random integers between 0 and 99.
np.random.seed(74)
np.random.randint(low = 0, high = 100, size = 5) # array([30, 91,  9, 73, 62])


## SELECT A RANDOM SAMPLE FROM AN INPUT ARRAY
'''
It’s also common to use the NP random seed function when you’re doing random sampling.
Specifically, if you need to generate a reproducible random sample from an input array, you’ll need to use numpy.random.seed.

Here, we’re going to use numpy.random.seed before we use numpy.random.choice. 
The NumPy random choice function will then create a random sample from a list of elements.

In the output, you can see that some of the numbers are repeated. 
This is because np.random.choice is using random sampling with replacement. 
'''
np.random.seed(0)
np.random.choice(a = [1,2,3,4,5,6], size = 5)

## WHAT NUMBER SHOULD I USE IN NUMPY RANDOM SEED?
'''
-- Basically, it doesn’t matter.
-- You can use numpy.random.seed(0), or numpy.random.seed(42), or any other number.

-- For the most part, the number that you use inside of the function doesn’t really make a difference.
-- You just need to understand that using different seeds will cause NumPy to produce different pseudo-random numbers. 
-- The output of a numpy.random function will depend on the seed that you use.
'''

# WHAT’S THE DIFFERENCE BETWEEN NP.RANDOM.SEED AND NP.RANDOM.RANDOMSTATE?
'''
-- Essentially, numpy.random.seed sets a seed value for the global instance of the numpy.random namespace.
-- On the other hand, np.random.RandomState returns one instance of the RandomState and does not effect the global RandomState.
'''

# APPLICATIONS OF NP.RANDOM.SEED
## 1. PROBABILITY AND STATISTICS
## 2. RANDOM SAMPLING
## 3. MONTE CARLO METHODS - Monte Carlo methods are a class of computational methods that rely on repeatedly drawing random samples.
## 4. MACHINE LEARNING
## 5. DEEP LEARNING