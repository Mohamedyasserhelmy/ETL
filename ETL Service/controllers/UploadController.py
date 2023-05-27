from re import template
from flask import Response, request, jsonify, redirect, flash, render_template
from flask import current_app
import pandas as pd
from werkzeug.utils import secure_filename
import os
import json

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

# posting the file to the upload service
def post_file():
    if 'file' not in request.files:
        flash("NO File Selected !!")
        return redirect(request.url)

    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        data_to_json = read_file(file)
        print(type(data_to_json[0]))
        print(data_to_json[0])
        if (data_to_json[0] != 91) and (data_to_json[0] != "["):
            return render_template("upload/incorrectfile.html")
        data_to_json = json.loads(data_to_json)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        print(type(data_to_json))
        return render_template("upload/data.html", data=data_to_json, file_name=filename)
    return Response("Please Enter A valid Data !! ")
