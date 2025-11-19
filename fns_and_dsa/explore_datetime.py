from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  return current_date

def calculate_future_date(current, future):
  future_date = current + future
  return future_date.strftime("%Y-%m-%d")

current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
days = timedelta(days=int(input("Enter the number of days to add to the current date: ")))

print(f"Future date: {calculate_future_date(current_date, days)}")