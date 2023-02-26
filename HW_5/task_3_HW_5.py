import os
import re

if __name__ == '__main__':
    os.getcwd()
    print(os.getcwd())
    os.chdir("./test/data")
    print(os.getcwd())
    with open('text.txt', "r") as file:
        my_file = file.read()
        filtered = re.findall(r'[A-z]', my_file)
        for i in filtered:
            print(f'Number of occurence of {i}:', filtered.count(i))
