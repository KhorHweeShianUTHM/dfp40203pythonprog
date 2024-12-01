# os is Python Modules in the Standard Library
# os use to allows you to access OS-level functionality, including the file system.

import os
#create directory
os.mkdir("newDirectory") # create directory name newDirectory
print(os.getcwd()) # displays the current working directory

#change the current directory
#path="C:\\Users\\TOSHIBA\\Desktop\\scl"
#os.chdir(path)
#print(os.getcwd()) # display the current working directory

#deletes the directory, which is passed as an argument in the method
#only can delete emply file
#os.rmdir("newDirectory")