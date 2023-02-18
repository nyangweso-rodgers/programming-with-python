# Data Structures & Algorithms with Python

## Table of Contents
1. [Introduction to Algorithms & Data Structures with Python](#Introduction-to-Algorithms-and-Data-Structures-with-Python)
2. [Stack](#Stack)
    - Implementation
    - Operations
    - Characteristics
    - Use cases

3. [Queue](#Queue)
    - Implementation
    - Operations
    - Characteristics
    - Use cases

3. [References](#References)
    - [Introduction to Data Structures and Algorithms With Python](https://dev.to/grayhat/introduction-to-data-structures-and-algorithms-with-python-4ih1)

# Introduction to Algorithms and Data Structures with Python
* __Data structures__ in Python deal with the organization and storage of data in the memory while a program is processing it. 
* Python __algorithms__ refer to the detailed set of instructions that helps in the processing of data for a specific purpose.

__Stacks__ and __Queues__ are the earliest data structure defined in computer science. A simple Python __list__ can act as a __queue__ and __stack__, also we can implement __stack__ and __queue__ using __classes__ and __functions__. A __queue__ follows __FIFO__ rule (__First In First Out__) and used in programming for __sorting__. It is common for __stacks__ and __queues__ to be implemented with an __array__ or __linked list__.

# Stack
* Follows __LIFO__(Last In First Out) principle.
* To __implement__ a stack, we need two simple operations:
    - __push__: adds an element to the top of the stack.
    - __pop__: removes an element from the top of the stack.
* __Operations__:
    - __Addition__: adds the items in the stack and increases the stack size. The addition takes place at the top of the stack.
    - __Deletion__: consists of two conditions, first, if no element is present in the stack, then underflow occurs in the stack, and second, if a stack contains some elements, then the topmost element gets removed. It reduces the stack size.
    - __Traversing__: involves visiting each element of the stack.
* __Characteristics__ include:
    - Insertion order of the stack is preserved.
    - Useful for parsing the operations.
    - Duplicacy is allowed.
* __Use Cases__ include:
    - _Imagine you're a software engineer working on a brand new word processor. You're tasked with creating an undo feature - allowing users to backtrack their actions till the beginning of the session. A __stack__ is an ideal fit for this scenario. We can record every action the user takes by pushing it to the stack. When the user wants to undo an action they'll pop it from the stack._

# Queue
* follows the __First-in-First-Out__ (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 
* To implement a queue, we need two simple operations:
    - __enqueue__ - It adds an element to the end of the queue.
    - __dequeue__ - It removes the element from the beginning of the queue.

* __Operations__ include:
    - __Addition__: It adds the element in a queue and takes place at the rear end, i.e., at the back of the queue.
    - __Deletion__: It consists of two conditions - If no element is present in the queue, __Underflow__ occurs in the queue, or if a stack contains some elements then element present at the front gets deleted.
    - __Traversing__: involves to visit each element of the queue.

* __Characteristics__ include:
    - Insertion order of the queue is preserved.
    - Duplicacy is allowed.
    - Useful for parsing CPU task operations.