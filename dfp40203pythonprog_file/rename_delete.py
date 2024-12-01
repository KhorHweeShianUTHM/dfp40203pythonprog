# os is Python Modules in the Standard Library
# os use to allows you to access OS-level functionality, including the file system.
import os
file_object = open("text.txt","wb") # opens a file for writing only in binary format
file_object.close()

#rename
#os.rename("text.txt","rename.txt") # exist file text.txt, rename to rename.txt

file_object.close() #close file

#Delete file
os.remove("rename.txt")