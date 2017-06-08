balance = float(raw_input('Enter the outstanding balance on the credit card: '))
interestRate = float(raw_input('Enter annual interest rate: '))

monthlyInterestRate = interestRate / 12.0
monthlyPayment = 10
months = 12
startingBalance = balance
lowestBalance = 0.01

lowerBound = balance / 12.0
upperBound = (balance*(1 + (interestRate / 12.0))**12.0)/12.0

while abs(balance) > lowestBalance:
    balance = startingBalance
    monthlyPayment = (upperBound - lowerBound) / 2 + lowerBound
    for x in range(12):
        balance = (balance * (1+(interestRate / 12.00))) - monthlyPayment
        if balance < 0:
            break
    if balance > 0:
        lowerBound = monthlyPayment
    else:
        upperBound = monthlyPayment

print 'RESULT ' + '\n' + ' Monthly payment to pay off debt in 1 year: $' + str(round(monthlyPayment, 2)) + '\n Number of months needed: ' + str(x+1) +'\n Balance: $' + str(round(balance, 2))
