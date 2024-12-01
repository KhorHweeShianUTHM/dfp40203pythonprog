def divide(x,y):
	try:
		print(f'{x}/{y} is {x / y}') 
	except ZeroDivisionError as e: # e = caught exception in python
		print(e)
	except TypeError:	
		print("Type error occured")
	except ValueError:
		print("Value error occured")

divide(12,2)
divide(10,0)
divide("e",4)