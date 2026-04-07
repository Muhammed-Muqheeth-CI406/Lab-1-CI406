import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.enqueue(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while not frontier.is_empty():
        current = frontier.dequeue()
        
        if current == goal:
            break
        
        for neighbor, cost in graph.get(current, []):
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.enqueue(neighbor, new_cost)
                came_from[neighbor] = current
    
    if goal not in came_from:
        return None, None
    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return cost_so_far[goal], path

# Define the graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)]
}

# Test the implementation
cost, path = uniform_cost_search(graph, 'A', 'G')
print(f"Cost and Path: ({cost}, {path})")