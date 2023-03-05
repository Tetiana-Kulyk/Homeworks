from Amphibian import Amphibian
from abc import abstractmethod

if __name__ == "__main__":
    frog = Amphibian("Edible frog", "Anura", "Ranidae", "Pelophylax", True)
    frog.simple_description()
    frog.breathe()
    frog.move()
    frog.reproduce()
