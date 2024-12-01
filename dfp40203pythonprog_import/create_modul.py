#modul_test.py file

import modul # call your module


c = input("Masukkan darjah celsius: ")
f = modul.celsius2F(float(c))
print("Fahrenheit adalah",f,"F")

#print(dir(modul)) #describe module
#print(dir(math)) #describe math module
