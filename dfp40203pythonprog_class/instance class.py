#Define instance methods
class Car:
	def __init__(self, make, model, price, inventory): #__init__instance
		self.make = make
		self.model = model
		self.price = price
		self.inventory = inventory
	def sellCar(self, quantity): # insert function sellCar & print in object car1 and car2
		self.inventory = self.inventory - quantity

car1 = Car("Chevy", "Volt", 15000.00, 10)#car1=object, argument to Car
print(car1.make, car1.model, car1.price, car1.inventory)
car2 = Car("Ford", "Focus", 10000.00, 5)
print(car2.make, car2.model, car2.price, car2.inventory)
print(car1.sellCar(4))
print(car1.inventory)
print(car2.sellCar(4))
print(car2.inventory)