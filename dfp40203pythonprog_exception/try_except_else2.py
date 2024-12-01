try:
	num = int(input("Enter the number:"))
	num1 = int(input("Enter divisible number:"))
	result = num/num1 #15/3=5
except ValueError:
	print("Value is not int type")
except ZeroDivisionError as e:
	print("Don't use zero",e) # e = caught exception in python
else:
	print("result is ",round(result,2)) # round use to round up number, so the ans must be 2 decimal number.