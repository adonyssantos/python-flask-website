from flask import render_template
from app import app
from app.courses_list import courses_list


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/courses")
def courses():
    return render_template("courses_list.html", courses_list=courses_list)


@app.route("/courses/<id>")
def course(id):
    for course in courses_list:
        if course["id"] == id:
            return render_template("course_details.html", course=course)
    return render_template("404.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
