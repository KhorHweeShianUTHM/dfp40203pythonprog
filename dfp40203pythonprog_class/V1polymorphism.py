#Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
class dog: #define class dog
	def sound(self): #method sound(same name)
		print("bow bow") #body of method sound

class cat: #define class cat
	def sound(self): #method sound(same name)
		print("meow") #body of method sound

def makesound(animaltype): #method makesound
	animaltype.sound() #call method which is "bow bow" or "meow"

catobj = cat() #catobj is object for class cat
dogobj = dog() #dogobj is object for class dog
makesound(catobj) #call makesound method of catobj 
makesound(dogobj) #call makesound method of dogobj 