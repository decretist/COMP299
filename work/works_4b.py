#
# Paul Evans (pevans@sandiego.edu)
# Jake Bayon (jbayon@sandiego.edu)
# COMP 499
# 9 May 2024
#
from typing import List
from pie_extended.cli.utils import get_tagger
from pie_extended.models.lasla import tokenizer
from pie_extended.models.lasla.imports import get_iterator_and_processor
import os
def main():
    results = []
    x = tokenizer.LatMemorizingTokenizer()
    text = open('corpora/final/Gratian2.txt', 'r').read()
    sentences = x._real_sentence_tokenizer(text)
    model_name = 'lasla'
    tagger = get_tagger(
        model_name, batch_size=256, device='cpu', model_path=None
    )
    
    # index into unlemmatized second-recension dicta
    index = 0

    for sentence in sentences:
        iterator, processor = get_iterator_and_processor()
        try:
            tagged = tagger.tag_str(
                sentence, iterator=iterator, processor=processor
            )
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
    
    # identify unique lemmas
    tmp = []
    for i in range(len(results)):
        if results[i][2] not in first_recension_lemmas:
            tmp.append(results[i])
    results = tmp

    # output unique lemmas
    f = open('results.' + str(os.getpid()), 'w')
    for i in range(len(results)):
        f.write(str(results[i]) + '\n')
    f.close()

    uniques = {}
    
    # transform output of work_2.py (results: list of tuples) into dictionary
    for result in results:
    
        # extract index, form, and lemma
        index = result[0]
        form  = result[1]
        lemma = result[2]
    
        if lemma not in uniques:
            uniques[lemma] = {form: [index]}
        elif lemma in uniques:
            entry = uniques[lemma]
            if form not in uniques[lemma]:
                entry[form] = [index]
            elif form in uniques[lemma]:
                entry[form].append(index)
    
    for lemma in sorted(uniques):
        print(lemma + ':')
        entry = uniques[lemma]
        for form in sorted(entry):
            print('\t' + form + ': ' + str(entry[form]))

if __name__ == '__main__':
    main()

