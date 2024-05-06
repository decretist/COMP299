#
# Paul Evans (pevans@sandiego.edu)
# 6 May 2024
#

# (a placeholder for "results" in works_2.py)
items = [
    (0, 'natura', 'natura'),
    (1, 'naturae', 'natura'),
    (2, 'naturae', 'natura'),
    (3, 'naturam', 'natura'),
    (4, 'natura', 'natura')
]

unique_dictionary = {}

# items = list of tuples (output of previous process; works_2.py)
# transform into dictionary
for item in items:

    # isolate lemma
    key = item[2]

    # values within dicitonary = tuple w/ 2 lists
    if key not in unique_dictionary:
        unique_dictionary[key] = ([item[0]], [item[1]])

    elif key in unique_dictionary:
        value = unique_dictionary[key]
        value[0].append(item[0])
        value[1].append(item[1])
        unique_dictionary[key] = (value[0], list(set(value[1])))

print(unique_dictionary)    

