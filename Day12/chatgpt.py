import string
from collections import deque

def find_path():
    # Read the input from the file and split it on line breaks.
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    grid = [line.strip() for line in lines]
    
    # Parse the input to create a representation of the grid and locate the starting position (S) and the goal position (E).
    rows = len(grid)
    cols = len(grid[0])
    start = None
    goal = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                goal = (i, j)
    
    # Create a list to map each character to its numerical representation.
    elevation_map = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    
    # Create a queue to hold the positions that need to be explored. Enqueue the starting position.
    queue = deque([(start, 0)])  # Each element of the queue is a tuple (position, steps)
    
    # Create a set to keep track of the positions that have been visited.
    visited = set()
    
    # While the queue is not empty:
    while queue:
        # Dequeue the next position from the queue.
        pos, steps = queue.popleft()
        
        # If the position is the goal position, return the number of steps taken to reach it (which is the depth of the node in the search tree).
        if pos == goal:
            return steps
        
        # If the position has not been visited before:
        if pos not in visited:
            # Mark it as visited.
            visited.add(pos)
            
            # Enqueue its neighbors (i.e., the squares that are one step up, down, left, or right from it and have an elevation no more than one higher than the current position).
            i, j = pos
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= ni < rows) and (0 <= nj < cols):
                  print(grid[ni][nj])
                  elevation = elevation_map[ord(grid[ni][nj]) - ord('a')]
                  cur_elevation = elevation_map[ord(grid[i][j]) - ord('a')]
                  if elevation <= cur_elevation + 1:
                      queue.append(((ni, nj), steps+1))
    
    # If the goal position was not reached, return -1 to indicate that it is not reachable.
    return -1

# Test the function by reading the input from the file 'input.txt'.
print(find_path())
