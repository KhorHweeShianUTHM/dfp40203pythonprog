def getACharacter2(str1):
	x =0
	for i in str1:
		if i == "k":
			x += 1
	if x == 0:
		print("tiada")
	return x


str1 = input("Insert your politeknik : ")
print("number of charactor 'k' is ", getACharacter2(str1))