monthly_income = input("Enter your monthly income:")
total_monthly_expenses = input("Enter your total monthly expenses:")
monthly_savings = int(monthly_income) - int(total_monthly_expenses)
projected_savings =int(int(monthly_savings) * 12 + (int(monthly_savings) * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")