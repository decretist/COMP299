#
# Paul Evans (pevans@sandiego.edu)
# 6 May 2024
#

items = [
    (0, 'natura', 'natura'),
    (1, 'naturae', 'natura'),
    (2, 'naturae', 'natura'),
    (3, 'naturam', 'natura'),
    (4, 'natura', 'natura')
]

unique_dictionary = {}

for item in items:
    key = item[2]
    print(key)
    if key not in unique_dictionary:
        unique_dictionary[key] = ([item[0]], [item[2]])
    elif key in unique_dictionary:
        value = unique_dictionary[key]
        value[0].append(item[0])
        value[1].append(item[1])
        unique_dictionary[key] = (value[0], list(set(value[1])))

print(unique_dictionary)    

