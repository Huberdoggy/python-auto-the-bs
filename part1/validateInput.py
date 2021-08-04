import pyperclip

while True:
    age = input("Enter your age => ")
    if age.isdecimal(): # if it's composed of only numbers
        break
    else:
        print(f"{age} is NOT a number!\nPlease enter a number"
              f" for your age")

# If first loop is satisfied, break out and run the below 'while' loop

while True:
    password = input('Select a new password (letters and numbers only) => ')
    if password.isalnum(): # if it has only letters and numbers
        break
    else:
        print(f"{password} is NOT in the correct format"
              f" ...it must have only letters and numbers.")


# pyperclip.copy("Hello Kyle, this is a ghost-copy test.")
# print(pyperclip.paste())