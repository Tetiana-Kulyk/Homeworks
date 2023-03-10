from HomeTask12.Train import Train
from HomeTask12.Wagon import Wagon

if __name__ == '__main__':
    train = Train("Toyota")
    print(len(train))
    wagon = Wagon(1)
    print(len(wagon))
    train + wagon
    print(len(train))
    wagon + "Jimme Tracey"
    wagon2 = Wagon(2)
    print(len(wagon))
    print(wagon)
    train + wagon2
    print(train)
