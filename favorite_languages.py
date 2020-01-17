# using dictionaries

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# loop over printing keys and values

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

# loop over just keys

for name in favorite_languages.keys():
    print(name.title())

# is the same as this

for name in favorite_languages:
    print(name.title())

# to call values, you MUST ask for the values

for value in favorite_languages.values():
    print(value.title())

# using a list and dict to loop

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    #using list
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# using conditional with dictionaries

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# looping through a dictionary in order

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking this poll.")

# looping throuhg all the variables in a dictionary

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# looping over a set where duplicates are only printed once
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# printing with lists inside dicts

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
