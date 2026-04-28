import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] + move[0],
                current_node.position[1] + move[1]
            )

            if (node_position[0] < 0 or node_position[0] >= len(grid) or
                node_position[1] < 0 or node_position[1] >= len(grid[0])):
                continue

            if grid[node_position[0]][node_position[1]] != 0:
                continue

            if node_position in closed_set:
                continue

            neighbor = Node(node_position, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(node_position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            skip = False
            for open_node in open_list:
                if neighbor.position == open_node.position and neighbor.g >= open_node.g:
                    skip = True
                    break

            if not skip:
                heapq.heappush(open_list, neighbor)

    return None


def print_grid(grid, path):
    grid_copy = [row[:] for row in grid]
    for r, c in path:
        grid_copy[r][c] = "*"

    print("\nGrid with path (*):")
    for row in grid_copy:
        print(" ".join(str(cell) for cell in row))


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter grid row by row (0 = free, 1 = obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input(f"Row {i}: ").split()))
    grid.append(row)

print("\nEnter start position (row col):")
start = tuple(map(int, input().split()))

print("Enter goal position (row col):")
end = tuple(map(int, input().split()))

path = astar(grid, start, end)

if path:
    print("\nPath found:")
    print(path)
    print_grid(grid, path)
else:
    print("\nNo path found")