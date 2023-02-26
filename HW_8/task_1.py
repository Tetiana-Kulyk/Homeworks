def function_name(function):

    def inner(arg1, arg2):
        return f"This is the result of the {function.__name__} function: {function(arg1, arg2)}"

    return inner


@function_name
def summation(num1, num2):
    """The function returns the sum of two numbers."""
    return num1 + num2


@function_name
def multiplication(num1, num2):
    """The function returns the product of two numbers."""
    return num1 * num2


if __name__ == '__main__':
    print(summation(2, 3))
    print(multiplication(4, 2))
