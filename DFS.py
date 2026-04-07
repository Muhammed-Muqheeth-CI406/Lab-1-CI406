from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

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
dfs(graph, start)