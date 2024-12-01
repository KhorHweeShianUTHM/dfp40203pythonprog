def divide(x,y):
	try:
		print(f'{x}/{y} is {x / y}') # {} = barren dictionary in python
	except ZeroDivisionError as e: # e = caught exception in python
		print(e)

divide(10,2)
divide(10,0)
divide(10,4)