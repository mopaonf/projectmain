from models.course_class import CourseClass 

def get_all_course_class():
    return CourseClass.read()

def get_course_class_with_course_class_id(course_class_id):
    return CourseClass.read(course_class_id)

def save_course_class( num_hours, course_class_id=None):
    if course_class_id != None:
        course_class = get_course_class_with_course_class_id(course_class_id)
        course_class.num_hours = num_hours

    else:
        course_class = CourseClass(
            num_hours=num_hours
        )

    course_class.save()

def delete_course_class(course_class_id):
    course_class = get_course_class_with_course_class_id(course_class_id)
    course_class.delete()