f = open("WriteContent.txt","w+") #open file object f
for i in range(10):
	f.write("This is line \n") # write into file Write Content
f.close()