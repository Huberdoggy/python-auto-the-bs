'''Multi-line print formatting reference &
string manipulation stuff'''

# print(""" Dear Alice,
#
# Eve's cat has been arrested for catnapping, cat burglary,
# and extortion.
#
# Sincerely,
#
# Kyle
# """)

spam = "Hello World!"
count = 0

for i in range(len(spam)):
    print(f"- Character {count}: {spam[i]}")
    count += 1


