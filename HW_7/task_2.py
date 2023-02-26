def is_int(object):
    """The function returns True if the object is an integer, else - False."""
    if type(object) == int:
        return True
    else:
        return False


def my_filter(function, iterable_object):
    """The function filters the iterable objects by the logic of the selected function."""
    return [element for element in iterable_object if function(element)]


if __name__ == '__main__':
    var = [1, "ho", 3.4, 6]
    print(my_filter(is_int, var))
