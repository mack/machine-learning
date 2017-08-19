from classifier import *
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        if 'photo' not in request.files:
            return redirect(request.url)
        photo = request.files['photo']
        if photo.filename == '':
            return redirect(request.url)
        if photo and allowed_file(photo.filename):
            print('Yay!')
        else:
            print('Awh...')

    return render_template("index.html", pageType='test2')

if __name__ == '__main__':
    # c = Classifier();
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
