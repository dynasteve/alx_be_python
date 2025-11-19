def perform_operation(num1, num2, operation):
  match operation:
    case "add":
      add(num1, num2)
    case "subtract":
      subtract(num1, num2)
    case "multiply":
      multiply(num1, num2)
    case "divide":
      divide(num1, num2)


  def add(num1, num2):
    """Returns the sum of 2 values num1 and num 2"""
    return num1 + num2

  def subtract(num1, num2):
    """Returns the difference of 2 values num1 and num 2"""
    return num1 + num2

  def multiply(num1, num2):
    """Returns the product of 2 values num1 and num 2"""
    return num1 * num2

  def divide(num1, num2):
    """Returns the quotient of 2 values num1 and num 2"""
    if num2 == 0:
      return "Cannot divide by 0"
    else:
      return num1 / num2

