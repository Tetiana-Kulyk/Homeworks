from Chordate import Chordate


class Mammal(Chordate):
    def __init__(self, name: str, order: str, family: str, genus: str, breastfeeding: bool):
        super().__init__(name, order, family, genus)
        self.__breastfeeding = breastfeeding

    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        print(f"{self._name} can breathe with lungs.")

    def move(self):
        """The function returns the way how this chordates animal can move."""
        print(f"{self._name} can move on land.")

    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        if self.__breastfeeding:
            print(f"{self._name} can reproduce and feed the offspring with milk.")
        else:
            print(f"{self._name} can reproduce.")
