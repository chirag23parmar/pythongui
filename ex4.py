import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='db3'
    )

cur= con.cursor()

s="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
#b1=(2,'Python_Update',800)
#cur.execute(s,b1)
books=[(2,'php',400),(3,'deep',200)]
cur.executemany(s,books)
con.commit()
#cur.execute(db)
