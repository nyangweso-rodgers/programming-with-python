# dog class with a class attribute

# class attributes are attributes that have the same value for all class instances.
# the following Dog class has a __class attribute__ called _species_ with the value "Canis familiaris": 
class Dog:
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
buddy = Dog('buddy', 3)
Miles = Dog('neo', 4)

print(buddy.name)
print(buddy.age)

# You can access class attributes the same way:
print(buddy.species)