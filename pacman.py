from queue import PriorityQueue

def nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    # Define the directions for UP, DOWN, LEFT, and RIGHT
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # Create a visited array to keep track of visited cells
    visited = [[False] * c for _ in range(r)]
    
    # Create a priority queue (min-heap) for UCS
    pq = PriorityQueue()
    
    # Initialize the priority queue with the starting position and cost
    pq.put((0, pacman_r, pacman_c))
    
    # Initialize the parent dictionary to store the path
    parent = {}
    
    while not pq.empty():
        cost, curr_x, curr_y = pq.get()
        
        # Mark the current cell as visited
        visited[curr_x][curr_y] = True
        
        # If the current cell is the food, break the loop
        if curr_x == food_r and curr_y == food_c:
            break
        
        # Explore neighbors
        for d in range(4):
            next_x, next_y = curr_x + dx[d], curr_y + dy[d]
            
            # Check if the next cell is valid and not visited
            if 0 <= next_x < r and 0 <= next_y < c and not visited[next_x][next_y] and grid[next_x][next_y] != '%':
                # Calculate the cost to move to the next cell
                move_cost = 0 if grid[next_x][next_y] == '.' else 1
                total_cost = cost + move_cost
                
                # Push the next cell into the priority queue with its cost
                pq.put((total_cost, next_x, next_y))
                
                # Store the parent of the next cell
                parent[(next_x, next_y)] = (curr_x, curr_y)
    
    # Reconstruct the path from food to pacman
    path = []
    curr_x, curr_y = food_r, food_c
    while (curr_x, curr_y) != (pacman_r, pacman_c):
        path.append((curr_x, curr_y))
        curr_x, curr_y = parent[(curr_x, curr_y)]
    path.append((pacman_r, pacman_c))
    
    # Print the distance and path
    print(len(path) - 1)
    for x, y in reversed(path):
        print(x, y)

# Sample Input
pacman_r, pacman_c = map(int, input().split())
food_r, food_c = map(int, input().split())
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]

# Call the function with the provided input
nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)
