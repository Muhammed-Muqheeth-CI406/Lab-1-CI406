from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        print(*queue)
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}

print("Enter parent and child nodes. Format: Parent Child1 Child2 ...")
print("Enter blank line to finish input.")

while True:
    line = input()
    if not line.strip():
        break
    parts = line.split()
    parent = parts[0]
    children = parts[1:]
    graph[parent] = children

start = input("Enter start node: ")
bfs(graph, start)