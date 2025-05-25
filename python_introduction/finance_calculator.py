# user input
income = float(input ("Enter your Monthly Income: "))
expenses = float(input ("Enter your Total Expenses: "))


 # calculate monthly savings
monthly_savings = income - expenses

 # calculate annual savings
annual_savings = (monthly_savings * 12 ) + (monthly_savings * 12 * 0.05)

 # print result
print(f"Your Monthly Savings are: {monthly_savings}")
print(f"Your Total Annual Savings are: {annual_savings}")
