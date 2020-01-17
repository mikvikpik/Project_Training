# copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

# notice how the list is the same
print("\nMy friend's favorite foods are:")
print(friend_foods)

# separate lists exist

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# this produces overlapping duplication

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods

my_foods.append('canoli')
friend_foods.append('ice cream')

# will print out identical lists with both lists appended with both elements
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
