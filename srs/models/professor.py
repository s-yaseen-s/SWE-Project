from app import get_db

class Professor:
    def __init__(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  

  def view_all_registered_students(self, course_id: str):
        db = get_db()

        rows = db.execute(
            """SELECT s.stID, s.sname, r.grade
             FROM Registered_In AS r
             JOIN Student      AS s ON r.stuID = s.stID
             JOIN Course       AS c ON r.coID = c.cID
            WHERE c.cID = ? AND c.PrID = ?;
            """ ,
            (course_id, self.pID),
        ).fetchall()

        students = [dict(row) for row in rows]

        return students
