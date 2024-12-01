#Ini adalah main kepada keseluruhan program Calculate ini.
#Run program ini untuk mendapatkan output anda.
import calculate_function #name of your file
import menu #name of your file
repeat=True

while (repeat):
	print(menu.menu)
	print("")
	choose=int(input("\t\tEnter your choice:"))
	if choose==1:
		calculate_function.Add()# call function Add() from import file
	elif choose==2:
		calculate_function.Sub()# call function Sub() from import file
	elif choose==3:
		calculate_function.Multi()# call function Multi() from import file
	elif choose==4:
		calculate_function.Divide()# call function Divide() from import file
	elif choose==5:
		repeat=False
		exit
	else:
		print("\t\tChoice is not in the MENU")
		print()