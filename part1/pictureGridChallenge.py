grid = \
    [['.', '.', '.', '.', '.', '.'],
     ['.', 'O', 'O', '.', '.', '.'],
     ['O', 'O', 'O', 'O', '.', '.'],
     ['O', 'O', 'O', 'O', 'O', '.'],
     ['.', 'O', 'O', 'O', 'O', 'O'],
     ['O', 'O', 'O', 'O', 'O', '.'],
     ['O', 'O', 'O', 'O', '.', '.'],
     ['.', 'O', 'O', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.']]


row_items = 6
col_items = 9
# Remember, the 'range' excludes the last digit, ex. 9 will
# actually stop at 8
for i in range(row_items):
 for j in range(col_items):
  if j < 8: # starting from 0 (list index syntax here), so don't add new line
   print(grid[j][i], end='')
  else: # add the new line to start next row
   print(grid[j][i])