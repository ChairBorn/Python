theBoard = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ', # The Data Structure that models the TicTacToe board
            'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',
            'Low-L': ' ', 'Low-M': ' ', 'Low-R': ' '}
# All the keys need to be passed for the function to work

def printBoard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('-+-+-')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('-+-+-')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])
    print('-+-+-')

# Let's take User's input
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)