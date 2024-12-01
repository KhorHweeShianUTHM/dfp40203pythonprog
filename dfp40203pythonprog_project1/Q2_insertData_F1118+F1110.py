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
sql = "INSERT INTO FRIENDSHIP (NO, FIRSTNAME, LASTNAME, AGE, ADDRESS) VALUES (%s, %s, %s, %s, %s)"
val = [(1,'Rohani','Abu Bakar',39,'Taman Tunku Sarina'),
       (2,'Noorazura','Mokhtar',38,'Taman Pulasan'),
       (3,'Thazliah','Thazalli',40,'Taman Tunku Sarina'),
       (4,'Nooraza','Othman',42,'Taman Tunku Maheran'),
       (5,'Mahani','Zakaria',40,'Kuaters Polimas'),
       (6,'JusroRizal','Jusoh',42,'Taman Bukit Tinggi'),
       (7,'Normiza','Tajudin',43,'Taman Bukit Tinggi'),
       (8,'Sarina','Sariff',48,'Taman Suria'),
       (9,'Amirah','Idris',33,'Taman Mahsuri'),
       (10,'Nordini','Ahmad',31,'Taman Aman')]
mycursor.executemany(sql, val)
dataBase.commit()
print(mycursor.rowcount, "details inserted")
# disconnecting from server
dataBase.close()