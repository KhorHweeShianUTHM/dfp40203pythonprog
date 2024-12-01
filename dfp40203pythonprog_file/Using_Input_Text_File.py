# file - file object
file  = open("hobby.txt","w")
for i in range(5):
	n = str(input("Enter hobby name:"))
	file.write("\n")
	file.write(n) # write is function() to write data into file
file.close()