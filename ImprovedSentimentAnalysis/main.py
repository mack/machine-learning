import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import numpy as np

if __name__ == '__main__':
    forest = joblib.load('sentiment.pkl')
    vectorizer = joblib.load('sentiment_vectorizer.pkl')

    prediction_str = "This was a terrible movie. I would not watch it."
    prediction_str = [" ".join(KaggleWord2VecUtility.review_to_wordlist(prediction_str, True))]
    prediction_str = vectorizer.transform(prediction_str)
    np.asarray(prediction_str)
    result = forest.predict(prediction_str)
    print(result)
