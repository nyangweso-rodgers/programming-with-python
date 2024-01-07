# what does the below code snippet do?

def some_func(array):
    array = iter(array)
    try:
        first = next(array)
    except StopIteration:
        return True
    return all(first == x for x in array)
