#
# Jake Bayon (jbayon@sandiego.edu)
# Paul Evans (pevans@sandiego.edu)
# COMP 494
# 6 May 2024
#
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

# compare with precomputed list of first-recension lemmas
f = open('corpora/final_lemmas/Gratian1.txt', 'r')
first_recension_lemmas = f.readline().split()
f.close()

# output unique lemmas
f = open('results.' + str(os.getpid()), 'w')
for i in range(len(results)):
    if results[i][2] not in first_recension_lemmas:
        f.write(str(results[i]) + '\n')
f.close()

