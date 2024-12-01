from tkinter import *

root = Tk()
root.title("Word") # name of program
root.geometry("200x100") # adjust size of program

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
	  # Message
	  
var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
