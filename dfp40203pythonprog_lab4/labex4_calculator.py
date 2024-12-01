# PYTHON LAB EXERCISE 4
# Name: KHOR HWEE SHIAN         
# Student ID: 03DDT19F1118     
# Class: DDT4D
# Activity: Write a program to create a simple calculator 

# Tkinter is a graphical user interface (GUI) module for Python
from tkinter import * # Tkinter Library in this program
import math # import math library in this program
from tkinter import messagebox # import messagebox in this program

class Calc(): # class declaration
	def __init__(self): # instance function
		self.total = 0 # (total value) variable declaration
		self.current = "" # (current value) variable declaration
		self.input_value = True # (input value) variable declaration 
		self.check_sum = False # (check sum) variable declaration 
		self.op = "" # (operation) variable declaration 
		self.result = False # (result) variable declaration 

	def numberEnter(self,num): # method numberEnter. num is properties
		self.result = False # result same with 'False'
		firstnum = txtDisplay.get() # get the first num
		secondnum = str(num) # get the second num 
		if self.input_value: # start of if...else Statement
			self.current = secondnum # if current value same with the second num
			self.input_value = False # if must be false
		else: # end of if...else Statement
			if secondnum == ".": # start of if...else Statement2, if second num is same with ".(dot)"
				if secondnum in firstnum: # if second num in content of first num
					return # return ans
			self.current = firstnum + secondnum # process of calculation
		self.display(self.current) # display output

	def sum_of_total(self): # method sum_of_total
		try:
			self.result = True # result same with 'True'
			self.current = float(self.current) # current value change to float data type
			if self.check_sum == True: # if check sum is correct
				self.valid_function() # call method
			else: # otherwise
				self.total = float(txtDisplay.get())
		except ValueError: # when user insert other word
			# message box name: ValueError, content: Check your values and operators.
			messagebox.showerror("ValueError", "Check your values and operators") # show error with message box

	def valid_function(self): # method valid_function
		try: # start of exception handling 
			if self.op == "add": # when it is add 
				self.total += self.current # process of addition calculation
			if self.op == "sub": # when it is subtract 
				self.total -= self.current # process of substraction calculation
			if self.op == "multi": # when it is multiple
				self.total *= self.current # process of multiplication calculation
			if self.op == "divide": # when it is divide
				self.total /= self.current # process of division calculation
			self.input_value = True # input value is True
			self.check_sum = False # check sum is False
			self.display(self.total) # display output
		except ZeroDivisionError: # when user divide by 0
			# message box name: ZeroDivisionError, content: We cannot divide by 0.
			messagebox.showerror("ZeroDivisionError", "We cannot divide by 0.") # show error with message box

	def operation(self,op): # method operation. op is properties
		self.current = float(self.current) # current value change to float data type
		if self.check_sum: # if check sum is correct
			self.valid_function() # call method
		elif not self.result: # if not result
			self.total = self.current # total equal with current
			self.input_value = True # input value is true
		self.check_sum = True # after all check sum is correct
		self.op = op # op = operation
		self.result = False # result is false

	def clear(self): # method clear, which is clear all number
		self.result = False # result is false
		self.current = "0" # the current is 0
		self.display(0) # display 0
		self.input_value = True # input value is correct
		self.total = 0 # total value is 0

	def display(self, value): # method display number
		txtDisplay.delete(0, END) # which is delete
		txtDisplay.insert(0, value) # which is insert

	def delete(self): # method delete, which is delete previous number
		numLen = len(txtDisplay.get()) # returns the number of elements
		txtDisplay.delete(numLen - 1, 'end') # delete one num
		if numLen == 1: # if the number length is 1
			txtDisplay.insert(0, "0") # display 0

	def opPM(self): # method opPM +/-
		try: # start of exception handling 
			self.result = False # result is false
			self.current = -(float(txtDisplay.get())) # put a '-(subtract)' in front number
			self.display(self.current) # display output
		except ValueError: # when user insert word
			# message box name: ValueError, content: Check your values and operators.
			messagebox.showerror("ValueError", "Check your values and operators") # show error with message box

	def squareRoot(self): # method squareRoot √
		try: # start of exception handling 
			self.result = False # result is false
			self.current = math.sqrt(float(txtDisplay.get())) # put a '-(subtract)' in front number
			self.display(self.current) # display output
		except ValueError: # when user insert word
			# message box name: ValueError, content: Check your values and operators.
			messagebox.showerror("ValueError", "Check your values and operators") # show error with message box

added_value = Calc() # added_value same to Calc() class

