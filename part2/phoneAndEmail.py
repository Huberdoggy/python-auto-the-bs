# Finds phone numbers & email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # Area code with or without parentheses (optional)
(\s|-|\.)?                      # sep (optional)
(\d{3})                         # first 3 digits
(\s|-|\.)?                      # sep (optional)
(\d{4})                         # last 4 digits
(\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension (optional)
)''', re.VERBOSE)

# Remember, bracket classes eliminate special meaing for chars like 'dot' and 'plus' so no need to escape them
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       # Username (one or more of chars in defined bracket class)
@                       # @ symbol
[a-zA-Z0-9.-]+          # domain name (one or more of chars in defined bracket class)
(\.[a-zA-Z]{2,4})      # dot something (ex. com, eu, gov)
)''', re.VERBOSE)

# Find matches in clipboard text (After Ctrl+C on webpage)

text = str(pyperclip.paste())
matches = []  # Store matches found from Ctrl+V
for groups in phoneRegex.findall(text):  # Will return tuples for each match.
    # Each tuple holds str for each regex group - i.e '()' parentheses grouping
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # Corresponds to area code, first 3 digits and
    # last 4 digits. We will standardize the format by joining with '-', regardless of the format of found matches
    if groups[8]:  # The final 'ext' group - This is at 8 due to the nested grouping in the regex expression
        phoneNum += ' x' + groups[8]  # Standardize this extension format as well
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # Append the entire match - i.e 'groups' at zero

# Now, copy match results back to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))  # Separate them via a newline
    print("Copied to the clipboard:")
    print('\n'.join(matches))  # Print each match on newline
else:
    print("No phone numbers or email addresses found.")
