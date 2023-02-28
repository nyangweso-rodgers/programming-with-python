
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
        
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# you can now instantiate some dogs of specific breeds in the interactive window:
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak('Woof'))

# To determine which __class__ a given object belongs to, you can use the built-in type():
print(type(miles))

# What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in __isinstance()__:
# Notice that isinstance() takes two arguments, an object and a class.
print(isinstance(miles, Dog)) # isinstance() checks if miles is an instance of the Dog class and returns True.

# The __miles__, __buddy__, __jack__, and __jim__ objects are all __Dog instances__, but __miles__ is not a __Bulldog instance__, and jack is not a Dachshund instance:
print(isinstance(miles, Bulldog))