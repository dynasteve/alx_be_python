size = int(input("Enter the size of the pattern: "))
y = 1

while y <= size:
  for val in range(0,size):
    print("*", end="")
  print("")
  y += 1