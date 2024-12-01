# Python program to connect
# to mysql databse
 
import mysql.connector
 
# Connecting from the server
conn = mysql.connector.connect (host= 'localhost', username='root', password='root')
 
print(conn)
 
# Disconnecting from the server
conn.close()
