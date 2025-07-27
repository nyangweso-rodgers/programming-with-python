class Car:
    # class variable 
    wheel = 4
    def __init__(self, color, model, year):
        # By prefixing the variable names with self, you tell Python these are attributes.
        self.color = color
        self.model = model 
        self.year = year

my_car = Car('white', 'beetle', 1967)
print(f"My car is {my_car.color}")
print(f"My car is {my_car.model}")
print(f"My car was built in {my_car.year}")
print(f"My car is a {my_car.wheel}-wheel drive")