root = Tk() # Creates root master with the TK() constructor
root.title("Calculator") # root title name
root.config(bg="#b8f2ba") # root color

calc = Frame(root) # calc same with Frame(root)
calc.pack(padx=5, pady=5) # padding x,y=5

txtDisplay = Entry(calc, font=('arial',20,'bold'), bd=35, width=20, justify=RIGHT) # characteristics of txtDisplay 
txtDisplay.grid(row=0, column=0, columnspan=4) # place of txtDisplay
txtDisplay.insert(0, "0") # display 0

# ============================ ROW 1 ============================ #

 # characteristics of Clear button 
btnClear = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="C", bg="#b3b3b3", command=added_value.clear)
btnClear.grid(row=1, column=0) # place of Clear button 

 # characteristics of Square Root button 
btnSqRoot = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="√", bg="#b3b3b3", command=added_value.squareRoot)
btnSqRoot.grid(row=1, column=1) # place of Square Root button

 # characteristics of PM +/- button 
btnPM = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="±", bg="#b3b3b3", command=added_value.opPM)
btnPM.grid(row=1, column=2) # place of PM +/- button 

 # characteristics of delete button 
btnDel = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="DEL", bg="#b3b3b3", command=added_value.delete)
btnDel.grid(row=1, column=3) # place of delete button

# ============================ ROW 2 ============================ #

 # characteristics of button 1 
btn1 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="1", bg="#dcdcdc", command=lambda:added_value.numberEnter(1))
btn1.grid(row=2, column=0) # place of button 1

 # characteristics of button 2
btn2 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="2", bg="#dcdcdc", command=lambda:added_value.numberEnter(2))
btn2.grid(row=2, column=1) # place of button 2

 # characteristics of button 3
btn3 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="3", bg="#dcdcdc", command=lambda:added_value.numberEnter(3))
btn3.grid(row=2, column=2) # place of button 3

 # characteristics of addition button 
btnAdd = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="+", bg="#b3b3b3", command=lambda:added_value.operation("add"))
btnAdd.grid(row=2, column=3) # place of addition button 

# ============================ ROW 3 ============================ #

 # characteristics of button 4
btn4 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="4", bg="#dcdcdc", command=lambda:added_value.numberEnter(4))
btn4.grid(row=3, column=0) # place of button 4

 # characteristics of button 5
btn5 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="5", bg="#dcdcdc", command=lambda:added_value.numberEnter(5))
btn5.grid(row=3, column=1) # place of button 5

 # characteristics of button 6
btn6 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="6", bg="#dcdcdc", command=lambda:added_value.numberEnter(6))
btn6.grid(row=3, column=2) # place of button 6 

 # characteristics of subtraction button 
btnSub = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="-", bg="#b3b3b3", command=lambda:added_value.operation("sub"))
btnSub.grid(row=3, column=3) # place of subtraction button 

# ============================ ROW 4 ============================ #

 # characteristics of button 7
btn7 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="7", bg="#dcdcdc", command=lambda:added_value.numberEnter(7))
btn7.grid(row=4, column=0) # place of button 7

 # characteristics of button 8
btn8 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="8", bg="#dcdcdc", command=lambda:added_value.numberEnter(8))
btn8.grid(row=4, column=1) # place of button 8

 # characteristics of button 9
btn9 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="9", bg="#dcdcdc", command=lambda:added_value.numberEnter(9))
btn9.grid(row=4, column=2) # place of button 9 

 # characteristics of multiple button 
btnMulti = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="×", bg="#b3b3b3", command=lambda:added_value.operation("multi"))
btnMulti.grid(row=4, column=3) # place of multiple button 

# ============================ ROW 5 ============================ #

 # characteristics of button 0
btn0 = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="0", bg="#dcdcdc", command=lambda:added_value.numberEnter(0))
btn0.grid(row=5, column=0) # place of button 0

 # characteristics of dot button 
btnDot = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text=".", bg="#dcdcdc", command=lambda:added_value.numberEnter("."))
btnDot.grid(row=5, column=1) # place of dot button 

 # characteristics of equal button 
btnEqual = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="=", bg="#ffa500", command=added_value.sum_of_total)
btnEqual.grid(row=5, column=2) # place of equal button

 # characteristics of divide button
btnDiv = Button(calc, pady=1, bd=5, fg="black", font=('arial',20,'bold'), width=5, height=2, text="÷", bg="#b3b3b3", command=lambda:added_value.operation("divide"))
btnDiv.grid(row=5, column=3) # place of divide button

root.mainloop() # main event loop