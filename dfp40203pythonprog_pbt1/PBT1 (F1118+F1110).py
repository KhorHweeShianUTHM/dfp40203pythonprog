import os #Importing os module

import datetime 
#Allows to manipulate times and dates together such as month, day, year, hour, second, microsecond

import re
#Regular Expression Operation
#Check if a particular string matches a given regular expression

# global variable declaration and initialization
# integer variable
food_price = 0.00 # Initializing of food_price as 0 
beverage_price = 0.00 # Initializing of beverage_price as 0
total_price = 0.00 # Initializing of total_price as 0
delivery_charge = 4.00 # Initializing of delivery_charge as 4
payment = 0.00 # Initializing of payment as 0
total_overall = 0.00 # Initializing of total_overall as 0
# boolean variable
inputNumberIC = False # Initializing of inputNumberIC as False
inputNumberPhone = False # Initializing of inputNumberPhone as False 
inputNumberPostcode = False # Initializing of inputNumberPostcode as False
inputEmailAddress = False # Initializing of inputEmailAddress as False

# menu of program 
print("++----------------------------------------------++")
print("+                     WELCOME                    +")
print("++----------------------------------------------++")


now = datetime.datetime.now() # get current datetime when user start program
print("Current date :",now.strftime("%Y-%m-%d")) # show current date with year-month-day format
print("Current time :",now.strftime("%H:%M:%S")) # show current time with hour-minute-second format
print("Today is", now.strftime("%A")) # show current weekday
print() # new line


orderTime = str("*****Order Time*****") # display order time
inputDate = now.strftime("%Y-%m-%d") # get date in year-month-day format
inputTime = now.strftime("%H:%M:%S") # get time in hour-minute-second format
inputDay = now.strftime("%A") # get weekday

# menu of insert info
print("**************************************************")
print("***           Please insert your info          ***")
print("**************************************************\n")
line1 = str("\n*****CUSTOMER DETAIL*****") # display line customer detail
# get customer name
try: # try of exception handling
    inputName = str(input("Name     : ")) # enter name
    while not inputName: # if it is a blank value
        print("Your name is empty. Please insert your name again") # display output
        inputName = str(input("Name     : ")) # enter again
        continue # loops to skip the next statement
    while True: # if the answer is correct
        break # stop the question
except: # if have any exception
    pass # nothing happen
# get customer ic number
while not inputNumberIC: # if not a ic number 
    inputIC = str(input("IC       : ")) # enter ic number 
    if len(inputIC) == 12: # if length of inputIC is 12 digits
        inputNumberIC = True # it is correct
    elif len(inputIC) == 0: # if length of inputIC is 0 digit
        print("Your IC is empty. Please insert your IC again") # display output
        inputNumberIC = False # it is wrong
    else: # Besides 
        print("Invalid IC number") # display output

print() # new line
print("Please fill up your address") # get customer address
# get customer street
try: # try of exception handling
    inputStreet = str(input("Street   : ")) # enter street
    while not inputStreet: # if it is a blank value
        print("Your street is empty. Please insert your street again") # display output
        inputStreet = str(input("Street   : ")) # enter again
        continue # loops to skip the next statement
    while True: # if the answer is correct
        break # stop the question
except: # if have any exception
    pass # nothing happen
# get customer postcode
while not inputNumberPostcode: # if not a postcode number 
    inputPostcode = str(input("Postcode : ")) # enter postcode number 
    if len(inputPostcode) == 5: # if length of inputPostcode is 5 digits
        inputNumberPostcode = True # it is correct
    elif len(inputPostcode) == 0: # if length of inputPostcode is 0 digit
        print("Your Postcode is empty. Please insert your Postcode again") # display output
        inputNumberIC = False # it is wrong   
    else: # Besides 
        print("Invalid Postcode number") # display output
        
# get customer city
try: # try of exception handling
    inputCity = str(input("City     : ")) # enter city
    while not inputCity: # if it is a blank value
        print("Your city is empty. Please insert your city again") # display output
        inputCity = str(input("City     : ")) # enter again
        continue # loops to skip the next statement
    while True: # if the answer is correct
        break # stop the question
