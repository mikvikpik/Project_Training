# dictionary fundamentals

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# assigning a dictionary value to a variable

new_points = alien_0['points']
print("You just earn " + str(new_points) + " points!")

# adding more values to a dictionary
# original dict
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
# new dict
print(alien_0)

# starting with an empty dict

alien_o = {}

alien_o['color'] = 'green'
alien_o['points'] = 5

print(alien_o)

# modifying values in a dict

alien_o = {'color': 'green'}
print("The alien is " + alien_o['color'] + ".")

alien_o['color'] = 'yellow'
print("The alien is now " + alien_o['color'] + ".")

# alien update dict

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_o['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    # This is a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_o['x_position'] = alien_o['x_position'] + x_increment

print("New x-position: " + str(alien_o['x_position']))

# removing key value pairs from dict

alien_o = {'color': 'green', 'points': 5}
print(alien_o)

del alien_o['points']
print(alien_o)
