class Dog:
    # class attribute
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self): # .description() returns a string displaying the name and age of the dog.
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}" # .speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.
    
miles = Dog("Miles", 4)
# .description() returns a string containing information about the Dog instance miles.
print(miles.description())

print(miles.speak("Woof Woof"))

print(miles.speak("Bow Wow"))

print(miles) # <__main__.Dog object at 0x00000257D056BFA0>