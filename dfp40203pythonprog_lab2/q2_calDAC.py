#labex2 - Khor Hwee Shian 03DDT19F1118
#question2 - Build a program to compute the diameter, area and perimeter by using OOP Classes in Python programming. 
#			 The program must include - Instantiate the Class Circle
#										Function for diameter, area and perimeter formula calculation
# 										Your program must be using “math” standard module/library
#										Create object to use diameter, area and perimeter
#										Display the output

class Circle: #define class Circle
	def diameter(d): #method diameter
		r=2*d #formula calculation of diameter circle
		return r 

	def area(a): #method area
		r=3.142*a*a #formula calculation of area circle
		return r

	def perimeter(c): #method perimeter
		r=2*3.142*c #formula calculation of perimeter circle
		return r