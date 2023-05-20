from flask import Response, request, jsonify, redirect, flash
from flask import current_app
import pandas as pd
from werkzeug.utils import secure_filename
import os

# Checking if the type is allowed 
def allowed_file(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and \
           file_extension in current_app.config['ALLOWED_EXTENSIONS'] 

# Reading file based on its extension
def read_file(file):
    file_extension = file.filename.rsplit('.', 1)[1].lower()
    if (file_extension == 'xml'):
        return pd.read_xml(file.read()).to_json(orient='records')
    elif (file_extension == 'csv'):
        return pd.read_csv(file).to_json(orient='records')
    return file.read()


def post_file():
    if 'file' not in request.files:
        flash("NO File Selected !!")
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data_to_json = read_file(file)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return Response(data_to_json, mimetype='application/json')
    return Response("Please Enter A valid Data !! ")