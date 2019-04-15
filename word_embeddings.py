from gensim.models import Word2Vec
import gensim
from functools import reduce
import numpy as np

word_vecs = Word2Vec.load("word2vec.model").wv

def get_word_embeddings(tokens):
    return reduce((lambda x, y: x + y), map(lambda x: np.array(word_vecs.get_vector(x)), tokens))
    