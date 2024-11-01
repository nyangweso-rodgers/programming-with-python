class Dog:
    # .__init__() initializes each new instance of the class.
    def __init__(self, name, age):
        # By prefixing the variable names with self, you tell Python these are attributes.
        
        # creates an attribute called name and assigns to it the value of the name parameter.
        self.name = name
        #  creates an attribute called age and assigns to it the value of the age parameter.
        self.age = age