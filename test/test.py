import mysql.connector
from datetime import datetime


conn = mysql.connector.connect(
    host="127.0.0.1", port="3306", password="1234", user="root", database="databasee"
)

if conn.is_connected():
    print("Connected TO DATABASE")
else:
    print("Not CONNECTED")


cursor = conn.cursor()
query = 'SELECT * FROM faculty'
cursor.execute(query)
result = cursor.fetchall()
