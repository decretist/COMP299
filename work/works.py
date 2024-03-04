# Paul Evans (10evans@cua.edu)
# 31 March 2021
from typing import List
from pie_extended.cli.utils import get_tagger
from pie_extended.models.lasla import tokenizer
from pie_extended.models.lasla.imports import get_iterator_and_processor
results = []
x = tokenizer.LatMemorizingTokenizer()
text = open('corpora/final/Gratian0.txt', 'r').read()
sentences = x._real_sentence_tokenizer(text)
model_name = 'lasla'
tagger = get_tagger(model_name, batch_size=256, device='cpu', model_path=None)
for sentence in sentences:
    iterator, processor = get_iterator_and_processor()
    try:
        tagged = tagger.tag_str(sentence, iterator=iterator, processor=processor)
    except:
        print(sentence)
        continue
    for i in range(len(tagged)):
        if tagged[i]['pos'] != 'PUNC':
        # if tagged[i]['morph'] != 'MORPH=empty':
            results.append(tagged[i]['lemma'])
f = open('corpora/final_lemmas/Gratian0.txt', 'w')
f.write(' '.join(results) + '\n')
f.close()
