list_of_friends =  ["John", "Marta", "James", "Amanda", "Marianna"]
for i in range(len(list_of_friends)):
    print(list_of_friends[i].center(20, "*"))
    print(f"{list_of_friends[i] : >20}\n")
