# for loops through a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# doing more with a loop
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    # additionally
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# out of the loop
print("Thank you everyone. That was a great magic show!")

#printing outside of the loop using the loop variable will only print the last known loop variable
print("I cant wait to see your next trick, " + magician.title() + ".\n")
