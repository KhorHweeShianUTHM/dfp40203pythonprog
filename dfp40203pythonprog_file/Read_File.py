# Open/close File
# Python Modulw os = Allows you to access 0S-level functinality, including the file system.

file = open("Balik_Kampung.txt", "r+") # arithmatic_function.py = file name
# print(file.read()) # read all file
# print(file.read(10)) # read the first 10 character
# print(file.readline()) # read a line
print(file.readlines()) # read all with line

# for x in file: # loop throught file line by line
# print(x)

file.close() # close file