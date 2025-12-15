from flask import Flask, render_template, session, request, flash, redirect, Blueprint
from models.student import Student
import sqlite3

student_bp = Blueprint('student', __name__)

@student_bp.route('/view_grades')
def view_grades():
    student_id = session.get('userID')
    if not student_id:
        return "Not logged in"
    student = Student(student_id, "", "")   
    sgrades = student.get_grades()
    return render_template('view_grades.html', grades=sgrades)

@student_bp.route('/course_reg')
def course_reg():

    return render_template("register_course.html")

@student_bp.route('/register_course', methods=['POST'])
def register_course():

    course_id = request.form.get("course_id")
    student_id = session["userID"]

    student = Student(student_id, "", "")
    try:
        student.RegisterCourse(course_id)
        return f"""
            <p>You have registered for course: {course_id}</p>
            <a href='/StudentHome'>Click here to go back to Student Home</a>
        """
    except sqlite3.IntegrityError:
        return f"""
            <h1>Error</h1>
            <p>You are already registered for this course.</p>
        """
    except Exception as e:
        return f"""
            <h1>Error</h1>
            <p>{str(e)}</p>
            <a href='/StudentHome'>Click here to go back</a>
        """