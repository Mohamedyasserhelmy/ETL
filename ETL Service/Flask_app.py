from flask import Flask, request, Response, flash, redirect, Blueprint
from flask import render_template
from config import Development_config, Production_config
from controllers.mainController import *
from controllers.UploadController import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
blueprint = Blueprint('blueprint', __name__)

# Importing Configuration from config class used for development (BEST PRACTICE)
app.config.from_object(Development_config())

# index blueprint    
blueprint.route('/', methods=['GET'])(index)

# Rendering csv template 
blueprint.route('/upload', methods=['GET'])(Parser)

# Uploading csv files and  check for it  
blueprint.route('/Uploader', methods=['POST'])(post_file)


app.register_blueprint(blueprint)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0')