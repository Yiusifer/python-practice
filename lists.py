names = ["Adam", "John", "Bob", "Mary", "Joseph"]

print(names[0])

print(names[-1])

print(names[-2])

names[0] = "Barbara"

print(names[0])

print(names)

# Printing based on start and end index
# Will not modifiy original array
# Starts at listed index, ends at the index before the given end
print(names[0:3])