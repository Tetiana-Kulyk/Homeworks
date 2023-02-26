import os

variable = []


def mathematical_operations(lst):
    for i in lst:
        if lst[2] == "1":
            return int(lst[0]) + int(lst[1])
        elif lst[2] == "2":
            return int(lst[0]) - int(lst[1])
        elif lst[2] == "3":
            return int(lst[0]) * int(lst[1])


if __name__ == '__main__':
    os.getcwd()
    print(os.getcwd())
    os.chdir("./test/data")
    print(os.getcwd())
    with open('text_HW5.txt', "r") as file:
        for line in file:
            variable.append(line.split())
        for i in range(len(variable)):
            print(mathematical_operations(variable[i]))
    print(variable)
