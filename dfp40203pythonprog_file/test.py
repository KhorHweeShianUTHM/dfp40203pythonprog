def Add():#declare function Addition
	print("\t\t--Addition two numbers--")
	print()
	nom1=int(input("\t\tEnter first number:"))
	nom2=int(input("\t\tEnter second number:"))
	total_add=nom1+nom2
	print("\t\tTotal Addition two numbers are:",total_add)
	print()

def Sub():#declare function Subtraction
	print("\t\t--Subtraction two numbers--")
	print()
	nom1=int(input("\t\tEnter first number:"))
	nom2=int(input("\t\tEnter second number:"))
	total_sub=nom1-nom2
	print("\t\tTotal Subtraction two numbers are:",total_sub)
	print()

def Multi():#declare function Multiplication
	print("\t\t--Multiplication two numbers--")
	print()
	nom1=int(input("\t\tEnter first number:"))
	nom2=int(input("\t\tEnter second number:"))
	total_multi=nom1*nom2
	print("\t\tTotal Multiplication two numbers are:",total_multi)
	print()

def Divide():#declare function Divide
	print("\t\t--Divide two numbers--")
	print()
	nom1=int(input("\t\tEnter first number:"))
	nom2=int(input("\t\tEnter second number:"))
	total_divide=nom1/nom2
	print("\t\tTotal Divide two numbers are:",total_divide)
	print()

repeat=True
while(repeat):
	print('''
		******************************
		MENU OF ARITHMATIC CALCULATION
		******************************''')
	print('''
		1.Addition two numbers
		2.Subtraction two numbers
		3.Multiplication two numbers
		4.Divide two numbers
		5.Exit program''')
	print()
	choose=int(input("\t\tEnter your choice:"))
	if choose==1:
		Add()
	elif choose==2:
		Sub()
	elif choose==3:
		Multi()
	elif choose==4:
		Divide()
	elif choose==5:
		repeat=False
		exit
	else:
		print("\t\tChoice is not in the MENU")
		print()