import Reptile

if __name__ == "__main__":
    snake = Reptile("Malayopython reticulatus", "Squamata", "Pythonidae", "Malayopython", True)
    snake.simple_description()
    snake.breathe()
    snake.move()
    snake.reproduce()