# Functions

## Example 1: Assigning a Function to a variable 
## You can then use that variable the same as you would use the function itself:
def func():
    print('I am a func()!')

func() # Output: I am a func()!
another_name = func
another_name() # Output: I am a func()!

## Example 2: You can display a function to the console with print(), include it as an element in a composite data object like a list, or even use it as a dictionary key:
def func():
    print('I am a func()!')

print('rodgers', func, 42) # rodgers <function func at 0x0000027FC5068558> 42

objects = ["cat", func, 42]
print(objects[1]) # <function func at 0x0000027FC5068EE8>
objects[1]() # I am a func()!

d = {"cat": 1, func: 2, 42: 3}
d[func] # I am a func()!