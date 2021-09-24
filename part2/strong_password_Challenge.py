"""Write a function that uses regular expressions to make sure the password string it
is passed is strong. A strong password is defined as one that is at least eight
characters long, contains both uppercase and lowercase characters, and has at
least one digit. You may need to test the string against multiple regex patterns to
validate its strength."""
import re
from time import sleep
# We will attempt to match each pattern individually, since it's not pertinent
# that they be in any order - only that a strong password includes ALL of these components


def compile_patterns():
    reg_expressions = {
        "length": ".{8}",
        "lower-case": "[a-z]+",
        "upper-case": "[A-Z]+",
        "digit": "\d{1}",
    }
    compiled_dict = {}
    for pattern in reg_expressions:
        new_item = re.compile(fr'{reg_expressions[pattern]}')
        compiled_dict[pattern] = new_item
    return compiled_dict


reg_dict = compile_patterns() # Now contains compiled regex objects for values

while True:
    ask = input("""\nEnter a password and I will determine if it passes the strength test 
                \nOr enter 'q' to quit anytime => """).strip()
    if ask == 'q':
        break
    else:
        count = 0  # Will add 1 for every match found in user input. Need all 4 patterns to equal 'strong password'
        pass_check = False
        while not pass_check:
            print("Now checking against length requirement...")
            sleep(2)
            if re.search(reg_dict.get("length", "empty"), ask):
                print(f'Your input {ask} passes the length test')
                pass_check = True
                count += 1
                print("\nNow checking against case requirements...")
                sleep(2)
                lower_c = reg_dict.get("lower-case", "empty")
                upper_c = reg_dict.get("upper-case", "empty")
                if (re.search(lower_c, ask) and re.search(upper_c, ask)):
                    print(f'Your input {ask} contains both upper and lowercase characters. Good job.')
                    pass_check = True
                    count += 1
                    print("\nNow checking against the digit requirement...")
                    sleep(2)
                    if re.search(reg_dict.get("digit", "empty"), ask):
                        print(f'Your input {ask} contains at least 1 digit. Excellent.')
                        pass_check = True
                        count += 1
                        if count == 3:
                            print(f"\nYOUR PASSWORD {ask} PASSED THE STRENGTH TEST!!")
                            break
                    else:
                        print(f'Your input {ask} does NOT contain at least 1 digit')
                        break
                else:
                    print(f'Your input {ask} does NOT contain an upper/lowercase combination')
                    break
            else:
                print(f'Your input {ask} is NOT at least 8 characters long')
                break
