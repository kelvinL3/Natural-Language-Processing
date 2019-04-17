from feature_NER import named_entity_recognition
from word_embeddings import get_word_embeddings
from lengthOfDocument import length_of_document
import csv

def store_features(lyrics):
    # do stuff
    return 0

with open("lyrics.csv") as lyrics:
    reader = csv.reader(lyrics)
    next(reader, None)
    for line in reader:
        store_features(line[-1])