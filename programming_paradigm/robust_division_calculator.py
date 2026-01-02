def safe_divide(numerator, denominator):
  try:
    numerator = float(numerator)
    denominator = float(denominator)
  except ValueError:
    return "Error: Please enter numeric values only."

  try:
    return f"The result of the division is {numerator/denominator}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
