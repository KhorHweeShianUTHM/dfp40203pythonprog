from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("My First Program") # name of program
top.geometry("100x100") # adjust size of program
def hello(): 
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello) # button name + when click button name
B1.place(x = 35,y = 50) 

top.mainloop() # end of program
