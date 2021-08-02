import sys

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    """Draw a simulation of a tic-tac-toe board and print it
    to screen...this won't print the keys since we're tell it to
    only print the null values and append the '|' boundaries respectively"""
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# Call the function with the elements of the 'board' dictionary from earlier to prettify the board boundaries
# Start a game - set range for 9 (corresponds to board spaces/turns able to be taken)
turn = 'X' # Init the default turn
for i in range(9):
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space?? (or nothing to forfeit)")
    move = input("=> ")
    if move == '':
        print("Goodbye, quitter")
        sys.exit()
    else:
        theBoard[move] = turn # assign the 'X or O' to the spot specified on the board
        # Now, use if/else to swap turns like so:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
# Print the end-game board if turns actually get to the boundary of 'range'
printBoard(theBoard)