from flask import Blueprint, render_template, redirect, request, session, url_for
import mysql.connector

views = Blueprint(__name__, "views")


@views.route("/", methods=["GET", "POST"])
def login():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM databasee.users WHERE Email= %s AND User_Pass= %s",
            (email, password),
        )
        record = cursor.fetchone()
        if record:
            session["loggedin"] = True
            session["email"] = record[1]
            session["password"] = record[4]
            return redirect(url_for("views.index"))
        else:
            print("Incorrect Info")
    return render_template("login.html")


@views.route("/index")
def index():
    return render_template("index.html")


@views.route("/profile")
def profile():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faculty")
    data = cursor.fetchall()
    cursor.close()
    return render_template("profile.html", faculty = data)


@views.route("/faculty")
def faculty():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faculty")
    data = cursor.fetchall()
    cursor.close()

    return render_template("faculty.html", faculty = data)


@views.route("/log")
def log():
    return render_template("log.html")


@views.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@views.route("/addfaculty")
def addfaculty():
    return render_template("addfaculty.html")


@views.route("/forgetpass")
def forgetpass():
    return render_template("forgetpass.html")


@views.route("/insert", methods=["GET", "POST"])
def insert():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        firstname = request.form["fname"]
        lastname = request.form["lname"]
        address = request.form["address"]
        birthday = request.form["birthday"]
        status = "Absent"
        Department = request.form["department"]
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO faculty (First_name,Last_name,Address,Birthday,Status,Department) Values (%s,%s,%s,%s,%s,%s)",
            (firstname, lastname, address, birthday, status, Department),
        )
        conn.commit()
        return redirect(url_for("views.faculty"))

    return render_template("addfaculty.html")
