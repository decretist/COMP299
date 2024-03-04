#
# Paul Evans (10evans@cua.edu)
# 31 March 2021
#
from typing import List
from pie_extended.cli.utils import get_tagger
from pie_extended.models.lasla import tokenizer
from pie_extended.models.lasla.imports import get_iterator_and_processor

def main():
    exceptions = open('exceptions.txt', 'w')
    samples = ['Gratian0', 'Gratian1', 'Gratian2', 'dePen']
    for sample in samples:
        x = tokenizer.LatMemorizingTokenizer()
        text = open('corpora/final/' + sample + '.txt', 'r').read()
        sentences = x._real_sentence_tokenizer(text)
        tagger = get_tagger(
            'lasla', batch_size=256, device='cpu', model_path=None
        )
        results = []
        for sentence in sentences:
            iterator, processor = get_iterator_and_processor()
            try:
                tagged = tagger.tag_str(
                    sentence, iterator=iterator, processor=processor
                )
            except:
                exceptions.write(sentence + '\n')
                exceptions.flush()
                continue
            for i in range(len(tagged)):
                if tagged[i]['pos'] != 'PUNC':
                # if tagged[i]['morph'] != 'MORPH=empty':
                    results.append(tagged[i]['lemma'])
        output = open('corpora/final_lemmas/' + sample +'.txt', 'w')
        output.write(' '.join(results) + '\n')
        output.close()
    exceptions.close()

if __name__ == '__main__':
    main()

