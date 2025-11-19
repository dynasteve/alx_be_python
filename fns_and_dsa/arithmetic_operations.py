def perform_operation(num1, num2, operation):
  def add(num1, num2):
    """Returns the sum of 2 values num1 and num 2"""
    return num1 + num2

  def subtract(num1, num2):
    """Returns the difference of 2 values num1 and num 2"""
    return num1 - num2

  def multiply(num1, num2):
    """Returns the product of 2 values num1 and num 2"""
    return num1 * num2

  def divide(num1, num2):
    """Returns the quotient of 2 values num1 and num 2"""
    if num2 == 0:
      return "Cannot divide by 0"
    else:
      return num1 / num2
    
  match operation:
    case "add":
      return add(float(num1), float(num2))
    case "subtract":
      return subtract(float(num1), float(num2))
    case "multiply":
      return multiply(float(num1), float(num2))
    case "divide":
      return divide(float(num1), float(num2))



