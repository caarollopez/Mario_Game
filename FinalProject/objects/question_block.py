from special_object import SpecialObject


class QuestionBlock(SpecialObject):
    """This class creates a question block of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the question block"""
        return 0, 16, 0, 16, 16