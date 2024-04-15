from models.course import Course

def get_all_courses():
    course = Course.read()

    return [ course.toJSON() for course in course ]

def get_course_with_course_id(course_id):
    return Course.read(course_id).toJSON()

def save_course(course_name, course_id=None):
    if course_id != None:
        # get course with id
        course = get_course_with_course_id(course_id)
        course.course_name = course_name
 
    else:
        course = Course(course_name=course_name)
    
    course.save()

    return course.toJSON()

def delete_course(course_id):
    course = get_course_with_course_id(course_id)
    course.delete()

    return course.toJSON()
