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