except: # if have any exception
    pass # nothing happen
# get customer state
try: # try of exception handling
    inputState = str(input("State    : ")) # enter state
    while not inputState: # if it is a blank value
        print("Your state is empty. Please insert your state again") # display output
        inputState = str(input("State    : ")) # enter again
        continue # loops to skip the next statement
    while True: # if the answer is correct
        break # stop the question
except: # if have any exception
    pass # nothing happen

# combine name of street,postcode,city and state to a address
inputAddress = (inputStreet + ", " + inputPostcode + ", " + inputCity + ", " + inputState) #Input Address

print() # new line
# get customer phone number
while not inputNumberPhone: # if not a phone number 
    inputPhone = str(input("Phone num: ")) # enter phone number
    if len(inputPhone) == 10: # if length of inputPhone is 10 digits
        inputNumberPhone = True # it is correct
    elif len(inputPhone) == 11: # if length of inputPhone is 11 digits
        inputNumberPhone = True # it is correct
    elif len(inputPhone) == 0: # if length of inputPostcode is 0 digits
        print("Your phone number is empty. Please insert your phone number again") # display output
        inputNumberIC = False # it is wrong       
    else: # Besides 
        print("Invalid phone number") # display output
# get customer email
while(True): # if it is correct 
    inputEmail = str(input("Email    : ")) # enter email 
    if re.match(r"[^@]+@[^@]+\.[^@]+", inputEmail): # if it is correct email format 
        break # stop the question 
    elif len(inputEmail) == 0: # if length of inputEmail is 0 digits
        print("Your email is empty. Please insert your email again") # display output
        inputEmailAddress = False # it is wrong
    else: # Besides 
        print("Email is not valid") # display output
        continue # loops to skip the next statement


def input_info(): # function input_info
# write a txt file as combine of date,time,weekday
# second line,customer name,ic,address,phone number,email  
    with open('Order.txt','w+') as out:
        out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'
                  .format(orderTime,"Date : "+inputDate,"Time : "+inputTime,"Day  : "+inputDay,
                          line1,"Name    : "+inputName,"IC      : "+inputIC,"Address : "+inputAddress,
                          "PhoneNum: "+inputPhone,"Email   : "+inputEmail))
                                                

input_info() #Call function

print() # new line
print("Please select your food and beverage") # display a line  
print() # new line

# shown of food and beverage menu
data1 = str("++----------------FOOD MENU----------------++")
data2 = str("+  CODE      MENU                  PRICE    +")
data3 = str("+   1.   Burger Set              (RM 11.00) +")
data4 = str("+   2.   Pizza Set               (RM 11.00) +")
data5 = str("+   3.   Spaghetti Bolognese Set (RM 12.00) +")
data6 = str("+   4.   Spaghetti Aglio Set     (RM 13.00) +")
data7 = str(" ")
data8 = str("++-------------BEVERAGE MENU---------------++")
data9 = str("+  CODE      MENU                  PRICE    +")
data10 = str("+   1.  Coca cola                    *      +")
data11 = str("+   2.  Pepsi                        *      +")
data12 = str("+   3.  Fanta Strawberry             *      +")
data13 = str("+   4.  Fanta Orange                 *      +")
data14 = str("+ *Included in the Food Set                 +")
data15 = str("++-----------------------------------------++")


def show_item(): # function show_item
    
# write a menu txt file as combine of food and beverage menu
    with open('Menu.txt','w+') as out:
        out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'
                  .format(data1,data2,data3,data4,data5,data6,data7,data8,data9,
                          data10,data11,data12,data13,data14,data15))

  
    file = open('Menu.txt', 'r') # open and read the file
    print(file.read()) # print out the file      



show_item() # call function

print("Please choose your favourite food and beverage") # display a line



def food_input_menu(a): #This is method of food_input_menu(argument)
    pass #It would raises error without the pass statement if the function is an empty statement.

