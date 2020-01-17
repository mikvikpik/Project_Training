# Writing clear prompts

name = input("Please enter you name: ")
print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
# a unique way to add onto a variable while still following PEP8
prompt += "\nWhat is you first name? "

name = input(prompt)
print("\nHello, " + name.title() + "!")
