from typing import List
from pie_extended.cli.utils import get_tagger, get_model, download

# In case you need to download
do_download = False
if do_download:
    for dl in download("lasla"):
        x = 1

# model_path allows you to override the model loaded by another .tar
model_name = "lasla"
tagger = get_tagger(model_name, batch_size=256, device="cpu", model_path=None)

sentences: List[str] = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. "]
# Get the main object from the model (: data iterator + postprocesor
from pie_extended.models.lasla.imports import get_iterator_and_processor
for sentence_group in sentences:
    iterator, processor = get_iterator_and_processor()
    print(tagger.tag_str(sentence_group, iterator=iterator, processor=processor) )
