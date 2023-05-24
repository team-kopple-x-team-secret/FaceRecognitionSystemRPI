from functools import wraps
from flask import Blueprint, render_template, redirect, request, session, url_for, flash
import datetime
import mysql.connector

views = Blueprint(__name__, "views")


def admin_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if "type" in session and session["type"] != "Admin":
            return redirect(
                url_for("views.login")
            )  # Redirect to the login page if not logged in
        return route_function(*args, **kwargs)

    return decorated_function


def login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(
                url_for("views.login")
            )  # Redirect to the login page if not logged in
        return route_function(*args, **kwargs)

    return decorated_function


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
            session["logged_in"] = True
            session["email"] = record[0]
            session["type"] = record[5]

            return redirect(
                url_for("views.index"),
            )
        else:
            flash("Incorrect Email or Password!")
    return render_template("login.html")


@views.route("/index/")
@login_required
def index():
    email = session.get("email")
    type = session.get("type")
    return render_template("index.html", email=email, type=type)


@views.route("/profile")
@admin_required
@login_required
def profile():
    email = session.get("email")
    type = session.get("type")
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
    return render_template("profile.html", faculty=data, email=email, type=type)


@views.route("/faculty")
@admin_required
@login_required
def faculty():
    email = session.get("email")
    type = session.get("type")
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

    return render_template("faculty.html", faculty=data, email=email, type=type)


@views.route("/log")
@admin_required
@login_required
def log():
    email = session.get("email")
    type = session.get("type")
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

    return render_template("log.html", log=data, email=email, type=type)


@views.route("/aboutus")
@login_required
def aboutus():
    email = session.get("email")
    type = session.get("type")
    return render_template("aboutus.html", type=type, email=email)


@views.route("/adduser")
@login_required
def adduser():
    return render_template("adduser.html")


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
@login_required
@admin_required
def insert():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )

    if request.method == "POST":
        email = request.form["email"]
        firstname = request.form["fname"]
        lastname = request.form["lname"]
        password = request.form["password"]
        Secretkey = request.form["secretkey"]

        cursor1 = conn.cursor()
        cursor1.execute("SELECT * FROM databasee.users WHERE Email = %s", (email,))
        record = cursor1.fetchone()
        if record:
            flash("Email Already Exist")
            return redirect(url_for("views.adduser"))
        else:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO databasee.users (Email,First_name,Last_name,User_Pass,Secret_Key,Type) Values (%s,%s,%s,%s,%s,%s)",
                (email, firstname, lastname, password, Secretkey, "Guard"),
            )
        conn.commit()
        flash("Successfully Added")
        return redirect(url_for("views.admin"))

    return render_template("adduser.html")


@views.route("/delete/<string:id_data>", methods=["GET"])
@login_required
@admin_required
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
@admin_required
@login_required
def update(id_data, fname_data, lname_data):
    email = session.get("email")
    type = session.get("type")
    return render_template(
        "updatefaculty.html",
        id=id_data,
        fname=fname_data,
        lname=lname_data,
        email=email,
        type=type,
    )


@views.route("/updated/", methods=["GET", "POST"])
@admin_required
@login_required
def updated():
    email = session.get("email")
    type = session.get("type")
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

        return redirect(url_for("views.faculty", email=email, type=type))


@views.route("/UpdateProfile")
@admin_required
@login_required
def UpdateProfile():
    email = session.get("email")
    type = session.get("type")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )

    return redirect(url_for("views.profile", type=type, email=email))


@views.route("/admin")
@admin_required
@login_required
def admin():
    email = session.get("email")
    type = session.get("type")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY Type ASC ")
    data = cursor.fetchall()
    cursor.close()

    return render_template("Admin.html", users=data, email=email, type=type)


@views.route("/changepasschanged", methods=["GET", "POST"])
@login_required
def changepasschanged():
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
        email = session.get("email")

        if newpass == confirmpass:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM databasee.users WHERE Email=%s AND User_Pass= %s",
                (email, currentpass),
            )
            record = cursor.fetchone()
            if record:
                cursor1 = conn.cursor()
                cursor1.execute(
                    "UPDATE users SET User_Pass=%s WHERE Email=%s", (newpass, email)
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


@views.route("/attendanceprofile/<string:id_data>/<string:lname_data>")
@admin_required
@login_required
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
@admin_required
@login_required
def searchlog():
    email = session.get("email")
    type = session.get("type")
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
    return render_template("searchlog.html", results=results, email=email, type=type)


@views.route("/searchfaculty", methods=["GET", "POST"])
@admin_required
@login_required
def searchfaculty():
    email = session.get("email")
    type = session.get("type")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        search_text = request.form["searched"]
        query = "SELECT * FROM faculty WHERE First_name LIKE '%{}%' OR Last_name LIKE '%{}%' OR ID LIKE '%{}%'".format(
            search_text, search_text, search_text
        )
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

    return render_template(
        "searchfaculty.html", results=results, email=email, type=type
    )


@views.route("/searchprofile", methods=["GET", "POST"])
@admin_required
@login_required
def searchprofile():
    email = session.get("email")
    type = session.get("type")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        password="1234",
        user="root",
        database="databasee",
    )
    if request.method == "POST":
        search_text = request.form["searched"]
        query = "SELECT * FROM faculty WHERE First_name LIKE '%{}%' OR Last_name LIKE '%{}%' OR ID LIKE '%{}%'".format(
            search_text, search_text, search_text
        )
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

    return render_template(
        "searchprofile.html", results=results, email=email, type=type
    )


@views.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("views.login"))


@views.route("/changepass")
def changepass():
    email = session.get("email")
    type = session.get("type")
    return render_template("changepass.html", email=email, type=type)


@views.route("/facultycheckin")
def facultycheckin():
    return render_template("facultycheckin")
