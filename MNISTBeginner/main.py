# logistic regression on mnist instead of a superior deep convolution net
from flask import Flask, render_template, request, redirect
from train import *

app = Flask(__name__)
c = classifier()


@app.route('/', methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        print(request.form['img'])
        return render_template("index.html", img='2')
    else:
        return render_template("index.html")
