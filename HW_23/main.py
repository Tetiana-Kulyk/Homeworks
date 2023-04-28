from mongo_collection import MongoCollection

if __name__ == '__main__':
    clothes_collection = MongoCollection("clothes")
    dict1 = {"name": "skinny_jeans", "quantity": 50, "colour": "blue", "size": "XS"}
    clothes_collection.insert_one(dict1)

    list_of_dicts1 = [{"name": "silky_blouse", "quantity": 44, "colour": "white", "size": "L"},
                      {"name": "mini_skirt", "quantity": 20, "colour": "black", "size": "S"}]
    clothes_collection.insert_many(list_of_dicts1)

    print(clothes_collection.find_one({"name": "skinny_jeans"}))

    print([x for x in clothes_collection.find_all()])

    query = {"colour": "white"}
    print([x for x in clothes_collection.find_by_query(query)])
