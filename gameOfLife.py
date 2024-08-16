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
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top Neigbor alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Right Top Neighbor alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left Neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right Neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom Left Neighbor alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom Neighbor alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom Right Neighbor alive
                
            # Set cell based on Conway's game of life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1 second pause to reduce the flickering