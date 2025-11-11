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
    edges.append((a, b, float(c)))

# Create undirected weighted graph
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

# --- Start and goal nodes ---
start = input("\nEnter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# --- A* Search Implementation ---
open_list = []
heapq.heappush(open_list, (heuristic.get(start, float('inf')), [start]))  # f = g + h, here g=0 at start
g_cost = {start: 0}
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
            cost = g_cost[node] + G[node][neighbor]['weight']
            if cost < g_cost.get(neighbor, float('inf')):  # found a better path
                g_cost[neighbor] = cost
                f_val = cost + heuristic.get(neighbor, float('inf'))  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (f_val, path + [neighbor]))

# --- Compute total cost of found path ---
if found_path:
    total_cost = sum(G[found_path[i]][found_path[i + 1]]['weight'] for i in range(len(found_path) - 1))
    print("\nPath found (A*):", " -> ".join(found_path))
    print("Total path cost (g):", total_cost)
else:
    print("\nNo path found.")