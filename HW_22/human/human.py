import json
from dict2xml import dict2xml


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def get_dict(self):
        return self.__dict__

    def convert_to_json(self):
        with open("converted_to_json.json", 'w+') as file:
            file.write(json.dumps(self.get_dict()))

    def convert_to_xml(self):
        with open("converted_to_xml.xml", 'w+') as file:
            file.write(dict2xml(self.get_dict()))
