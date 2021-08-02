# write a function that accepts a list as an argument and returns a string with items
# separated by a comma and a space, with 'AND' inserted prior to the last item

spam = []
combo = 'and'

def formatted_list(my_lst):
    spam.insert(-1, combo)
    for i in range(len(my_lst)):
        if i < my_lst.index(combo):
            print(my_lst[i] + ', ', end='')

        else:
            print(my_lst[i] + ' ', end='')




while True:
    ask = input("Enter an item to add to the list (press 'q' to quit) => ")
    if ask == 'q' and len(spam) == 1:
        last_item = spam[-1]
        break
    elif ask == 'q':
        break
    else:
        spam.append(ask)


if len(spam) > 1:
    formatted_list(spam)
elif len(spam) == 1:
    print(f"\n\t{last_item.title()}")
elif len(spam) == 0:
    print(f"\n\t*** Nothing here ***")


