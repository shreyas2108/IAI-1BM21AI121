def displayPathtoPrincess(N, grid):
    # Find the positions of 'm' (bot) and 'p' (princess)
    bot_position = None
    princess_position = None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # Calculate the difference in positions to determine the moves needed
    delta_x = princess_position[0] - bot_position[0]
    delta_y = princess_position[1] - bot_position[1]

    # Generate and print the moves to rescue the princess
    moves = []
    if delta_x < 0:
        moves.extend(['UP'] * abs(delta_x))
    elif delta_x > 0:
        moves.extend(['DOWN'] * abs(delta_x))

    if delta_y < 0:
        moves.extend(['LEFT'] * abs(delta_y))
    elif delta_y > 0:
        moves.extend(['RIGHT'] * abs(delta_y))

    for move in moves:
        print(move)

# Read input
N = int(input())
grid = [list(input()) for _ in range(N)]

# Call the function to rescue Princess Peach
displayPathtoPrincess(N, grid)
