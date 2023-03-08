# How to create a dict using curly braces
fruits = {
    1: 'apple',
    2: 'orange',
    3: 'pineapple'
}
#print(fruits)
#print(type(fruits)) # <class 'dict'>

# How to create a dict using the dict() constructor

## creating a dictionary from a tuple
animals = dict(cat = 1, dog = 2, goat = 3)
#print(type(animals))
#print(animals)

## creating a dictionary from a list of tuples.
siblings = [('Robert', 1), ('Brendah', 2), ('Irine', 3)]
#print(type(siblings))

siblings_dic = dict(siblings)
#print(type(siblings_dic))
#print(siblings_dic)

# How to create a dict using the fromkeys() method
student_keys = ["Rodgers", "Omondi", "Nyangweso"]
student_values = 0 # set the default value to zero

students = dict.fromkeys(student_keys, student_values)
print(students)