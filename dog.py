"""Creating Class"""

#Creating the Dog class
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in respone to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# Class is above
# Instance is a Class being used
# Instance below

my_dog = Dog('willie', 6)

# Instance being used for variable input

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# does not print because it only initializes
my_dog.name

# Does print because of the function inside the class
my_dog.sit()
my_dog.roll_over()


# Second Instance
your_dog = Dog('lucy', 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
