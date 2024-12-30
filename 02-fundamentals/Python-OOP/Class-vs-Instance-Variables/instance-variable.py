class Wall():
    def __init__(self):
        self.height = 10
        
south_wall = Wall()
south_wall.height = 20 # only updates this install of the wall
print(south_wall.height) # 20

north_wall = Wall()
print(north_wall.height) # 10