weight = input("Enter your weight: ")

unit = input("(K)g or (L)bs: ")

# print(type(unit))

if unit.upper() == "K":
  convertedWeight = int(weight) * 2.2
  print("Your weight in pounds is: " + str(convertedWeight))
elif unit.upper() == "L":
  convertedWeight = int(weight) / 2.2
  print("Your weight in pounds is: " + str(convertedWeight))
else:
  print("Please enter a valid unit of measurement")