while True: #While loop is primitive loop
   
    try:  #It is used to test a block of code for errors         
        food = int(input("Food code: "))  #Users input food code
        if food == 1: #If users choose 1
            food = "Burger Set" #Choice 1 is Burger Set 
            food_price = 11.00 #Burger Set is RM11.00
            food_code = 1 #Food code for Burger Set is 1
            break #It is used to break out of a loop.
        elif food == 2: #If users choose 2
            food = "Pizza Set" #Choice 2 is Pizza Set
            food_price = 11.00 #Pizza Set is RM11.00
            food_code = 2 #Food code for Pizza Set is 2
            break #It is used to break out of a loop.
        elif food == 3: #If users choose 3
            food = "Spaghetti Bolognese Set" #Choice 3 is Spaghetti Bolognese Set
            food_price = 12.00 #Spaghetti Bolognese Set is RM12.00
            food_code = 3 #Food code for Spaghetti Bolognese Set is 3
            break #It is used to break out of a loop.
        elif food == 4: #If users choose 4
            food = "Spaghetti Aglio Set" #Choice 4 is Spaghetti Aglio Set
            food_price = 13.00 #Spaghetti Aglio Set is RM13.00
            food_code = 4 #Food code for Spaghetti Aglio Set is 4
            break #It is used to break out of a loop.

    except: #It is used to handle an error
        pass #Must use pass because the statement of this exception does not exist
    print("Invalid input. Please try again") #Display exception error's message
    print() #Break the line once/it does a line break




def beverage_input_menu(a): #Method of beverage_input_menu(argument)
    pass #Used pass when this method does not has statement(avoid error occurs)
#While loop is primitive loop
while True: #Execute when the condition is true
    #Exception handling
    try: #It is used to test a block of code for errors 
        beverage = int(input("Beverage Code: ")) #Users input beverage code
        if beverage == 1: #If users choose 1
            beverage = "Coca cola" #Choice 1 is Coca-cola
            beverage_price = 0.00 #Initial value for beverage's price
            break #It is used to break out of a loop.
        elif beverage == 2: #If users choose 2
            beverage = "Pepsi" #Choice 2 is Pepsi
            beverage_price = 0.00 #Initial value
            break #It is used to break out of a loop.
        elif beverage == 3: #If users choose 3
            beverage = "Fanta Strawberry" #Choice 3 is Fanta Strawberry
            beverage_price = 0.00 #Initial value for beverage's price
            break #It is used to break out of a loop.
        elif beverage == 4: #If users choose 4
            beverage = "Fanta Orange" #Choice 4 is Fanta Orange
            beverage_price = 0.00 #Initial value for beverage's price
            break #It is used to break out of a loop.
        
    except: #It is used to handle an error
        pass #Must use pass because the statement of this exception does not exist

    print("Invalid input. Please try again") #Display output statement
    print() #Break the line once/ it does a line break
    print("Food code: ", food_code) #Users will have second choice to input the valid of food code
    

#Calculation
total_price = food_price + beverage_price #Total prices for food and beverage
total_overall = total_price + delivery_charge #Total prices included delivery's fee

print("--------------------------------------------") #Output(design pattern)
print("Dear", inputName, ",") #Retrieve user's name and display his/her name
print("Your order is", food, "RM", food_price) #Display ordered food includes with its price
print("Your order is", beverage, "RM", beverage_price) #Display ordered beverage includes with its price

print("--------------------------------------------") #Output(design pattern)
print() #Break the line once/it does a line break
#Print the receipt information
print("Food price     = RM ", format(food_price,'.2f')) #Print food price with 2 decimal places
print("Beverage price = RM ", format(beverage_price,'.2f')) #Print beverage price with 2 decimal places
print("Total price    = RM ", format(total_price,'.2f')) #Print total price with 2 decimal places
print("Delivery charge= RM ", format(delivery_charge,'.2f')) #Print delivery's fee with 2 decimal places
print("_____________________________________________") #Output(design pattern)
print("Total          = RM", format(total_overall,' .2f')) #Print overall price with 2 decimal places
                        #'.2f' means float 2 decimal places


