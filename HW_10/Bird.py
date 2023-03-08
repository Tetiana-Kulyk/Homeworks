from Chordate import Chordate


class Bird(Chordate):
    def __init__(self, name: str, order: str, family: str, genus: str, flying: bool):
        super().__init__(name, order, family, genus)
        self.__flying = flying

    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        print(f"{self._name} can breathe with lungs.")

    def move(self):
        """The function returns the way how this chordates animal can move."""
        if self.__flying:
            print(f"{self._name} can move both on land and in the air.")
        else:
            print(f"{self._name} can move.")

    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        print(f"{self._name} can reproduce by laying eggs.")
