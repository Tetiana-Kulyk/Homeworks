from Chordate import Chordate


class Fish(Chordate):
    def __init__(self, name: str, order: str, family: str, genus: str, underwater_breathing: bool, swimming: bool):
        super().__init__(name, order, family, genus)
        self.__underwater_breathing = underwater_breathing
        self.__swimming = swimming

    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        if self.__underwater_breathing:
            print(f"{self._name} can breathe with gills under the water.")
        else:
            print(f"{self._name} can breathe.")

    def move(self):
        """The function returns the way how this chordates animal can move."""
        if self.__swimming:
            print(f"{self._name} can move under the water.")
        else:
            print(f"{self._name} can move.")

    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        print(f"{self._name} can reproduce by spawning.")
