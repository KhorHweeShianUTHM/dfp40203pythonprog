from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Fill name") # name of program
top.geometry("300x250") # adjust size of program
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

top.mainloop()
