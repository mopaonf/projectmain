import sqlite3

class CourseClass: 
  TABLE_NAME = "course_class"

  def __init__(self, course_class_id=None, course_id=None, class_id=None, num_hours=None):
    self.course_class_id = course_class_id
    self.course_id = course_id
    self.class_id = class_id
    self.num_hours = num_hours

  def save(self):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()

      if self.course_class_id:
        query = f"UPDATE {self.TABLE_NAME} SET num_hours=?, course_id=?, class_id=? WHERE course_class_id=?"
        cursor.execute(query, (self.num_hours, self.course_id, self.class_id, self.course_class_id))
      else:
        query = f"INSERT INTO {self.TABLE_NAME} (course_id, class_id, num_hours) VALUES (?, ?, ?)"
        cursor.execute(query, (self.course_id, self.class_id, self.num_hours))

        course_class_id = cursor.execute(f"SELECT MAX(course_class_id) FROM {self.TABLE_NAME}").fetchone()[0]
        self.course_class_id = course_class_id

  def read(self):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()
      if self.course_class_id:
        query = f"SELECT course_class_id, course_id, class_id, num_hours FROM {self.TABLE_NAME} WHERE course_class_id=?"
        result = cursor.execute(query, (self.course_class_id,)).fetchone()

        course_class = CourseClass(course_class_id=result[0], course_id=result[1], class_id=result[2], num_hours=result[3])
        return course_class
      else:
        query = f"SELECT course_class_id, course_id, class_id, num_hours FROM {self.TABLE_NAME}"
        results = cursor.execute(query).fetchall()
        course_classes = []

        for result in results:
          course_class = CourseClass(course_class_id=result[0], course_id=result[1], class_id=result[2], num_hours=result[3])
          course_classes.append(course_class)

        return course_classes

  def delete(self):
    if self.course_class_id:
      with sqlite3.connect("db.sqlite3") as connection: 
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE course_class_id=?", (self.course_class_id,))