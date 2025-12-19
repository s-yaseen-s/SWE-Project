from flask import Blueprint, render_template, session, request
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo
from srs.db import get_db

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
def get_students_in_course(c_id):
    p_id = session["userID"]
    p_name = session.get("pname", "")
    prof = Professor(pID=p_id, pname=p_name, password="")
    db = get_db()
    students = professorRepo(db, p_id).get_students_in_course(c_id)
    return render_template(
        "professor_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )

@professor_bp.route("/grade")
def grade_page():
    return render_template("Grade.html")

@professor_bp.route("/assign-grade", methods=["POST"])
def assign_grade():
    professor_id = session.get('userID')
    if not professor_id:
        return "Not logged in"
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    if not student_id or not course_id or not grade:
        return "Missing required fields"
    
    db = get_db()
    repo = professorRepo(db, professor_id)
    result = repo.assign_grade(student_id, course_id, grade)

    return result
