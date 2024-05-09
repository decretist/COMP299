
# Jake Bayon (jbayon@sandiego.edu)
# COMP 499
# 9 May 2024

from typing import List
from pie_extended.cli.utils import get_tagger
from pie_extended.models.lasla import tokenizer
from pie_extended.models.lasla.imports import get_iterator_and_processor
import os
results = []
x = tokenizer.LatMemorizingTokenizer()
text = open('corpora/final/Gratian2.txt', 'r').read()
sentences = x._real_sentence_tokenizer(text)
model_name = 'lasla'
tagger = get_tagger(model_name, batch_size=256, device='cpu', model_path=None)

# index into unlemmatized second-recension dicta
index = 0

# create results (list of tuples with index, form, lemma)
for sentence in sentences:
    iterator, processor = get_iterator_and_processor()
    try:
        tagged = tagger.tag_str(sentence, iterator=iterator, processor=processor)
    except:
        print(sentence)
        continue

    for i in range(len(tagged)):
        if tagged[i]['pos'] != 'PUNC':
            results.append((index, tagged[i]['form'], tagged[i]['lemma']))
            index += 1

# initialize dictionary
unique_dictionary = {}

# loop through list of tuples
for tuple in results:

	# isolate lemma
    key = tuple[2]

	# create value (a tuple with two lists)
    if key not in unique_dictionary:
        unique_dictionary[key] = ([tuple[0]], [tuple[1]])

    elif key in unique_dictionary:
        value = unique_dictionary[key]
        value[0].append(tuple[0])
        value[1].append(tuple[1])
        unique_dictionary[key] = (value[0], list(set(value[1])))
		
# alphabetize dictionary (by keys)
sorted_dictionary = {key: unique_dictionary[key] for key in sorted(unique_dictionary)}

# print dictionary
for key in sorted_dictionary:
    print(key, ":", unique_dictionary[key])
