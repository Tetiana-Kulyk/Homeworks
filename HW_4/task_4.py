camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for i in range(len(camel_case_list)):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_case_list.append(pattern.sub('_', camel_case_list[i]).lower())
print(snake_case_list)
