# Methods
# A function that is part of an object = method

course = "i am learning python"
capitalizedString = course.capitalize()
upperCaseString = course.upper()

print(capitalizedString)
print(upperCaseString)

# Index in python starts at 0
# This will also count white spaces
print(course.find('y'))
print(course.find("am"))

# Using 'in' operator to determine if a word / character is in the string
# Returns boolean
jsCheck = 'javscript' in course
print("Is the word 'javascript' in the 'course' string? " + str(jsCheck))

pythonCheck = 'python' in course
print("Is the word 'python' in the 'course' string? " + str(pythonCheck))

# Replace will not modify the original string
modifiedString = course.replace('python', 'javascript')
print(modifiedString)
print(course)