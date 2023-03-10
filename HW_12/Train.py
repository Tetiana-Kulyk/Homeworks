class Train:
    def __init__(self, name: str):
        self.__name = name
        self.__length = list()

    def __len__(self):
        return len(self.__length)

    def __add__(self, wagon):
        self.__length.append(str(wagon))

    def __str__(self):
        lst = ["["+i+"]" for i in self.__length]
        return f"<=[HEAD]-{'-'.join(lst)}"
