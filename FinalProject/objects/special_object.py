
class SpecialObject:
    """This is the mother class from which every special object will be inherited.
    We consider that an special object is an object which may disappear from the screen, depending on Mario's behaviour.
    That is: Mushroom, Star, FireFlower, BreakableBlock, CoinsBlock, QuestionBlock ... """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, go: str):
        """This function makes the special object move to the left as Mario goes right so that it seems like he is actually
        moving"""
        if go.lower() == 'go':
            self.x -= 1

    # Creating properties and setters for the x and y coordinates in order to check its values
    @property
    def x(self):
        """It gets the Special Object's x coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """It checks the Special Object's x coordinate, raising errors when considered"""
        if type(x) != int:
            raise TypeError("It should be an integer")
        else:
            self.__x = x

    @property
    def y(self):
        """It gets the Special Object's y coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        """It checks the Special Object's y coordinate, raising errors when considered"""
        if type(y) != int:
            raise TypeError("It should be an integer")
        else:
            self.__y = y
