month_income = input("Enter your monthly income: ")
month_expen = input("Enter your total monthly expenses: ")
month_savings = month_income - month_expen

annual_int = 5/100
proj_sav = month_savings * 12 + (month_savings * 12 * annual_int)

print(f"Your monthly savings are ${month_savings}.")
print(f"Projected savings after one year, with interest, is: ${proj_sav}.")
