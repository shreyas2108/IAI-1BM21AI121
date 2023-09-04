from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent, move, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def get_blank_position(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def is_goal_state(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != i * n + j + 1:
                return False
    return True

def get_possible_moves(state):
    moves = []
    i, j = get_blank_position(state)
    n = len(state)

    if i > 0:
        moves.append("UP")
    if i < n - 1:
        moves.append("DOWN")
    if j > 0:
        moves.append("LEFT")
    if j < n - 1:
        moves.append("RIGHT")

    return moves

def apply_move(state, move):
    i, j = get_blank_position(state)
    new_state = [list(row) for row in state]

    if move == "UP":
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif move == "DOWN":
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif move == "LEFT":
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif move == "RIGHT":
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

    return new_state

def solve_puzzle(initial_state):
    n = len(initial_state)
    initial_node = PuzzleNode(initial_state, None, None, 0)

    priority_queue = PriorityQueue()
    priority_queue.put(initial_node)

    visited_states = set()

    while not priority_queue.empty():
        current_node = priority_queue.get()
        current_state = current_node.state

        if is_goal_state(current_state):
            moves = []
            while current_node.parent:
                moves.append(current_node.move)
                current_node = current_node.parent
            moves.reverse()
            return moves

        visited_states.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            new_state = apply_move(current_state, move)
            if tuple(map(tuple, new_state)) not in visited_states:
                new_node = PuzzleNode(new_state, current_node, move, current_node.cost + 1)
                priority_queue.put(new_node)

    return None

# Read input
k = int(input())
initial_state = [list(map(int, input().split())) for _ in range(k)]

# Solve the puzzle
moves = solve_puzzle(initial_state)

# Print the solution
if moves:
    print(len(moves))
    for move in moves:
        print(move)
else:
    print("No solution found")
