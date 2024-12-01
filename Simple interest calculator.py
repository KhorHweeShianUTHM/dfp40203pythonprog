from tkinter import *

root=Tk()
root.title("Simple interest calculator")
root.geometry("500x300")

def Calculate():
	p=int(principal_entry.get())
	r=int(rate_entry.get())
	t=int(time_entry.get())
	amount=(p*r*t)/100
	amount=Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)

principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="Rate of interest:",font="arial 15")
time=Label(root,text="Time:",font="arial 15")

principal.place(x=50,y=20)
rate.place(x=5,y=90)
time.place(x=50,y=160)

interest=Label(root,text="Interest:",font="arial 15")
interest.place(x=50,y=230)

principal_value=StringVar()
rate_value=StringVar()
time_value=StringVar()

principal_entry=Entry(root,textvariable=principal_value,font="arial 20",width=8)
rate_entry=Entry(root,textvariable=rate_value,font="arial 20",width=8)
time_entry=Entry(root,textvariable=time_value,font="arial 20",width=8)

principal_entry.place(x=200,y=20)
rate_entry.place(x=200,y=90)
time_entry.place(x=200,y=160)

Button(text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)


root.mainloop()