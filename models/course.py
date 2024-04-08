import sqlite3
import json

class Course: 
  TABLE_NAME = "course"

  def __init__(self, course_id=None, course_name=None):
    self.course_id = course_id 
    self.course_name = course_name

  def save(self):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()

      if self.course_id:
          query = f"UPDATE {self.TABLE_NAME} SET course_name = ? WHERE course_id = ?"
          cursor.execute(query, (self.course_name, self.course_id))
      else:
          query = f"INSERT INTO {self.__class__.TABLE_NAME} (course_name) VALUES(?)"
          cursor.execute(query, (self.course_name,))

  def read(self, ):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()
      if self.course_id:
        query = f"SELECT course_id, course_name FROM {self.__class__.TABLE_NAME} WHERE course_id = ?"
        result = cursor.execute(query, (self.course_id,)).fetchone()

        course = Course(course_name=result[1])
        course.course_id = result[0]

        return course
      else:
        query = f"SELECT course_id, course_name FROM {self.__class__.TABLE_NAME}"
        results = cursor.execute(query).fetchall()
        courses = []

        for result in results:
          course = Course(course_name=result[1])
          course.course_id = result[0]
          courses.append(course)

        return courses

  def delete(self):
    if self.course_id:
      with sqlite3.connect("db.sqlite3") as connection: 
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE course_id = ?", (self.course_id,))
        
  def toJSON(self):
        return {
            "course_name": self.course_name,
            "course_id": self.course_id
        }