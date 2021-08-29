def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    # will print a header centered; calculated for the entire width of our cols
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        # print each key left-justified and padded by periods
        # print each value right-justified and padded by spaces



picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4,
                       'cookies': 8000}
printPicnic(picnicItems, 12, 5) # feed the params - dictionary, 'l' and 'r' widths
printPicnic(picnicItems, 20, 6)