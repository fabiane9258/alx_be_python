
# User input
monthly_income = float(input("Enter your Monthly Income: "))
monthly_expenses = float(input("Enter your Total Expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings with 5% interest
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Print results
print(f"Your Monthly Savings are: {monthly_savings:.2f}")
print(f"Your Total Annual Savings are: {annual_savings:.2f}")
