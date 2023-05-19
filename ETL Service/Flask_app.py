from flask import Flask, request, Response, flash, redirect
from flask import render_template
import pandas as pd
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Checking if the type is allowed 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def mainPage():
    return "<p> welcome to flask Application </p>"

@app.route("/csv")
def csvParser():
    return render_template("csv.html")

@app.post("/csvUploader")
def post_csv_file():
    if 'file' not in request.files:
        flash("NO file selected !!")
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data_to_json = pd.read_csv(request.files['file']).to_json(orient='records')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return Response(data_to_json, mimetype='application/json')
    return Response("Please Enter A valid Data !! ")


if (__name__ == '__main__'):
    app.run(host='0.0.0.0')