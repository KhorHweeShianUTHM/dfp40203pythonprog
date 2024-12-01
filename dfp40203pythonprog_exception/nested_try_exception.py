x = 10
y = 0

try:
	print("outer try block")
	try:
		print("nested try block")
		print(x / y)
	except TypeError as te: # te = caught exception in python
		print("nested except block")
		print(te)
except ZeroDivisionError as ze: # ze = caught exception in python
	print("outer except block")
	print(ze)