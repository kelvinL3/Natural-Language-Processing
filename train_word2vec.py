import gensim
import csv

def train(filename):
    words = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            words.append(gensim.utils.simple_preprocess(row[-1]))
    model = gensim.models.Word2Vec(words)
    model.save("word2vec.model")

if __name__ == "__main__":
    train("lyrics.csv")