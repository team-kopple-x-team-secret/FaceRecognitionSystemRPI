from flask import Flask, session
from views import views
import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1", port="3306", password="1974", user="root", database="databasee"
)
if conn.is_connected():
    print("Connected TO DATABASE")
else:
    print("Not CONNECTED")

app = Flask(__name__)
app.secret_key = "sssswhhhaz"

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
    
