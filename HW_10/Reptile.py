import Chordate


class Reptile(Chordate):
    def __init__(self, name: str, order: str, family: str, genus: str, crawling: bool):
        super().__init__(name, order, family, genus)
        self.__crawling = crawling

    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        print(f"{self._name} can breathe with lungs.")

    def move(self):
        """The function returns the way how this chordates animal can move."""
        if self.__crawling:
            print(f"{self._name} can move by crawling.")
        else:
            print(f"{self._name} can move.")

    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        print(f"{self._name} can reproduce by laying eggs.")
