name_prefix ="Madam" #global variable
def info(name,age,fav_color): # name&fav_color is string, age is integer
	print("Your name is ",name)
	print("Your age is  ",age)
	print("Your favorite color is ",fav_color)
	return name_prefix + " " + name

print(info("Azura",20,"blue"))