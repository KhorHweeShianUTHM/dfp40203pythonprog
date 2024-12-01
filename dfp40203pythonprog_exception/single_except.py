def divide(x,y):
	try:
		print(f'{x}/{y} is {x / y}') 
	except (ZeroDivisionError,TypeError,ValueError) as e: # e = caught exception in python
		print(e)

divide(5,2)
divide("a",2)