class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Hello, % s. You are % old." % (self.name, self.age))

# Objects of the class Emp has been made here
Emps = [Emp("john", 43),
Emp("robert", 16),
Emp("rodgers", 24)]

# Objects of the class Emp have been used here
for emp in Emps:
    emp.info()