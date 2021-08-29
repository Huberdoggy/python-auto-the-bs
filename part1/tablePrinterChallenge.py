"""Write a function named printTable() that takes
a list of lists of strings and displays it in a well-organized table
with each column right-justified"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def get_longest_str(list_data):
    colWidths = [0] * len(list_data) # Returns a list of Zeroes corresponding to the
    # number of nested lists in tableData => i.e [0, 0, 0]
    count = 0
    while count < len(list_data):
        for item in list_data[count]:
            if len(item) > colWidths[count]: # So initially, if greater than zero...
                colWidths[count] = len(item) # Store new 'longest' value in the respective
                # nested list
        count += 1 # Increment so that we can iterate to the next nested list
    return colWidths


longest_str_totals = get_longest_str(tableData)
print(longest_str_totals)

for word in range(len(tableData[0])): # print all 4 items from each list
    for item in range(len(tableData)): # Nested so (i.e [0][0], [1][0])
        # Each 'item' will print with 'rjust' corresponding
        # to the longest word in said nested list (i.e - 8, 5, 5)
        print(tableData[item][word].rjust(longest_str_totals[item]), end=' ')
    print()







