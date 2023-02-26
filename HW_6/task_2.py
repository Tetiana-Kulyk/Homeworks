import math


def square(side):
    """
    Find the perimeter, area and diagonal of the square
    """
    perimeter = 4 * side
    area = side * 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)

print(square(3))
