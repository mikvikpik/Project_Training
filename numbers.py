# using numerical lists

#the range function
# ends at 4
for value in range(1,5):
    print(value)

#ends at 5
for value in range(1,6):
    print(value)

# using range ot make a list of numbers
numbers = list(range(1,6))
print(numbers)

# to create number intervals, use the thrid param
even_numbers = list(range(2,11,2))
print(even_numbers)

# square numbers
# empty list
squares = []
# loop to create into list
for value in range(1,11):
    square = value**2
    squares.append(square)
# print outside of loop
print(square)

# to create more direct loop
squares = []
# loop to write into list
for value in range(1,11):
    squares.append(value**2)

print(squares)

# discovering numeric values
print("Min value of squares: " + str(min(squares)))
print("Max value of squares: " + str(max(squares)))
print("Sum of squares: " + str(sum(squares)))
