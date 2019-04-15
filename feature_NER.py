
# download spacy

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm


nlp = en_core_web_sm.load()

entity_to_index_map = {
	"PERSON":0,
	"NORP":1,
	"FAC":2,
	"ORG":3,
	"GPE":4,
	"LOC":5,
	"PRODUCT":6,
	"EVENT":7,
	"WORK_OF_ART":8,
	"LAW":9,
	"LANGUAGE":10,
	"DATE":11,
	"TIME":12,
	"PERCENT":13,
	"MONEY":14,
	"QUANTITY":15,
	"ORDINAL":16,
	"CARDINAL":17,
}


def named_entity_recognition(lyric_string):
	
	missing = {}
	
	doc = nlp(lyric_string)
	# print([(X.text, X.label_) for X in doc.ents])
	# print([X.label_ for X in doc.ents])
	vector = [0] * len(entity_to_index_map)
	for X in doc.ents:
		if X.label_ not in entity_to_index_map:
			if X.label_ not in missing:
				print("Error, entity {} does not appear in entity_to_index_map".format(X.label_))
				missing[X.label_] = 1
			else:
				missing[X.label_] += 1
		else:
			vector[entity_to_index_map[X.label_]]+=1
	
	if missing:
		print("There are unrecognized labels from spacy {}".format(missing))
	# print(vector)
	return vector
	


if __name__ == "__main__":
	print(named_entity_recognition("Angela Merkel reached a deal with EU negotiators to end the trade imbalance."))