import networkx as nx
import matplotlib.pyplot as plt
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

# --- Draw the graph and highlight the found path ---
pos = nx.spring_layout(G)  # layout for positioning
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, width=2)

if found_path:
    # Highlight the found path in red
    path_edges = list(zip(found_path, found_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=found_path, node_color='orange', node_size=900)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("BFS Traversal and Found Path")
plt.show()
