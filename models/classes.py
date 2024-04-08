import sqlite3

class Classes: 
  TABLE_NAME = "classes"

  def __init__(self, class_id=None, class_name=None):
      self.class_id = class_id 
      self.class_name = class_name
    

  def save(self):

    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()

      if self.class_id:
        query = f"UPDATE {self.TABLE_NAME} set class_name = ? WHERE class_id = ?"
        cursor.execute (query, (self.class_name, self.class_id))
      else:
         
          query = f"INSERT INTO {self.__class__.TABLE_NAME} (class_name) VALUES(?)"

          cursor.execute(query, (self.class_name))
      pass

  def read(self,class_id=None):
    with sqlite3.connect("db.sqlite") as connection:
      cursor = connection.cursor()
      if class_id:
        query = f"SELECT (class_id, class_name) FROM {self.__class__.TABLE_NAME} WHERE class_id = ?"

        result = cursor.execute(query, (id)).fetchone()

        classes = Classes(class_namename=result[1])
        classes.id = result[0]

        return classes
      else:
        query = f"SELECT (class_id, class_name) FROM {self.__class__.TABLE_NAME}"

        results = cursor.execute(query).fetchall
        classess = []
        
        for resut in results:
          classes = Classes(class_name=result[1])
          classes.class_id = result[0]

          classess.append(classes)

        return classess
    pass 

  def delete(self):
    if self.class_id:
      with sqlite3.connect("db.sqlite") as connection: 
        cursor= connection.cursor()

        cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE class_id = ?", {self.class_id, }) 
    pass 

