# logistic regression on mnist instead of a superior deep convolution net
from flask import Flask, render_template
from train import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def main():
    c = classifier()
    c.predict()

if __name__ == '__main__':
    main()
