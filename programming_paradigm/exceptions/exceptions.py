class InsufficientBalanceError(Exception):
  """Custom exception to prevent the user from withdrawing funds more than what is in their bank account"""

  def __init__(self):
    pass

  def __str__(self):
    return f"Sorry, you have insuffient funds."