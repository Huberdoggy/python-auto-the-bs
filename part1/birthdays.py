birthdays = {'Kyle': 'Jan 7', 'Paul': 'Jan 26', 'Stephen': 'Dec 8'}

while True:
    name = input("Enter a name (or nothing to quit) => ")
    if name == '':
        break
    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}.")
    else:
        print(f"I don't have a birthday for {name}.")
        print("What is their birthday?")
        their_bday = input("=> ")
        birthdays[name] = their_bday
        print(f"Birthday database updated with {name}'s bday of {their_bday}.")

