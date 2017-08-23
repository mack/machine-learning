import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import nltk

if __name__ == '__main__':
    # load in data
    train_data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    test_data = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3)

    train = []
    print(len(train_data["review"]))
    print(train_data['review'][0])
    # for i in range(0, len(train_data["review"])):
    #     train.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train_data['review'][i], True)))
    # print(train[0])
