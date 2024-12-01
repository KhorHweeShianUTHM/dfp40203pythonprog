# Python example program which explains usage
# of else block in exception handling of python programming.
try:
	x=float(input("Enter your number:"))
	result=100/x
	print(result)
except Exception as e: # when user enter character/division by 0 - it have many exception in one
	print("exception occured",e) # e = caught exception in python
else:
	print("else block is executing")