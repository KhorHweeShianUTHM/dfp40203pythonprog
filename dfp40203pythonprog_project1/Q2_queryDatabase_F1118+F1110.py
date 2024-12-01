# importing required library 
import mysql.connector
 
# connecting to the database 
dataBase = mysql.connector.connect(
 host = "localhost",
 user = "root",
 passwd = "root",
 database = "mydatabase" ) 
 
# preparing a cursor object 
cursorObject = dataBase.cursor() 
 
print("Displaying QUESTION1 from the FRIENDSHIP table:")
 
# selecting query
query = "SELECT NO, FIRSTNAME, LASTNAME, AGE, ADDRESS FROM FRIENDSHIP"
cursorObject.execute(query)
 
myresult = cursorObject.fetchall()
 
for x in myresult:
 print(x)
 
# disconnecting from server
dataBase.close()

