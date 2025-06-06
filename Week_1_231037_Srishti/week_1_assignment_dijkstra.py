import networkx as nx
import matplotlib.pyplot as plt
import time
import random
#code for dijkstra algo
def dijkstra_shortest_path(graph, source, target):
    try:
        path = nx.dijkstra_path(graph, source, target, weight='weight')
        distance = nx.dijkstra_path_length(graph, source, target, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, float('inf')
    
# A* heuristic function
def class_based_heuristic(n1, n2):
    if node_classes[n1] == node_classes[n2]:
        return 0
    else:
        return 5


#creating nodes
G = nx.Graph()

#  Step 1: Enter number of nodes and take node names
n = int(input("Enter number of nodes: "))
nodes = []

for i in range(n):
    node = input(f"Enter name of node {i+1}: ")
    nodes.append(node)


G.add_nodes_from(nodes)
# defining node classes
node_classes = {}

print("\nNow enter class for each node:")
for node in nodes:
    cls = input(f"Enter class for node '{node}': ")
    node_classes[node] = cls
      
e = int(input("Enter number of edges: "))
edges = []

for i in range(e):
    u = input(f"Enter start_node of edge {i+1}: ")
    v = input(f"Enter end_node of edge {i+1}: ")
    w = float(input(f"Enter weight({u},{v}):"))
    edges.append((u, v, {'weight':w}))

G.add_edges_from(edges)      





# shortest friendship effort of 5 randomly selected nodes

if len(nodes) >= 5:
    random_nodes = random.sample(nodes, 5)
    print("\nRandomly selected 5 nodes:", random_nodes)

    print("\nShortest paths between the selected 5 nodes using Dijkstra's Algorithm:\n")
    for i in range(len(random_nodes)):
        for j in range(i + 1, len(random_nodes)):
            source = random_nodes[i]
            target = random_nodes[j]
            path, distance = dijkstra_shortest_path(G, source, target)
            if path:
                print(f"{source} ➜ {target}: Path = {path}, Distance = {distance}")
            else:
                print(f"{source} ➜ {target}: No path exists.")
else:
    print("\nNot enough nodes to select 5.")


#applying A*
# Apply A* to first pair only (for demo)
source = random_nodes[0]
target = random_nodes[1]
print(f"\nApplying A* from {source} ➜ {target} with class-based heuristic:")

try:
    path_astar = nx.astar_path(G, source, target, heuristic=class_based_heuristic, weight='weight')
    length_astar = nx.astar_path_length(G, source, target, heuristic=class_based_heuristic, weight='weight')
    print(f"A* Path = {path_astar}, Distance = {length_astar}")
except nx.NetworkXNoPath:
    print("No path exists between the selected pair.")

# Draw the graph
pos = nx.spring_layout(G,weight='weight')
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12)
plt.show(block=False)
time.sleep(0.5)

input("Press Enter to close the graph...")

