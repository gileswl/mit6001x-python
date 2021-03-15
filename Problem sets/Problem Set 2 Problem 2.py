# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
#    balance - the outstanding balance on the credit card
#
#    annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#
# Lowest Payment: 180 
#
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
# 
#    Monthly interest rate = (Annual interest rate) / 12.0
#    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# get the initial values - uncomment for automated tests

# initialBalance = float(input('What is the initial balance? '))
# annualInterestRate = float(input('What is the annual interest rate, expressed as a decimal (e.g. 20% = 0.2)? '))
# totalMonths = float(input('How long is the period in months? '))
# balance = initialBalance

# set values for automated tests

totalMonths = 12
initialBalance = balance

# Make an initial guess about a satisfactory payment rate and round the guess to the nearest $10.

paymentRateGuess = (initialBalance / totalMonths)
lowerBound = 0
upperBound = initialBalance

# calculate the balance at the end of the year with this payment rate

monthsPassed = 0
monthlyInterestRate = annualInterestRate / 12

while abs(lowerBound - upperBound) > 1:
    while monthsPassed < totalMonths:
        unpaidBalance = balance - paymentRateGuess 
        balance = unpaidBalance + (unpaidBalance*monthlyInterestRate)
        monthsPassed += 1
    remainingBalance = balance
    monthsPassed = 0
    balance = initialBalance
    # If the balance remains positive, set a lower bound. make a new higher guess by averaging the guess and the upper bound, and round it to the nearest $10
    # If the balance is zero or less, set an upper bound. make a new lower guess by averaging the guess and the lower bound, and round it to the nearest $10. When the lower bound and the upper bound converge, you have your answer
    if remainingBalance > 0:
        lowerBound = paymentRateGuess
        paymentRateGuess = ((paymentRateGuess + upperBound) / 2)
#        print('New guess is ' +str(paymentRateGuess))
    else:
        upperBound = paymentRateGuess
        paymentRateGuess = ((paymentRateGuess + lowerBound) / 2)
#        print('New guess is ' +str(paymentRateGuess))
if lowerBound - round(lowerBound,-1) > 0:
    print('Lowest Payment: ' + str(int(round((lowerBound+5),-1))))
else:
    print('Lowest Payment: ' + str(int(round(lowerBound,-1))))