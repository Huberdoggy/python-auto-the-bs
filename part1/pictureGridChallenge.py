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

for i in range(row_items):
 for j in range(col_items):
  if j < 8:
   print(grid[j][i], end='')
  else:
   print(grid[j][i])