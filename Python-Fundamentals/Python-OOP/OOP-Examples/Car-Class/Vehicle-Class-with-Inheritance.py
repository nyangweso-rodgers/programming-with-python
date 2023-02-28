# update the Car class by breaking it into two categories, one for vehicles, and one for devices that use electricity:
class Vehicle:
    # A Vehicle is defined as having .color and .model attributes.
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
class Device:
    # a Device is defined to have a ._voltage attribute
    def __init__(self):
        self._voltage = 12
        
class Car(Vehicle, Device):
    # The color, model, and _voltage attributes will be part of the new Car class.
    def __init__(self, color, model, year):
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year
        
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems!")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage
        
my_car = Car("yellow", "beetle", 1969)
print(f"My car is {my_car.color}")
print(f"My car uses {my_car.voltage} volts")
my_car.voltage = 6
print(f"My car now uses {my_car.voltage} volts")

# Examining an Object’s Attributes
print(dir(my_car))
    