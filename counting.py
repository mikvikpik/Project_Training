# using while loops
# dangerous and can be infinite if there is no exit or end to while

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# second loop - using continue in a loops

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# avoiding infinite loops
# will stop at 5
x = 1
while x < 5:
    print(x)
    x += 1

# will never stop
# will print '1' forever
# x =1
# while x < = 5:
#   print(x)
