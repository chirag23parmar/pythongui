import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="")
print(con.connection_id)
