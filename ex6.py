import mysql.connector
mydb=mysql.connector.connect(
        host='localhost',
        user='root'
        password='',
        database='db3'
        )
cur=mydb.cursor()
s="SELECT * from book"
cur.execute(s)
result=cur.fetchall()

for rec in result:
        print(rec)

        
