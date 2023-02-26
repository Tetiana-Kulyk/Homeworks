import re
unconverted_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
keys = []
values = []
unconverted_string = unconverted_string.strip()
unconverted_string = unconverted_string.replace('sssss', '')
keys_values_list = re.split(r"[=,&]", unconverted_string)
keys_values_list = list(filter(None, keys_values_list))
for i in range(len(keys_values_list)):
    if i == 0 or i % 2 == 0:
        keys.append(keys_values_list[i])
    else:
        values.append(keys_values_list[i])
converted_dict = dict(zip(keys, values))
print(converted_dict)
