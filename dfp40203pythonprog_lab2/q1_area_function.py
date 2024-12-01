#labex2 - Khor Hwee Shian 03DDT19F1118
#question1 - Build a program to compute area of triangle and square. 
#			 The program must include - Function of menu
#										Function of triangle and square formula calculation
#										Display output

def Triangle(): #declare function Triangle
	print()
	print("\t\t--Area of Triangle--")
	print()
	b=int(input("\t\tPlease value of base:")) #ask user input(base)
	h=int(input("\t\tPlease value of height:")) #ask user input(height)
	areaTri=0.5*b*h #formula calculation of area tringle
	print()
	print("\t\tThe area of triangle are:",areaTri) #dispaly output with the answer
	print()

def Square(): #declare function Square
	print()
	print("\t\t--Area of Square--")
	print()
	a=int(input("\t\tPlease enter value of side:")) #ask user input(side)
	areaSqur=a*a #formula calculation of area Square
	print()
	print("\t\tThe area of Square are:",areaSqur) #dispaly output with the answer
	print()

repeat=True
while(repeat):
	print('''
		=====================
		 CALCULATION OF AREA 
		=====================''')
	print('''
		1.Area of Triangle
		2.Area of Square''')
	print()
	activity=int(input("\t\tPlease enter the activity: ")) #ask user input(activity)
	if activity==1:
		Triangle() #call function Triangle
	elif activity==2:
		Square() #call function Square
		repeat=False
		exit #stop the program
	else:
		print("The number that u've entered is not in the list.")
		print()