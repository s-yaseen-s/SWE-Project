# Course Registration System

A Flask-based course registration system created for the CSAI 203 Introduction to Software Engineering course. It provides separate workflows for students, professors, and administrators, backed by SQLite.

## Roles and workflows

- **Students:** sign in, view course-related pages, register for or drop courses, and view grades
- **Professors:** sign in, view assigned courses, and manage course grading workflows
- **Administrators:** manage users and course/professor assignments

The repository also includes course design, progress, and requirements documents under `docs/`.

## Technology

- Python 3
- Flask
- Flask-Login
- SQLite
- pytest and pytest-flask for tests

## Setup

```bash
git clone https://github.com/s-yaseen-s/SWE-Project.git
cd SWE-Project
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m srs.app
```

The application entry point is `srs/app.py`. It includes an `/init` route that initializes the database from the SQL files; review the project configuration and database contents before using this route. The checked-in SQLite database is included in the repository.

## Run tests

```bash
pytest
```

The GitHub Actions workflow in `.github/workflows/python-tests.yml` runs the Python tests.

## Project layout

- `srs/app.py` — Flask application and role-based routes
- `srs/controllers/` — administrator, professor, and student route groups
- `srs/models/` — role models
- `srs/repositories/` — database access helpers
- `srs/database/schema.sql` — database schema
- `srs/database/data.sql` — initial data
- `srs/templates/` — HTML pages
- `srs/static/style.css` — application styles
- `tests/` — pytest test suite
- `docs/` — course design, progress, and requirements PDFs

## Security note

This is a course project, not a production-ready student information system. Review authentication, secret management, authorization, and database setup before deploying or entering real student data.

## License

No license file was present when this README was written. Contact the repository owner before reusing the project.
