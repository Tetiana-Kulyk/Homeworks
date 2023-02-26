import os
import random

list_of_tuples = []
count = 0

if __name__ == '__main__':
    os.getcwd()
    print(os.getcwd())
    # os.makedirs("HW_5/test/data")
    os.getcwd()
    print(os.getcwd())
    os.chdir("./test/data")
    print(os.getcwd())
    while count < 100:
        list_of_tuples.append((random.randint(4, 100), random.randint(4, 100), random.randint(1, 3)))
        count += 1

    with open("text_HW5.txt", "w+") as file:
        for i in list_of_tuples:
            for j in i:
                if j == i[2]:
                    file.write(str(j) + "\n")
                else:
                    file.write(str(j) + " ")
