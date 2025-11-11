import networkx as nx
from collections import deque

# --- Input the graph ---
edges = []
print("Enter edges (e.g., A B). Type 'done' when finished:")
while True:
    e = input()
    if e.lower() == 'done':
        break
    a, b = e.split()
    edges.append((a, b))

G = nx.Graph()
G.add_edges_from(edges)

# --- Take start and goal nodes ---
start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

# --- BFS Implementation ---
visited = set()
queue = deque([[start]])
found_path = None

while queue:
    path = queue.popleft()
    node = path[-1]
    if node == goal:
        found_path = path
        break
    if node not in visited:
        for neighbor in G.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
        visited.add(node)

# --- Print the result ---
if found_path:
    print("Path found:", " -> ".join(found_path))
else:
    print("No path found.")