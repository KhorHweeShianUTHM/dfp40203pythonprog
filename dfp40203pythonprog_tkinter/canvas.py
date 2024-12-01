from tkinter import *
from tkinter import messagebox

top = Tk() 
top.title("My Canvas") # name of program
top.geometry("300x250") # adjust size of program
C = Canvas(top, bg="blue", height=250, width=300) 
coord = 10, 50, 240, 210 
arc = C.create_arc(coord, start=0, extent=150, fill="red") 
C.pack() # call the pack
top.mainloop() # end of program