import sys, random 

print('ROCK', 'PAPER', 'SCISSORS')
# Init Vars to keep track of wins and losses
wins = 0
losses = 0
ties = 0

# The main loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program if player picks 'q'
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the Player input loop
        print('Type one of r, p, s or q.')
        
    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versu...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    # Display what the Computer chose
    randomNumber = random.randint(1, 3)
    