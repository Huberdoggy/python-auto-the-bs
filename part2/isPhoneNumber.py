"""Playing with regex checks using new tools (i.e 'search, match, and groups')
    typically, I was always using re.fullmatch for everything I'd implement re on"""

import re

def isPhoneNumber(inp_str):
    phone_reg = re.compile(r'(\()?\d{3}(\))?-\d{3}-\d{4}')
    mo = phone_reg.search(inp_str)
    if mo:
        return f"Phone number found in your input: {mo.group()}"
    else:
        return f"Input does NOT match requirements."


while True:
    check = input("Enter a valid phone number in format xxx-xxx-xxxx => ")
    if check == 'q':
        break
    else:
        print(isPhoneNumber(check))

# Messing with raw syntax in conjunction with my habit of compiling dictionaries full of patterns

# reg_patterns = {
#         'phone_pat': re.compile(r'\d{3}-\d{3}-\d{4}'),
#     }


# spidey_reg = re.compile(r'Spidey(\ssense|\sweb|\sgloves)')
# mo = spidey_reg.search('Spiderman has Spidey sense')
# print(mo.group())
# print(mo.group(1))