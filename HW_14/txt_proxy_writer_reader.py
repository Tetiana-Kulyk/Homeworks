from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_to_file(self):
        self.__is_actual = False
        new_data = input()
        if new_data == self.__result:
            raise Exception("This file already contains this data. Please send new data.")
        else:
            self.__txt_writer.write(new_data)
            return self.read_file()
