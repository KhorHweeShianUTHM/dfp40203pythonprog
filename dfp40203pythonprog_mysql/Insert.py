# importing required library
import mysql.connector
# connecting to the database
dataBase = mysql.connector.connect(
 host = "localhost",
 user = "root",
 passwd = "root",
 database = "mydatabase" ) 
# preparing a cursor object
mycursor= dataBase.cursor()
sql = "INSERT INTO Student (Name, Roll) VALUES (%s, %s)"
val = [("Akash", "98"),
("Neel", "23"),
("Rohan", "43"),
("Amit", "87"),
("Anil", "45"),
("Megha", "55"),
("Sita", "95")]
mycursor.executemany(sql, val)
dataBase.commit()
print(mycursor.rowcount, "details inserted")
# disconnecting from server
dataBase.close()