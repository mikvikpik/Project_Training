# exploring lists

# variable bicycles is a list
bicycles = ['trek' , 'cannondale', 'redline', 'specialized']

# Print list
print(bicycles)

# print item in a list 
print(bicycles[0])

# print string in a list and modify props
print(bicycles[0].title())

# print item in a list by index starting at 0
# notice number 1 is second item in list
print(bicycles[1])

# notice number 3 is 4th item in list
print(bicycles[3])

# printing negative starts from back end of list
print(bicycles[-1])

# using print statement and strings and list variables

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

