class InvalidRange(Exception):
	pass
try:
	marks=input("Enter the marks:")
	marks=int(marks)
	if(marks<0 or marks>100):
		raise InvalidRange
	print("Marks =", marks)

except ValueError: # if user insert except number
	print("Invalid Input")
except InvalidRange: # if user insert under 0 or exceed 100
	print("Invalid Range")