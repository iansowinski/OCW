balance = float(raw_input('Enter the outstanding balance on the credit card: '))
interestRate = float(raw_input('Enter annual interest rate: '))
minimumRate = float(raw_input('Enter minimum monthly payment rate: '))

remainingBalance = balance

for x in range(12):
    minimumMonthlyPayment = round((minimumRate * remainingBalance), 2)
    interestPaid = round(((interestRate / 12.00) * remainingBalance), 2)
    principalPaid = round((minimumMonthlyPayment - interestPaid), 2)
    remainingBalance = round((remainingBalance - principalPaid), 2)

    print 'MONTH ' + str(x+1) + '\n' + ' Minimum monthly payment: $' + str(minimumMonthlyPayment) + '\n Principle paid: $' + str(principalPaid) + '\n Remaining balance: $' + str(remainingBalance)
