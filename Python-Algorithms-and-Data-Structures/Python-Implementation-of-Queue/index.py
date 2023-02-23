import queue
#print(dir(queue))

# Queue is created as an object L
prime_numbers = queue.Queue(maxsize=10)
#print(prime_numbers) # <queue.Queue object at 0x000002A4B88E3E20>
#print(type(prime_numbers)) # <class 'queue.Queue'>

# Data is inserted in 'L' at the end using put()
prime_numbers.put(1)
prime_numbers.put(2)
prime_numbers.put(3)
prime_numbers.put(5)
prime_numbers.put(7)

# get() - takes data from the head of the Queue
print(prime_numbers.get()) # Output: 1
print(prime_numbers.get()) # Output: 2
print(prime_numbers.get()) # Output: 3
print(prime_numbers.get()) # Output: 5