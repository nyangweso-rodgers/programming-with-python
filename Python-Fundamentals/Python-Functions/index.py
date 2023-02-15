# creating a function
def my_function():
    print("Hello Python Functions")
    
# calling a function
my_function()

# Arbitrary Arguments, *args
## If the number of arguments is unknown, add a * before the parameter name:
def my_kids(*kids):
    print("The Youngest Child is " + kids[2])
my_kids("Rodgers", "Omondi", "Nyangweso")

# Keyword Arguments
def my_cousins(cousin_1, cousin_2, cousin_3):
    print("The youngest Cousin is " + cousin_3)
    
my_cousins(cousin_1 = "Rodgers", cousin_2 = "Omondi", cousin_3 = "Nyangweso")

# Example: Arbitrary Keyword Arguments, **kwargs
## If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_siblings(**sib):
    print("His las name is " + sib["last_name"])
    
my_siblings(first_name = 'Robert', last_name = 'Okoth')

# Default Parameter Value
def countries(country = 'Kenya'):
    print("I am from " + country)
    
countries("Uganda")
countries("Tanzania")
countries()
countries("Nigeria")

# Passing a List as an Argument
def fav_food(food):
    for f in food:
        print(f)
        
fruits = ['apple', 'mango', 'oranges']
fav_food(fruits)

# Return Values
def sum(x):
    return 5 * x

print(sum(2))
print(sum(3))

# The pass statement
def pass_statement():
    pass