from flask import Blueprint, render_template, redirect

views = Blueprint(__name__, "views")


@views.route("/")
def login():
    return render_template("login.html")

@views.route("/index")
def index():
    return render_template("index.html")