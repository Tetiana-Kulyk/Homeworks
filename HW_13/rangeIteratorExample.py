from rangeIterator import RangeIterator

if __name__ == '__main__':
    my_iterator = RangeIterator([11, 1, 23, 24, 2, 9, 44, 6, 9], 2, 6)
    for item in my_iterator:
        print(item)
