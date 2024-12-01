str1="Politeknik Sultan Abdul Halim Muadzam Shah"
# Code 1: 
c = str1[3] #character yg ke3(0=P,1=o,2=l,3=i)
print ("Char 3:", c )

# Code 2: 
r = str1 [0:10] #character dari 0-10
print ("Char 0 - 10:",r )

# Code 3: 
rn = str1 [-11: -1] #kira from belakang
print ("String negatif:",rn )

# Code 4: 
length = len(str1) #jumlah aksara
print("Jumlah aksara :", length)

# Code 5: 
strlower = str1.lower() #lowercase
print(strlower)

# Code 6: 
strupper = str1.upper() #uppercase
print(strupper)

# Code 7: 
strrep = str1.replace("Politeknik", "Kolej")#tukar perkataan
print(strrep)

# Code 8: 
perkataan = str1.split(" ")#pisahkan perkataan
print(perkataan[0])
print(perkataan[1])
print(perkataan[2])
print(perkataan[3])
print(perkataan[4])
print(perkataan[5])
print(perkataan)

# Code 9: 
#check string
check= "Poli" in str1 #semak perkataan poli
if check:
	print("Ada")
else:
	print("Tidak")

# Code 10: 
str2 = ", Kedah" #combine
print(str1 + str2)

# Code 11: 
firstname = "John"
lastname = "Malibu"
age = 35
info = "{} {} is {} years old"
print(info.format(firstname, lastname, age))

# Code 12: 
name = "Mike" # string declacre
print ("Nickname: ", name)
fname, lname = "Mike", "Gilmore" #declare firstname and lastname
print ("Full name is: ", fname, lname)#concatinate 2 string


























