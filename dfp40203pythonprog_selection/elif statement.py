savings = float(input('Enter how much you have in saving: '))
#condition for if else can use in() or not,if saving==0/if (saving==0)
if savings==0: 
	print("No savings")
elif savings<500:
	print("Well done")
elif savings<1000:
	print("That a tidy sum")
elif savings<10000:
	print("You are awesome")
else:
	print("Thank you")