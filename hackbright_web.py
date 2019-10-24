"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/display_form")
def show_student_form():


    return render_template("add_new_student.html")


@app.route("/add_new_student", methods=["POST"])
def make_new_student():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    
    hackbright.make_new_student(first_name, last_name, github)
    
    return render_template("student_info.html", 
                            first_name=first_name,
                            last_name=last_name,
                            github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