def payment_balance(a): #Method of payment_balance(argument)
    pass #Used pass when this method does not has statement(avoid error occurs)
#While loop is primitive loop            
while True: #Execute when the condition is true
    #Exception handling 
    try: #It is used to test a block of code for errors
        payment = int(input("Cash payment   = RM  ")) #Users make payment by cash
        
        if payment >= total_price: #Cash payment must larger than total price
            balance = payment - total_overall #Calculate balance 
            print("Balance        = RM ", format(balance,'.2f')) #Display amount of balance with 2 decimal places
            break #It is used to break out of a loop.
        elif payment < total_price: #Another condition may happens if amount of payment is less than total price
            
            print("Your amount is not enough") #Display warning message to that user
            print() #Break the line once/it does a line break
            continue #It continues to the next iteration of the loop.
    except: #It is used to handle an error
        pass #Must use pass because the statement of this exception does not exist

    print("Invalid value. Please try again") #Print output statement
    print() #Break the line once/it does a line break



print() #Break the line once/it does a line break
print("Your order will arrive with in 30 minutes") #Print output statement
print() #Break the line once/it does a line break



foodPrice = str(food_price) #Create object for food_price in string type
beveragePrice = str(beverage_price) #Create object for beverage_price in string type
totalPrice = str(total_price) #Create object for total_price in string type
deliveryCharge = str(delivery_charge) #Create object for delivery_charge in string type
totalOverall = str(total_overall) #Create object for total_overall in string type
Payment = str(payment) #Create object for payment in string type
Balance = str(balance) #Create object for balance in string type

#Used to append a file
append = open("Order.txt", "a") #"a" used for writing
                                #It appends data to the end of the file/creates a new file
#Write into Order's file
append.write("\n*****ORDER INFORMATION*****") #Write output into Order's file 
append.write("\nFood        : " + food + " (RM" + foodPrice + ")") #Write the output's result into Order's file 
append.write("\nBeverage    : " + beverage + " (RM" + beveragePrice + ")") #Write the output's result into Order's file
append.write("\n") #\n=newline(used to separate the lines)
append.write("\n*****PAYMENT INFORMATION*****") #Write output into Order's file 
append.write("\nTotal price : RM" + totalPrice) #Write the output's result into Order's file 
append.write("\nDelivery charge : RM" + deliveryCharge) #Write the output's result into Order's file 
append.write("\nTotal       : RM" + totalOverall) #Write the output's result into Order's file 
append.write("\nPayment     : RM" + Payment) #Write the output's result into Order's file 
append.write("\nBalance     : RM" + Balance) #Write the output's result into Order's file 


append.close() #Close file


def yes_or_no(): #Method of yes_or_no()
    print("Do you want to view your receipt order?") #Print output statement
    print("[y]=Yes / [n]=No") #Print output statement
    YesNo = input("View Receipt? : ") #Users input either 'y' or 'n'
    print() #Break the line once/it does a line break
    
    YesNo = YesNo.lower() #lower() means lowercase's method
   
    if(YesNo == "y"): #Users input 'y' for viewing the receipt
        return 1 #Return the index value of 1
    
    elif(YesNo == "n"): #Users input 'n' if they don't want the receipt
        return 0 #Return the index value of 0
   
    else: #Else block is used for executing the FALSE condition
        print("Invalid input")
        return -1 #Return the index value of -1

while(True): #Execute when the condition is true
    inp = yes_or_no() #Create inp as an object for calling method of yes_or_no()
    if(inp == -1): #Any negative value means that function could not find its particular element
        continue #It continues to the next iteration of the loop.
    elif(inp == 1): #When users input 'y'
        file = open('Order.txt', 'r') #Read data in text's file of Order
        print(file.read()) #Display Order.txt file # file is an object for calling method of read()
    elif(inp == 0): #When users input 'n'
        print("++----------------------------------------------++") #Output(design pattern)
        print("+                   THANK YOU                    +") #Output(design pattern)
        print("++----------------------------------------------++") #Output(design pattern)
        break #It is used to break out of a loop.
    break #It is used to break out of a loop.
        

