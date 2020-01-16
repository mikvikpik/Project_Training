""" Changing, Adding, and Removing Elements"""

# create list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# edit element in list
# overwrite 0 index element
motorcycles[0] =  'ducati'

# print overwrite
print(motorcycles)

# append to list
motorcycles.append('honda')

# print append
print(motorcycles)

# new empty list overwrite
motorcycles = []
# add to list by append
# append will add onto end of list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# should print in a list with honda first and suzuki last
print(motorcycles)

# using insert to add new item to list without overwrite
# insert calls for 2 params, first is index location, second is value
motorcycles.insert(0,'ducati')
# print now has ducati in 0 index pos
print(motorcycles)

# removing an element from list

# new list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# deleting 0 index element
del motorcycles[0]
# should print with 'honda' deleted
print(motorcycles)

# restart delete and delete 1 index
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# removing an item from list using pop
# start with orig list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# define pop element to show relevance
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# printing using strings and lists and popped list element
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print("The last motorcycle I owned was a " + last_owned.title() + ".")

# pop any element index from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')


# removing any item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# removing an item set as a variable
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
# note use of whitespace tag \n for printing to new line
print("\nA " + too_expensive.title() + " is too expensive for me.")

