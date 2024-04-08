import os

from flask import Flask

from views.course import course_view

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__), 
    'uploads'
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(course_view)