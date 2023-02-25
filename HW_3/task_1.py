list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers_list = []
even_numbers_list = []
for index, value in enumerate(list_of_elements):
    inner_tuple = index, value
    if value % 2 == 0:
        even_numbers_list.append((index,value))
    else:
        odd_numbers_list.append((index,value))
print(odd_numbers_list, even_numbers_list)
