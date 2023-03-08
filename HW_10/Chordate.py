from abc import ABC, abstractmethod


class Chordate(ABC):
    def __init__(self, name: str, order: str, family: str, genus: str):
        self._kingdom = "Animalia"
        self._phylum = "Chordata"
        self._name = name
        self._order = order
        self._family = family
        self._genus = genus

    def __scientific_description(self):
        """The function returns the class description of this chordates animal."""
        return f"This is the {self._name} from the {self._kingdom} kingdom, {self._phylum} phylum, {self._order} order, {self._family} family and {self._genus} genus."

    @abstractmethod
    def breathe(self):
        """The function returns the way how this chordates animal can breathe."""
        pass

    @abstractmethod
    def move(self):
        """The function returns the way how this chordates animal can move."""
        pass

    @abstractmethod
    def reproduce(self):
        """The function returns the way how this chordates animal can reproduce."""
        pass

    def simple_description(self):
        print("The Wikipedia says: ")
        print(self.__scientific_description())
        print(f"But in simple words it is just a {self.__class__.__name__}.")
