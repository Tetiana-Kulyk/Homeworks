def my_all(iterable_object):
    """The function returns True if all the elements of the iterable object are True, otherwise returns False."""
    for element in iterable_object:
        if not element:
            return False
    return True


if __name__ == '__main__':
    lst = [True, True, False]
    print(my_all(lst))
