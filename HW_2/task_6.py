list_with_duplicates = ["John Dow", "John Dow", "Marta Dow"]
unique_names_list = list(dict.fromkeys(list_with_duplicates))
print(unique_names_list)
