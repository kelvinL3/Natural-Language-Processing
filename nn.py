from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
import pickle
import numpy as np 
import argparse
import sys

option = len(sys.argv)

X = np.load("X.npy")
y = np.load("Y.npy")
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = MLPClassifier(hidden_layer_sizes=(100,50), max_iter=500)

def train():
    scaler = StandardScaler()

    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    clf.fit(X_train, y_train)
    # pickle.dump(clf, open("model", 'wb'))

def test():
    clf = pickle.load(open("model", 'rb'))
    predictions = clf.predict(X_test)
    sum = 0
    for i in range(len(predictions)):
        if predictions[i] == y_test[i]:
            sum += 1
    print(sum/len(predictions))

if option == 1:
    test()
else:
    train()
    test()

print("done")