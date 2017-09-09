# logistic regression on mnist instead of a superior deep convolution net
from flask import Flask, render_template, request, redirect
from train import *
import json

app = Flask(__name__)
c = classifier()


@app.route('/', methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        img = request.form['img']
        img_parsed = json.loads(img)
        prediction = c.predict(img_parsed)
        return render_template("index.html", predicted_value=prediction)
    else:
        return render_template("index.html")
