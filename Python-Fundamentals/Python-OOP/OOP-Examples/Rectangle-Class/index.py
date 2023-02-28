class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __repr__(self): # __repr__ is a special method used to represent a class's objects as a string.
        return f"{self.__class__.__name__}(length = {self.length}, width = {self.width})"
    
rectangles = [Rectangle(length=1, width=3), Rectangle(length=10, width=10), Rectangle(length=2, width=2)]

print(min(rectangles, key=lambda rectangle: rectangle.length * rectangle.width))