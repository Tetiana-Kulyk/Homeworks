import Mammal

if __name__ == "__main__":
    wolf = Mammal("Canis lupus", "Carnivora", "Canidae", "Canis", True)
    wolf.simple_description()
    wolf.breathe()
    wolf.move()
    wolf.reproduce()