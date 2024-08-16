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
        
    # Calculate the next step cells based on current step cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            
            # Count Number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top Left Neighbor is alive
                