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
# creating table 
lecturerRecord = """CREATE TABLE FRIENDSHIP (
 NO INT,
 FIRSTNAME VARCHAR(50) NOT NULL,
 LASTNAME VARCHAR(50) NOT NULL,
 AGE INT NOT NULL,
 ADDRESS VARCHAR(20) NOT NULL
 )"""
# table created
cursorObject.execute(lecturerRecord) 
# disconnecting from server
dataBase.close()