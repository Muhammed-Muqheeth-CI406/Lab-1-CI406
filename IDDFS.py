def dls(graph, node, goal, limit, path):
    if node == goal:
        return path
    
    if limit == 0:
        return None
    
    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(graph, neighbor, goal, limit - 1, path + [neighbor])
            if result:
                return result
    return None


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nSearching at depth: {depth}")
        result = dls(graph, start, goal, depth, [start])
        if result:
            return result
    return None


graph = {}

while True:
    node = input("\nEnter node name (or type 'done' to finish): ")
    if node.lower() == 'done':
        break
    
    num = int(input(f"How many neighbors does {node} have? "))
    
    neighbors = []
    for i in range(num):
        neighbor = input(f"Enter neighbor {i+1} of {node}: ")
        neighbors.append(neighbor)
    
    graph[node] = neighbors


start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))


result = iddfs(graph, start, goal, max_depth)


if result:
    print("\nGoal found! Path:", " -> ".join(result))
else:
    print("\nGoal not found.")