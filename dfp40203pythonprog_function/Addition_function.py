jum=0 #global variable
def sum(nom1,nom2): #declare function sum with 2 parameters
	print("Addition 2 numbers and return the value")
	jum=nom1+nom2 #jum is local variable
	print("In function ",nom1," + ",nom2," local total",jum)
	return jum
	
sum(15,25) #call function
print("Out of function, global total",jum)
