from classifier import * # my classifier class
# For the images:
import os
import cv2
import numpy as np
# For the web stuff:
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename

# Other global variables
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'static/img/uploads'

# Create flask obj and init values
app = Flask(__name__)
app.config['UPLOADS_FOLDER'] = UPLOAD_FOLDER

# Create classifier obj
c = Classifier()
c.load_model()

# taken from flask official website (will update with link)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Handle index
@app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        if 'photo' not in request.files: # Has the photo been provided
            return redirect(request.url)
        photo = request.files['photo']
        if photo.filename == '': # Does the photo have a name
            return redirect(request.url)
        if photo and allowed_file(photo.filename): # Is the photo null and is the name valid
            # Save photo for later use in training
            filename = secure_filename(photo.filename)
            path = os.path.join(app.config['UPLOADS_FOLDER'], filename)
            photo.save(path)

            # Convert photo data into usable np array for our classifier
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (50, 50))
            img = np.array(img)
            img = img.reshape(50, 50, 1)
            output = c.predict(img)
            return render_template("index.html", img=path, prediction_val=output['prediction_val'], prediction=output['prediction'])
        else:
            return redirect(request.url)
    else:
        return render_template("index.html")
