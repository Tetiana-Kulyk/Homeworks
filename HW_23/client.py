import config


class BaseDB:
    def __init__(self, collection):
        self.client = config.client
        self.db = self.client[config.database]
        self.collection = self.db[collection]

    def insert_one(self, dictionary):
        return self.collection.insert_one(dictionary)

    def insert_many(self, list_of_dicts):
        return self.collection.insert_many(list_of_dicts)

    def find_one(self, data):
        return self.collection.find_one(data)

    def find_all(self):
        return self.collection.find()

    def find_by_query(self, query):
        return self.collection.find(query)
