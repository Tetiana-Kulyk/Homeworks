def my_min(iterable_object, amount_of_result=0):
    """The function returns the minimal value (or values) from the iterable object."""
    new_list = sorted(iterable_object)
    if amount_of_result == 0:
        return new_list[0]
    else:
        return new_list[:amount_of_result]


def my_max(iterable_object, amount_of_result=0):
    """The function returns the maximal value (or values) from the iterable object."""
    new_list = sorted(iterable_object, reverse=True)
    if amount_of_result == 0:
        return new_list[0]
    else:
        return new_list[:amount_of_result]


if __name__ == '__main__':
    lst1 = [1, 4, 5, 10]
    print(my_max(lst1, amount_of_result=2))
