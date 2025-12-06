from db import get_db

class Student:
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password

    def RegisterCourse(self, course_id):
        
        db = get_db()

        valid_course = db.execute("SELECT cID FROM Course WHERE cID = ?", (course_id,)).fetchone()
        
        if valid_course is None:
            raise Exception("The selected Course does not exist.")

        db.execute("""
                INSERT INTO Registered_In VALUES(?, ?, NULL)
                """, (self.sID, course_id))
        db.commit()