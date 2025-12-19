from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo
from srs.db import get_db

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
@login_required
def get_students_in_course(c_id):
    prof = current_user
    db = get_db()
    students = professorRepo(db, prof.pID).get_students_in_course(c_id)
    return render_template(
        "view_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )

@professor_bp.route("/grade")
@login_required
def grade_page():
    return render_template("Grade.html")

@professor_bp.route("/assign-grade", methods=["POST"])
@login_required
def assign_grade():
    professor_id = current_user.pID
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    if not student_id or not course_id or not grade:
        return "Missing required fields"
    
    db = get_db()
    repo = professorRepo(db, professor_id)
    result = repo.assign_grade(student_id, course_id, grade)

    return result

@professor_bp.route("/")
@login_required
def view_courses():
    professor_id = current_user.pID
    db = get_db()
    courses = professorRepo(db, professor_id).get_courses()

    return render_template("ProfessorHome.html", courses=courses)
