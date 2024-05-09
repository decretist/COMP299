#
# Paul Evans (pevans@sandiego.edu)
# 6 May 2024
#

# (a placeholder for "results" in works_2.py)
results = [
    (0, 'natura', 'natura'),
    (1, 'naturae', 'natura'),
    (2, 'naturae', 'natura'),
    (3, 'naturam', 'natura'),
    (4, 'natura', 'natura')
]

unique_lemmas = {}

# transform output of work_2.py (results: list of tuples) into dictionary
for result in results:

    # extract index, form, and lemma
    index = result[0]
    form  = result[1]
    lemma = result[2]

    if lemma not in unique_lemmas:
        unique_lemmas[lemma] = {form: [index]}
    elif lemma in unique_lemmas:
        entry = unique_lemmas[lemma]
        if form not in unique_lemmas[lemma]:
            entry[form] = [index]
        elif form in unique_lemmas[lemma]:
            entry[form].append(index)

for lemma in sorted(unique_lemmas):
    print(lemma + ':')
    entry = unique_lemmas[lemma]
    for form in sorted(entry):
        print('\t' + form + ': ' + str(entry[form]))
