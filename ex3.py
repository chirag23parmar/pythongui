import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='db3'
    )

cur= con.cursor()

db="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(db)

