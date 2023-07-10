import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

cur= con.cursor()
cur.execute("CREATE DATABASE db3")
