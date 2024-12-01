#Method overriding allows us to change the implementation of a function in the child class that is defined in the parent class.
class Car: #define class Car
	__name = "BMW" #class property

	def drive(self): #method drive
		print("I am driving") #body of method drive

	def __updateSoftware(self): #method __updateSoftware
		print("Updating Software") #body of method __updateSoftware

	def show(self): #method show
		return self.__updateSoftware() #call/return __updateSoftware method

redcar = Car() #redcar is object for class Car
redcar.drive() #call drive method of redcar 
print(redcar.show()) #print show method of redcar