month_income = int(input("Enter your monthly income: "))
month_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = month_income - month_expenses

annual_int = 5/100
proj_sav = int(monthly_savings * 12 + (monthly_savings * 12 * annual_int))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${proj_sav}.")


# monthly_savings = (monthly_income - monthly_expenses |float(monthly_income)float(monthly_expenses))