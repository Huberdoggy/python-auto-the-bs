from pprint import pprint, pformat

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0) # set default to zero so the next part doesn't error out when incrementing the char
    count[character] += 1 # jump to the next char in the variable string

pprint(count)

# print(pformat(count))