def squares_generator():
    """The generator returns the square of even number in range from 0 to 1000000000 inclusively."""
    for i in range(0, 1000000001):
        if i % 2 == 0:
            yield i ** 2
        else:
            continue


generator = squares_generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
