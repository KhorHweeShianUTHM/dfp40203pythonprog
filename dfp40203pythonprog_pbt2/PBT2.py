from tkinter import * # Import tkinter
class LoanCalculator: # class LoanCalculator
 
    def __init__(self): # function __init__ with argument self keyword
    	# compute the total payment
        window = Tk()  # create the widget
        window.title("Loan Calculator") # set title name

        # create the input boxes(left side)
        Label(window, text = "Annual Interest Rate").grid(row = 1,
                                          column = 1, sticky = W) # place of annual interest rate name with West side
        Label(window, text = "Number of Years").grid(row = 2,
                                      column = 1, sticky = W) # place of number of years input name with West side
        Label(window, text = "Loan Amount").grid(row = 3,
                                  column = 1, sticky = W) # place of loan amount input name with West side
        Label(window, text = "Monthly Payment").grid(row = 4,
                                      column = 1, sticky = W) # place of monthly payment input name with West side
        Label(window, text = "Total Payment").grid(row = 5,
                                    column = 1, sticky = W) # place of total payment input name with West side
 
        # for taking inputs(right side)
        self.annualInterestRateVar = StringVar() # Annual Interest Rate StringVar() helps you manage the value of a widget
        Entry(window, textvariable = self.annualInterestRateVar,
                     justify = RIGHT).grid(row = 1, column = 2) # text widget of Annual Interest Rate
        self.numberOfYearsVar = StringVar() # Number of Years StringVar() helps you manage the value of a widget
 
        Entry(window, textvariable = self.numberOfYearsVar,
                 justify = RIGHT).grid(row = 2, column = 2) # text widget of Number of Years
        self.loanAmountVar = StringVar() # Loan Amout StringVar() helps you manage the value of a widget
 
        Entry(window, textvariable = self.loanAmountVar,
              justify = RIGHT).grid(row = 3, column = 2) # text widget of loanAmount
        self.monthlyPaymentVar = StringVar() # Monthly Payment StringVar() helps you manage the value of a widget
        lblMonthlyPayment = Label(window, textvariable =
                           self.monthlyPaymentVar).grid(row = 4,
                           column = 2, sticky = E) # place of Monthly Payment display output with East side
 
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable =
                       self.totalPaymentVar).grid(row = 5,
                       column = 2, sticky = E) # place of Total Payment display output with East side
         
        # create the button
        btComputePayment = Button(window, text = "Compute Payment",
                                  command = self.computePayment).grid(
                                  row = 6, column = 2, sticky = E) # place of Compute Payment button with East side
        window.mainloop() # Create an event loop
 
 
    
    def computePayment(self): # function computePayment with argument self keyword
        # calculate the total payment         
        monthlyPayment = self.getMonthlyPayment( # get() is a method or function that used for receiving users input
        float(self.loanAmountVar.get()), # get loan amount from user in float type
        float(self.annualInterestRateVar.get()) / 1200, # get interest rate per year(divide by 1200) from user
        int(self.numberOfYearsVar.get())) # get number of years from user in integer type
 
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) # '10.2f' means minimum of field width 10, 2 decimal places
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                                * int(self.numberOfYearsVar.get()) # formula for calculating total payment
 
        self.totalPaymentVar.set(format(totalPayment, '10.2f')) # display total payment and included its parameter and format

  	# function getMonthlyPayment with argument self keyword , loanAmount, monthlyInterestRate, numberOfYears
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):   
    # calculate the monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / (1 # formula of calculating monthly Payment
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)) # formula of calculating monthly Payment
        return monthlyPayment; # return the result of monthly payment
        root = Tk() # create the widget
 		# root = Tk() is a main application window included a title bar and also its border

LoanCalculator() # call the class to run the program