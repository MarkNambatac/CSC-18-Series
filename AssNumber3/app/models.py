from app import app, psql

class Users(object):
    def __init__(self, id_no=None, name=None, course=None):
        self.id_no = id_no
        self.name = name
        self.course = course

    def add(self):
        cursor = psql.connection.cursor()

        sql = "INSERT INTO students(id_no, name, course) \
                VALUES('%s','%s','%s')" % \
              (self.id_no, self.name, self.course)

        cursor.execute(sql)
        psql.connection.commit()

    def delete(self):
        cursor = psql.connection.cursor()
        sql = "DELETE FROM students WHERE id_no = '%s'" % (self.id_no)
        cursor.execute(sql)
        psql.connection.commit()

    def update(self):
        cursor = psql.connection.cursor()
        sql = "UPDATE students SET name = '%s', course = '%s' WHERE id_no = '%s'" % (self.name, self.course, self.id_no)
        cursor.execute(sql)
        psql.connection.commit()


    def search(self):
        cursor = psql.connection.cursor()
        sql = "SELECT * FROM students WHERE id_no = '%s'" % (self.id_no)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    @classmethod
    def all(cls):
        cursor = psql.connection.cursor()
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result



