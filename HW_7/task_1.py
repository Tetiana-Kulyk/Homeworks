import sys


def my_print(text):
    """The function outputs the input text or the value of the variable to console."""
    tmp_stdout = sys.stdout
    sys.stdout.write(text)

if __name__ == '__main__':
    my_print("Hi Peter")
