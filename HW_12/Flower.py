# task1

class Flower:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}: \n\t{self.__dict__}"
