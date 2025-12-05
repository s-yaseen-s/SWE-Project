from app import get_db
class Professor:
    def _init_(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  

    def get_students_in_course(self, course_id: str):
          db = get_db()

        sql = """SELECT s.stID, s.sname, r.grade
                 FROM Student s
                 JOIN Registered_In r ON s.stID = r.stuID
                 JOIN Course c        ON r.coID = c.cID
                 WHERE c.cID = ? AND c.PrID = ?;
              """

        rows = db.execute(sql, (course_id, self.pID)).fetchall()

        students = [dict(row) for row in rows]

        return students
