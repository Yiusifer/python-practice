# print('Hello World')

# Declaring a variable
# Python is case sensitive
age = 20
is_online = True

# User input is saved in name variable
name = input("What is your name? ")
print("Hello " + name)

# Type conversion
birth_year = input("Enter your year of birth: ")
age = 2022 - int(birth_year)
# Note: concatenation in python requires data types to be the same
# Must be all strings or all ints, not a combo
# Fixed with int() or str()
print("You are " + str(age) + " years old.")

#Type conversions:
int()
float()
bool()
str()