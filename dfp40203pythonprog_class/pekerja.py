class pekerja:
	def __init__(self,sal):
		self.sal = sal

	def overtime(self, OThours, RMhour):
		self.sal = self.sal + OThours * RMhour

pekerja1 = pekerja(1500)
print("Your salary is RM:",pekerja1.sal)
pekerja1.overtime(4,5.00)
print("Your salary + overtime is RM:",pekerja1.sal)