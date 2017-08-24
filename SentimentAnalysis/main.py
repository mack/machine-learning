from classifier import *
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# load classifier
classifier = Classifier()

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST"):
        prediction_str = request.form['s']
        result = classifier.predict(prediction_str)
        if result['positive'] > result['negative']:
            print('pos')
            percentage_pos = result['positive'] / (result['positive'] + result['negative'])
            return render_template('index.html', rating='Positive', color='pos', percentage=str(percentage_pos * 100))
        else:
            print('neg')
            percentage_neg = result['negative'] / (result['positive'] + result['negative'])
            return render_template('index.html', rating='Negative', color='neg', percentage=str(percentage_neg * 100))
    else:
        return render_template('index.html')
