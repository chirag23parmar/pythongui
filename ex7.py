import mysql.connector
mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db3'
        )
cur=mydb.cursor()
s="UPDATE book SET price=price+10 WHERE price>200"

cur.execute(s)
mydb.commit()
