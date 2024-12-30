# List Comprehension

# Example 1: perfect squares
square_list = []
for x in range(1, 11):
    square_list.append(x*x)
print(square_list)

# Example 2: using list comprehesion, we can perform the above iteration in one step
square_list = [x*x for x in range(1, 11)]
print("Result using list comprehension: ", square_list)