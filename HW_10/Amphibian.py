from Chordate import Chordate


class Amphibian(Chordate):
    def __init__(self, name: str, order: str, family: str, genus: str, external_fertilization: bool):
        super().__init__(name, order, family, genus)
        self.__external_fertilization = external_fertilization

    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        print(f"{self._name} can breathe with lungs.")

    def move(self):
        """The function returns the way how this chordates animal can move."""
        print(f"{self._name} can move by jumping.")

    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        if self.__external_fertilization:
            print(f"{self._name} can reproduce by external fertilization.")
        else:
            print(f"{self._name} can reproduce.")
