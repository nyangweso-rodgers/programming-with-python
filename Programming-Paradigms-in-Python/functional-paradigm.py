# functional way of finding the sum in a list

import functools

my_lists = [1, 2, 3, 4, 5]

# using lambda expression
print(functools.reduce(lambda x, y: x + y, my_lists))

# Recursive Functional Approach
def sum_the_list(my_lists):
    if len(my_lists) == 1:
        return my_lists[0]
    else:
        return my_lists[0] + sum_the_list(my_lists[1:])
print(sum_the_list(my_lists))