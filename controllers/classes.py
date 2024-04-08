import os

from models.classes import Classes
from .course_class import save_course_class

from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_classes():
    return Classes.read()

def get_class_with_class_id(class_id):
    return Classes(class_id)

def save_class(class_name, class_id=None, uploaded_course_class=None):
    if class_id != None:
        classes = get_class_with_class_id(id)
        classes.class_name =(
          class_name
        )
    else:
        classes = Classes(
            class_name
        )

    classes.save()

    for course_class in uploaded_course_class:
        course_name = secure_filename(course_class.coursename)

        save_course_class(classes=classes.class_id)

        course_class.save(
            os.path.join(UPLOAD_FOLDER, course_name)
        )

    return course_class
    
def delete_classes(classes_id):
    Classes = get_class_with_class_id(classes_id)
    Classes.delete()