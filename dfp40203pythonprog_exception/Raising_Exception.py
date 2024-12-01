class ValidationError(Exception):
	pass


def divide(x, y):
	try:
		if type(x) is not int: # jika x bukan integer
			raise TypeError("Unsupported type") # raise = naikkan
		if type(y) is not int: # jika y bukan integer
			raise TypeError("Unsupported type")
	except TypeError as e: # kecuali ralatjenis
		print(e)
		raise ValidationError("Invalid type of arguments")

	if y == 0:
		raise ValidationError("We can't divide by 0.")

try:
	divide(10,0)
except ValidationError as ve:
	print(ve)

try:
	divide(10,"5") # "5" = string word
except ValidationError as ve:
	print(ve)