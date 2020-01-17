# using tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# trying to change tuple elements does not work

# dimensions[0] = 250 # will raise error

# loop through tuple
for dimension in dimensions:
    print(dimension)

# overwrite a tuple/variable

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("Use tuples when you don't want individual elements to be changed.")
