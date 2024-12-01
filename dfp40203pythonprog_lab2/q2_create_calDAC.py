#labex2 - Khor Hwee Shian 03DDT19F1118
#question2 - Build a program to compute the diameter, area and perimeter by using OOP Classes in Python programming. 
#			 The program must include - Instantiate the Class Circle
#										Function for diameter, area and perimeter formula calculation
# 										Your program must be using “math” standard module/library
#										Create object to use diameter, area and perimeter
#										Display the output

from q2_calDAC import Circle # from "q2_calDAC.py" import "Circle class"
import math #import math module

r = input("Please enter value of radius: ") #ask user to input radius
d = Circle.diameter(float(r)) #create an (diameter) object, change the value become a float data type
print("The diameter of Circle is",d) #display output

a = Circle.area(float(r)) #create an (area) object, change the value become a float data type
print("The area of Circle is",a) #display output

c = Circle.perimeter(float(r)) #create an (perimeter) object, change the value become a float data type
print("The Perimeter of Circle is",c) #display output