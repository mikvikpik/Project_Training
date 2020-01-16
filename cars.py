""" Organizing a list """
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# sort is by alpha
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort reverse requires reverse param
cars.sort(reverse = True)
print(cars)

# temp sort a list with sorted ed='expect disappear'
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# printing a list in reversed order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# reverse call perm reverses list
cars.reverse()
print(cars)


# length of list
print(len(cars))
