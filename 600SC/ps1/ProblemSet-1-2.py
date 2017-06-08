balance = float(raw_input('Enter the outstanding balance on the credit card: '))
interestRate = float(raw_input('Enter annual interest rate: '))

monthlyInterestRate = interestRate / 12.0
monthlyPayment = 10
months = 12
startingBalance = balance
while True:
    balance = startingBalance
    for x in range(12):
        balance = (balance * (1+(interestRate / 12.00))) - monthlyPayment
        if balance < 0:
            break
    if balance < 0:
        print 'RESULT ' + '\n' + ' Monthly payment to pay off debt in 1 year: $' + str(round(monthlyPayment, 2)) + '\n Number of months needed: ' + str(x+1) +'\n Balance: $' + str(round(balance, 2))
        break
    monthlyPayment = monthlyPayment + 10
