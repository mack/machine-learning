# from classifier import *
import cv2
import io
import os
import numpy as np
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'static/img/uploads'
app.config['UPLOADS_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        print(request)
        if 'photo' not in request.files:
            return redirect(request.url)
        photo = request.files['photo']
        if photo.filename == '':
            return redirect(request.url)
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            path = os.path.join(app.config['UPLOADS_FOLDER'], filename)
            photo.save(path)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (50, 50)) # resize for our classifier
            return render_template("index.html", img=path, prediction_val="93.232", prediction="DOG")
        else:
            return redirect(request.url)
    else:
        return render_template("index.html")

# if __name__ == '__main__':
#     # c = Classifier();
#     app.jinja_env.auto_reload = True
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     print('now')
#     app.run()
