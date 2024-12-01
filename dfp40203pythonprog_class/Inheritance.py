class Person: #person is parent class
	def __init__(self, fname, lname): #instance function
		self.firstname = fname
		self.lastname = lname

	def printname(self): #printname is method
		print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method
class Student(Person): # Child Student inheritance the Property of and method from Person
	pass

y = Student("Mike", "Olsen")#y is object for class Student
y.printname()

x = Person("John", "Doe") #x is object for class Person
x.printname()