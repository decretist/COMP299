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

# transform output of work_2.py (items: list of tuples) into dictionary
for item in items:

    key = item[2] # extract lemma

    if key not in unique_dictionary:
        value = [(item[0], item[1])] # value: list of tuples
        unique_dictionary[key] = value
    elif key in unique_dictionary:
        value = unique_dictionary[key]
        value.append((item[0], item[1]))

# print(unique_dictionary)

for key in sorted(unique_dictionary):
   print(key + ':')
   for value in unique_dictionary[key]:
       print('\t' + str(value))


