class Wagon:
    def __init__(self, number):
        self.__number = str(number)
        self.__length = []

    def __add__(self, passenger: str):
        return self.__length.append(passenger)

    def __len__(self):
        return len(self.__length)

    def __str__(self):
        return self.__number
