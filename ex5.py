import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='db3'
    )

cur= con.cursor()
s="SELECT * from book"

cur.execute(s)
result=cur.fetchall()

for rec in result:
    print(rec)
con.commit()

#cur.execute(db)
