import networkx as nx

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

# --- DFS Implementation (no functions) ---
stack = [[start]]
visited = set()
found_path = None

while stack:
    path = stack.pop()
    node = path[-1]
    if node == goal:
        found_path = path
        break
    if node not in visited:
        visited.add(node)
        for neighbor in reversed(list(G.neighbors(node))):  # reverse to keep consistent order
            new_path = list(path)
            new_path.append(neighbor)
            stack.append(new_path)

# --- Print the result ---
if found_path:
    print("Path found:", " -> ".join(found_path))
else:
    print("No path found.")