class Wall():
    def __init__(self, height):
        # this stops us from accessing __height
        # property directly on an instance of a wall
        self.__height = height
        
    def get_height(self):
        return self.__height
    
        """
        - In the example above, we don't want users of the Wall class to be able to change its height.
        - We make the __height property private and expose a public get_height method so that users can still read the height of a wall without being tempted to update it.
        """
# This will stop developers from being able to do something like:
# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error