class Wall():
    height = 10
    
south_wall = Wall()
print(south_wall.height) # prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height) # prints "20"