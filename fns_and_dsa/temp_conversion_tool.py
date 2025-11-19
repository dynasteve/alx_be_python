FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
  return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32


def main():
  try:
    temp = float(input("Enter the temperature to convert: "))
  except:
    print("Invalid temperature. Please enter a numeric value.")
    main()

  temptype = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

  match temptype:
    case "C":
      print(f"{temp}°{temptype} is {convert_to_fahrenheit(temp)}")

    case "F":
      print(f"{temp}°{temptype} is {convert_to_celsius(temp)}")

    case _:
      print("invalid temperature type. Please input C or F")

if __name__ == "__main__":
  main()
