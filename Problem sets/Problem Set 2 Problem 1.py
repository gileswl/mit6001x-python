# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# 
# The following variables contain values as described below:
# 
#    balance - the outstanding balance on the credit card
#
#    annualInterestRate - annual interest rate as a decimal
#
#    monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
#
# Remaining balance: 813.41
#
# instead of
# 
# Remaining balance: 813.4141998135 
# 
# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# 
# Remaining balance: 4784.0

# get the initial values - uncomment for automated tests

# initialBalance = float(input('What is the initial balance? '))
# annualInterestRate = float(input('What is the annual interest rate, expressed as a decimal (e.g. 20% = 0.2)? '))
# monthlyPaymentRate = float(input('What is the minimum monthy payment rate, expressed as a decimal? '))
# totalMonths = float(input('How long is the period in months? '))
# balance = initialBalance

# set values for for automated tests
totalMonths = 12

# calculate the current balance month by month

monthsPassed = 0
monthlyInterestRate = annualInterestRate / 12

while monthsPassed < totalMonths:
    unpaidBalance = balance - (balance*monthlyPaymentRate) 
    balance = unpaidBalance + (unpaidBalance*monthlyInterestRate)
    monthsPassed += 1

# format the balance as a string to two decimal places and print it out

formattedBalance = "{:.2f}".format(balance)
print('Remaining balance: ' + formattedBalance)