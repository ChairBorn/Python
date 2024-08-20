theBoard = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ', # The Data Structure that models the TicTacToe board
            'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',
            'Low-L': ' ', 'Low-M': ' ', 'Low-R': ' '}

def printBoard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('-+-+-')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('-+-+-')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])
    print('-+-+-')
printBoard(theBoard)