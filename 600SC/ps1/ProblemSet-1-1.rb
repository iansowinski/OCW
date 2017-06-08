puts "Enter the outstanding balance on the credit card: "
balance = gets.to_f
puts "Enter annual interest rate: "
interestRate = gets.to_f
puts "Enter minimum monthly payment rate: "
minimumRate = gets.to_f

remainingBalance = balance

for x in 0..11 do
  minimumMonthlyPayment = (minimumRate * remainingBalance).round(2)

  interestPaid = ((interestRate / 12.00) * remainingBalance).round(2)

  principalPaid = (minimumMonthlyPayment - interestPaid).round(2)
  remainingBalance = (remainingBalance - principalPaid).round(2)

  puts "MONTH" + (x+1).to_s + "\n" + " Minimum monthly payment: $" + minimumMonthlyPayment.to_s + "\n" + "Principle paid: $" + principalPaid.to_s + "\n" + "Remaining balance: $" + remainingBalance.to_s
end
