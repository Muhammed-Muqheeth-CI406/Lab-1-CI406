def dls(graph, start, goal, limit):
    visited = set()
    stack = [(start, 0)]   # (node, depth)

    while stack:
        node, depth = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            if node == goal:
                print("\nGoal found!")
                return True

            if depth < limit:
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1))

    print("\nGoal not found within depth limit.")
    return False


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
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

dls(graph, start, goal, limit)