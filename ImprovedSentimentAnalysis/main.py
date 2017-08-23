import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # load in data
    train_data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    test_data = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3)

    # format data
    train = []
    for i in range(0, len(train_data["review"])):
        train.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train_data['review'][i], True)))

    vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000)
    train_features = vectorizer.fit_transform(train)
    np.asarray(train_features)

    # train model
    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(train_features, train_data["sentiment"])

    # save the model with sklearn joblib
    joblib.dump(forest, 'sentiment.pkl')
