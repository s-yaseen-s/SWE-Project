from app import get_db

class Professor:
    def _init_(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  

    def view_all_registered_students(self):

        db = get_db()

        sql = """SELECT s.stID, s.sname
                 FROM Student s
                 JOIN Registered_In r ON s.stID = r.stuID
                 JOIN Course c        ON r.coID = c.cID
                 WHERE c.PrID = ? 
                 GROUP BY s.stID, s.sname
                 HAVING COUNT(c.cID) = (
                     SELECT COUNT(*) 
                     FROM Course 
                     WHERE PrID = ? 
                 );
              """

        rows = db.execute(sql,(self.pID, self.pID)).fetchall()

        students = [dict(row) for row in rows]

        return students
