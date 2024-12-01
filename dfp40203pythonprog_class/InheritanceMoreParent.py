class A: #define superclass A
	def methodA(self): #method A
		print("A class")
class B: #define superclass B
	def methodB(self):
		print("B class")
class C: #define superclass C
	def methodC(self):
		print("C class")
class D(A, B, C): #define subclass D
	def methodD(self):
		print("D class")
d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()