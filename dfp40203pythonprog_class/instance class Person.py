class Person:
	def __init__(self, name, age): #__inti__ instance function. name and age is par
		self.name = name #properties
		self.age = age #properties	

p1 = Person("John", 36)#p1 is object in class Person

print(p1.name)
print(p1.age)

p1.age = 40 #modify properties on objects

print(p1.name)
print(p1.age)

del p1

#print(p1) 
#NameError: name 'p1' is not defined sbb dah del ms line 16