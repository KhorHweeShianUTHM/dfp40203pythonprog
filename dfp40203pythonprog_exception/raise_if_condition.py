x = int(input("Enter a number:"))

if x < 0: # jika x kurang dari 0
	raise Exception("Sorry, no numbers below zero")
else:
	print("It positive number")