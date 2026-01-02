from exceptions.exceptions import InsufficientBalanceError

class BankAccount:
  def __init__ (self, account_balance = 0):
    self.account_balance = account_balance

  def deposit(self, amount):
    return amount + self.account_balance

  def withdraw(self, amount):
    try:
      if self.account_balance <= 0 or amount >= self.account_balance:
        raise InsufficientBalanceError
      else:
        return True
    except:
      return False
    finally:
      pass

  def display_balance(self):
    print (f"Current Balance: ${self.account_balance}")
    return self.account_balance
