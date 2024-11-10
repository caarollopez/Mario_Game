
class Object:
    """This is the mother class from which every static object will be inherited.
    That is: Pipes, HardBlock, Floor, Bush, Cloud and Mountain"""
    def __init__(self, x: int, y: int):
        """This function initializes every object.
        @x is the x coordinate
        @y is the y coordinate"""
        self.x = x
        self.y = y

    def move(self, go: str):
        """This function makes the object move to the left as Mario goes right so that it seems like he is actually
        moving"""
        if go.lower() == 'go':
            self.x -= 1

    # Creating properties and setters for the x and y coordinates in order to check its values
    @property
    def x(self):
        """It gets the Object's x coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """It gets the Object's x coordinate"""
        if type(x) != int:
            raise TypeError("It should be an integer")
        else:
            self.__x = x

    @property
    def y(self):
        """It gets the Object's y coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        """It gets the Object's y coordinate"""
        if type(y) != int:
            raise TypeError("It should be an integer")
        else:
            self.__y = y

