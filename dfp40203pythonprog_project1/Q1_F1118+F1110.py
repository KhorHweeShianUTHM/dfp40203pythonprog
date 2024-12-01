# Python program to create a table
   
from tkinter import *
  
  
class Table:
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(row):
            for j in range(column):
                  
                self.e = Entry(root, width=20, fg='black',
                               font=('Calibri',12,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, list[i][j])
  
# take the data
list = [(1,'Rohani','Abu Bakar',39,'Taman Tunku Sarina'),
       (2,'Noorazura','Mokhtar',38,'Taman Pulasan'),
       (3,'Thazliah','Thazalli',40,'Taman Tunku Sarina'),
       (4,'Nooraza','Othman',42,'Taman Tunku Maheran'),
       (5,'Mahani','Zakaria',40,'Kuaters Polimas'),
       (6,'JusroRizal','Jusoh',42,'Taman Bukit Tinggi'),
       (7,'Normiza','Tajudin',43,'Taman Bukit Tinggi'),
       (8,'Sarina','Sariff',48,'Taman Suria'),
       (9,'Amirah','Idris',33,'Taman Mahsuri'),
       (10,'Nordini','Ahmad',31,'Taman Aman')]
   
# find total number of rows and
# columns in list
row = len(list)
column = len(list[0])
   
# create root window
root = Tk()
t = Table(root)
root.mainloop()

