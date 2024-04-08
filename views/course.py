from flask import Blueprint, request, Response

from controllers.course import *
from models.exceptions import ModelNotFoundError

course_view = Blueprint('course', __name__, url_prefix='/course')

@course_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_courses()
    else:
        submitted_data = request.POST

        return Response(save_course(submitted_data['course_name']), status=201)

@course_view.route('/<course_id>', methods=['GET', 'POST', 'DELETE'])
def get_or_update_instance(course_id):
    if request.method == 'GET':
        try:
            return get_course_with_course_id(course_id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.PATCH
        return Response(save_course(name=data['course_name']), status=201)
    elif request.method == 'DELETE':
        return Response(delete_course(course_id), status=201)