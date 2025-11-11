import networkx as nx
import heapq

# --- Input graph edges ---
edges = []
print("Enter edges (e.g., A B cost). Type 'done' when finished:")
while True:
    e = input()
    if e.lower() == 'done':
        break
    a, b, c = e.split()
    edges.append((a, b, float(c)))  # cost is used for display

G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- Take heuristic values ---
heuristic = {}
print("\nEnter heuristic values (e.g., A 6). Type 'done' when finished:")
while True:
    h = input()
    if h.lower() == 'done':
        break
    n, val = h.split()
    heuristic[n] = float(val)

# --- Take start and goal ---
start = input("\nEnter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# --- Greedy Best First Search ---
open_list = []
heapq.heappush(open_list, (heuristic.get(start, float('inf')), [start]))
visited = set()
found_path = None

while open_list:
    f, path = heapq.heappop(open_list)
    node = path[-1]
    if node == goal:
        found_path = path
        break
    if node not in visited:
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(open_list, (heuristic.get(neighbor, float('inf')), new_path))

# --- Print result ---
if found_path:
    print("\nPath found (Greedy Best First Search):", " -> ".join(found_path))
else:
    print("\nNo path found.")