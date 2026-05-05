from collections import deque

GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))


def get_neighbors(state):
    neighbors = []
    
    # find blank (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(0,1), (1,0), (0,-1), (-1,0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def bfs(start):
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == GOAL:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current]))

    return None


def print_state(state):
    for row in state:
        print(row)
    print()


print("Enter initial state (use 0 for blank):")
start = []
for i in range(3):
    row = tuple(map(int, input().split()))
    start.append(row)

start = tuple(start)

path = bfs(start)

if path:
    print("\nSolution found in", len(path)-1, "moves:\n")
    for step in path:
        print_state(step)
else:
    print("No solution found")