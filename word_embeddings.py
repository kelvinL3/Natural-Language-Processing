from gensim.models import Word2Vec
import gensim
from functools import reduce
import numpy as np

word_vecs = Word2Vec.load("word2vec.model").wv

def get_word_embeddings(tokens):
    sum = np.zeros((100,))
    for t in tokens:
        try:
            sum += word_vecs.get_vector(t)
        except KeyError as e:
            pass
    return sum
    