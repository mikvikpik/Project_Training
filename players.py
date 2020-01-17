# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# print different slice
print(players[1:4])

# print different slice
print(players[:4])

# print different slice
print(players[-3:])

# loop through slice of list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

