from flask import Blueprint, render_template, redirect, request, session, url_for, flash
import datetime
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
            session["password"] = record[2]
            return redirect(url_for("views.index"))
        else:
            flash("Incorrect Email or Password!")
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
    return render_template("profile.html", faculty=data)


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

    return render_template("faculty.html", faculty=data)


@views.route("/log")
def log():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log ORDER BY Datee DESC")
    data = cursor.fetchall()
    cursor.close()

    return render_template("log.html", log=data)


@views.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@views.route("/addfaculty")
def addfaculty():
    return render_template("addfaculty.html")


@views.route("/forgetpass", methods=["GET", "POST"])
def forgetpass():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        email1 = request.form["email"]
        secretkey1 = request.form["secretkey"]
        newpass = request.form["newpass"]
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM databasee.users WHERE Email= %s AND Secret_Key= %s",
            (email1, secretkey1),
        )
        record = cursor.fetchone()
        if record:
            session["loggedin"] = True
            session["email"] = record[1]
            session["secretkey"] = record[3]

            cursor1 = conn.cursor()
            cursor1.execute(
                "UPDATE users SET User_Pass=%s WHERE Email=%s", (newpass, email1)
            )
            conn.commit()
            cursor.close()
            conn.close()

            flash("Reset Successfully!")

            return redirect(url_for("views.login"))

        else:
            flash("Incorrect Secret Key!")
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
        flash("Successfully Added")
        return redirect(url_for("views.faculty"))

    return render_template("addfaculty.html")


@views.route("/camera")
def camera():
    return render_template("camera.html")


@views.route("/delete/<string:id_data>", methods=["GET"])
def delete(id_data):
    flash("Record has been Deleted")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM faculty WHERE ID= %s" % (id_data))
    conn.commit()
    return redirect(url_for("views.faculty"))


@views.route(
    "/update/<string:id_data>/<string:fname_data>/<string:lname_data>",
    methods=["GET", "POST"],
)
def update(id_data, fname_data, lname_data):
    return render_template(
        "updatefaculty.html", id=id_data, fname=fname_data, lname=lname_data
    )


@views.route("/updated/", methods=["GET", "POST"])
def updated():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        id1 = request.form["pota"]
        firstname = request.form["fname"]
        lastname = request.form["lname"]
        address = request.form["address"]
        birthday = request.form["birthday"]
        status = "Absent"
        Department = request.form["department"]
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE faculty SET First_name=%s, Last_name=%s, Address=%s, Birthday=%s, Status=%s, Department=%s WHERE ID=%s",
            (firstname, lastname, address, birthday, status, Department, id1),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Edit Successfully!")

        return redirect(url_for("views.faculty"))


@views.route("/UpdateProfile")
def UpdateProfile():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )

    return redirect(url_for("views.profile"))


@views.route("/admin")
def admin():
    return render_template("Admin.html")


@views.route("/adminchanged", methods=["GET", "POST"])
def adminchanged():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        currentpass = request.form["currentpass"]
        newpass = request.form["password"]
        confirmpass = request.form["confirmpass"]

        if newpass == confirmpass:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM databasee.users WHERE ID=%s AND User_Pass= %s",
                ("1", currentpass),
            )
            record = cursor.fetchone()
            if record:
                session["loggedin"] = True
                session["ID"] = record[0]
                session["User_Pass"] = record[2]

                cursor1 = conn.cursor()
                cursor1.execute(
                    "UPDATE users SET User_Pass=%s WHERE ID=%s", (newpass, "1")
                )
                conn.commit()
                cursor.close()
                conn.close()

                flash("Change Successfully!")
                return redirect(url_for("views.admin"))
            else:
                flash("Incorrect Password!")
        else:
            flash("Password not match!")

    return render_template("Admin.html")


@views.route("/schedule")
def schedule():
    return render_template("schedule.html")


@views.route("/attendanceprofile/<string:id_data>/<string:lname_data>")
def attendanceprofile(id_data, lname_data):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log WHERE ID=%s ORDER BY Datee DESC" % (id_data))
    data = cursor.fetchall()
    cursor.close()
    return render_template(
        "attendanceprofile.html",
        id=id_data,
        lname=lname_data,
        profilerecord=data,
    )


@views.route("/searchlog", methods=["GET", "POST"])
def searchlog():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        search_text = request.form["searched"]
        query = "SELECT * FROM log WHERE First_name LIKE '%{}%' OR Last_name LIKE '%{}%' OR ID LIKE '%{}%'".format(
            search_text, search_text, search_text
        )
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
    return render_template("searchlog.html", results=results)
