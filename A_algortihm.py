import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic (estimated distance to goal)
        self.f = 0  # Total cost = g + h

    def __lt__(self, other):
        return self.f < other.f  # Needed for priority queue ordering

def heuristic(a, b):
    """Heuristic function: Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    # Initialize start and end nodes
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    heapq.heappush(open_list, start_node)
    open_set = {start: start_node}

    closed_set = set()  

    while open_list:
        # Get node with lowest f cost
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        
        # Remove from open set
        open_set.pop(current_pos)

        # Goal reached!
        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Mark current node as visited
        closed_set.add(current_pos)

        # Explore neighbors (up, down, left, right)
        x, y = current_pos
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next_pos in neighbors:
            # Check grid boundary
            if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
                continue
            # Skip obstacles or visited
            if grid[next_pos[0]][next_pos[1]] == 1 or next_pos in closed_set:
                continue

            # Create neighbor node
            neighbor = Node(next_pos, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(next_pos, end)
            neighbor.f = neighbor.g + neighbor.h

            # If neighbor already in open set with lower f, skip it
            if next_pos in open_set and open_set[next_pos].f <= neighbor.f:
                continue

            heapq.heappush(open_list, neighbor)
            open_set[next_pos] = neighbor

    return None  # No path found

# ------------- Test the function -------------------

# Grid definition: 0 = free path, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)

path = astar(grid, start, end)

if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
