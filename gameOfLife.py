import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add the living cell
        else:
            column.append(' ') # Add the dead cell
    nextCells.append(column) # nextCell is a list of column lists 
    
while True: # Main Program Loop
    print('\n\n\n\n\n') # Separate each step with new lines
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # of space
        print() # Print a new line at the end of the row