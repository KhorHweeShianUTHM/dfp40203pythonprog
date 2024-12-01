print('''
	****************************
	CALCULATION OF INCOME LIMIT
	****************************
	''')
print('''
	===============================================
	| Group     |       Income limit              | 
	|  T20      | RM10977.00-RM15041.00 and more  |
	|  M40      | RM5336.00-RM10976.00            |
	|  B40      | RM1929.00-RM5335.00             |
	===============================================
	''')
i = float(input('Please enter you income limit(RM): '))
if (i>1929 and i<5335): 
	print('Your group is B40')
elif (i>5336 and i<10976):
	print('Your group is M40')
else:
	print("Your group is T20")