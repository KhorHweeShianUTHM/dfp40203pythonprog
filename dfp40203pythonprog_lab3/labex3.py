#labex3 - Khor Hwee Shian 03DDT19F1118
#question1 - Write a program to read data from a user’s input text file (phonelist.txt)
#			 Count the number of its appearance in the list
#			 Display the output
#			 Then write the output in the output text file


import os # All of the following code assumes you have os imported.
class NumberCount: # class declaration
	# variable declaration
	aliah_tel = 0
	robert_tel = 0
	abu_tel = 0
	azman_tel = 0
	james_tel = 0
	sopi_tel = 0
	siti_tel = 0
	ali_tel = 0

	try:
		file = open("phonelist.txt", "r") # open the phonelist.txt file, and the Access Mode is r = reading
		contact = file.readlines() # read all in file
		for line in contact: # line in contact
			if 'Aliah' in line: # if find 'Aliah' word in lile so it will count it
				aliah_tel += 1 # aliah_tel = aliah_tel + 1
			if 'Robert' in line: # if find 'Robert' word in lile so it will count it
				robert_tel += 1 # robert_tel = robert_tel + 1
			if 'abu' in line: # if find 'abu' word in lile so it will count it
				abu_tel += 1 # abu_tel = abu_tel + 1
			if 'azman' in line: # if find 'azman' word in lile so it will count it
				azman_tel += 1 # azman_tel = azman_tel + 1
			if 'James' in line: # if find 'James' word in lile so it will count it
				james_tel += 1 # james_tel = james_tel + 1
			if 'sopi' in line: # if find 'sopi' word in lile so it will count it
				sopi_tel += 1 # sopi_tel = sopi_tel + 1
			if 'siti' in line: # if find 'siti' word in lile so it will count it
				siti_tel += 1 # siti_tel = siti_tel + 1
			if 'ali' in line: # if find 'ali' word in lile so it will count it
				ali_tel += 1 # ali_tel = ali_tel + 1
	        	
		# display output
		print(f'aliah-0194022445: {aliah_tel} times')
		print(f'robert-011145569: {robert_tel} times')
		print(f'abu-0124512123: {abu_tel} times')
		print(f'azman-0137894561: {azman_tel} times')
		print(f'james-0194789632: {james_tel} times')
		print(f'sopi-0124563210: {sopi_tel} times')
		print(f'siti-0177451236: {siti_tel} times')
		print(f'ali-0194022433: {ali_tel} times')
		print()

		file.close() # file close

	except:
		print("Sorry, I cannot find the File...") # exception: when system cannot find file

	select = ""

	while (select != 'Y' or select != 'y') and (select != 'N' or select != 'n'): # while looping statement, while select is not y and n it will loop
		select = str(input('Would you like to output these results to a file?(Y/N)\n'))
		if(select == 'Y' or select == 'y'): # if selection statement, if he/she insert Y/y
			path = str(input("Please enter the path of the text file that you want to solve.(example: C:/Users/TOSHIBA/Desktop/PROJECTNAME/phonelist.txt)\n"))
			print('---------------------------------------------')
			print('Congratulation , File is created ! !')
			print('---------------------------------------------')
			desktop = os.path.expanduser("~\\Desktop") # it will automatic scan user path example: C:\Users\TOSHIBA\Desktop

			# remove path from file name
			# for example, C:\Users\TOSHIBA\Desktop\[python] labex3_03ddt19f1118\phonelist.txt to phonelist.txt
			file_name = path.split("/")[-1]
			# remove file extension from name
			# for example, phonelist.txt to phonelist
			title = file_name.rsplit(".",1)[0]

			resultFile = open(title + "_result.txt","w") # write the result to the new txt file which its name is phonelist_result.txt
			resultFile.write("My Result from {}: \n\n".format(file_name)) # shown the path that user insert which its name is C:\Users\TOSHIBA\Desktop\[python] labex3_03ddt19f1118\phonelist.txt

			resultA = str(aliah_tel) # change the int variable to str variable(new variable named resultA)
			resultFile.write('aliah-0194022445: ' + resultA + ' times\n')

			resultB = str(robert_tel) # change the int variable to str variable(new variable named resultB)
			resultFile.write('robert-011145569: ' + resultB + ' times\n')

			resultC = str(abu_tel) # change the int variable to str variable(new variable named resultC)
			resultFile.write('abu-0124512123: ' + resultC + ' times\n')

			resultD = str(azman_tel) # change the int variable to str variable(new variable named resultD)
			resultFile.write('azman-0137894561: ' + resultD + ' times\n')

			resultE = str(james_tel) # change the int variable to str variable(new variable named resultE)
			resultFile.write('james-0194789632: ' + resultE + ' times\n')

			resultF = str(sopi_tel) # change the int variable to str variable(new variable named resultF)
			resultFile.write('sopi-0124563210: ' + resultF + ' times\n')

			resultG = str(siti_tel) # change the int variable to str variable(new variable named resultG)
			resultFile.write('siti-0177451236: ' + resultG + ' times\n')

			resultH = str(ali_tel) # change the int variable to str variable(new variable named resultH)
			resultFile.write('ali-0194022433: ' + resultH + ' times\n')

			resultFile.close() # close file
			break # stop it
		elif(select == 'N' or select == 'n'): # if he/she insert N/n
			print('---------------------------------------------')
			print('Goodbye, See you next again ! ! ')
			print('---------------------------------------------')
			break # stop it