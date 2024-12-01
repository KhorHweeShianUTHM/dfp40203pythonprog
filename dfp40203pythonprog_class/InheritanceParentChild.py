class Parent: #define superclass/parent
	def show(self): #method show
		print("Parent method")
class Child(Parent): #define subclass/child
	def display(self): #method display
		print("Child method")
c = Child() #create an object
c.display() #call function display() method
c.show() #call function show() method