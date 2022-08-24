from pydoc import tempfilepager


temperature = 5

# No curly braces in python, use indentation instead
if temperature > 30:
  print("It's a hot day!")
elif temperature > 20:
  print("It's a nice day!")
else:
  print("It's a cold day!")
print("Done")
