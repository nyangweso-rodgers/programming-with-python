class Animal():
    # parent "Animal" class
    def __init__(self, num_of_legs):
        
class Cow(Animal):
    # child class "Cow" inherits "Animal"
    def __init__(self):
        # call the parent class to 
        # give the coe some legs
        super().init(4)