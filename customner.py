import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

import json

nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object

f = open('training_data.json')
TRAIN_DATA = json.load(f)

for text, annot in tqdm(TRAIN_DATA['annotations']): 
    doc = nlp.make_doc(text) 
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents 
    db.add(doc)

db.to_disk("./training_data.spacy") # save the docbin object

nlp_ner = spacy.load("model-best") 

doc = nlp_ner('''The global crypto market capitalisation tumbled 3.60 percent over the last 24 hours to 
95.77 billion.
While dogecoin''') # input sample text

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)