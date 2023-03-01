def double(element):
    """The function doubles any value."""
    return element * 2


def my_map(function, iterable_object):
    """The function applies selected function to the iterable object and returns modified object."""
    return [function(element) for element in iterable_object]


if __name__ == '__main__':
    lst = [1, "Ha", 4.5]
    print(my_map(double, lst))
