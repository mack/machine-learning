import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
forest = joblib.load('sentiment.pkl')
vectorizer = joblib.load('sentiment_vectorizer.pkl')

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST"):
        prediction_str = request.form['s']
        result = classify(prediction_str)
        if result[0] == 1: return render_template('index.html', rating='Positive', color='pos')
        else: return render_template('index.html', rating='Negative', color='neg')
    else:
        return render_template('index.html')

def classify(sentiment_str):
    sentiment_str = [" ".join(KaggleWord2VecUtility.review_to_wordlist(sentiment_str, True))]
    sentiment_str = vectorizer.transform(sentiment_str)
    np.asarray(sentiment_str)
    return forest.predict(sentiment_str)
