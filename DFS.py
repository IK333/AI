import networkx as nx
import matplotlib.pyplot as plt

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

# --- Draw the graph and highlight the found path ---
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, width=2)

if found_path:
    path_edges = list(zip(found_path, found_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=found_path, node_color='orange', node_size=900)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("DFS Traversal and Found Path")
plt.show()
