from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/view_grades')
def view_grades():
    sgrades = [
        {'course': 'Mathematics', 'grade': 'A'},
        {'course': 'Science', 'grade': 'B+'},
        {'course': 'History', 'grade': 'A-'}
    ]
    return render_template('view_grades.html', grades=sgrades)

if __name__ == '__main__':
    app.run(debug=True)