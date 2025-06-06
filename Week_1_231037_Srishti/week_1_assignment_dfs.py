import networkx as nx
import matplotlib.pyplot as plt
import time
import random

# dfs code
def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)
# code for a friend group
def dfs_collect(node, visited, graph, group):
    visited[node] = True
    group.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_collect(neighbor, visited, graph, group)

#code for no.of connected components
def find_connected_components(graph):
    visited =  {node: False for node in graph}
    components = 0
    for node in graph:
        if not visited[node]:
            dfs(node, visited, graph)
            components += 1
    return components

#defining graph
G = nx.Graph()

#  Step 1: Enter number of nodes and take node names
n = int(input("Enter number of nodes: "))
nodes = []

for i in range(n):
    node = input(f"Enter name of node {i+1}: ")
    nodes.append(node)

G.add_nodes_from(nodes)

#  Step 2: Enter number of edges and take edge pairs
e = int(input("Enter number of edges: "))
edges = []

for i in range(e):
    u = input(f"Enter start_node of edge {i+1}: ")
    v = input(f"Enter end_node of edge {i+1}: ")
    w = float(input(f"Enter weight({u},{v}):"))
    edges.append((u, v, {'weight':w}))

G.add_edges_from(edges)


#  Step 3: Draw the graph
pos = nx.spring_layout(G,weight='weight')
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12)
plt.show(block=False)
time.sleep(0.5)


# no. of components
num_components = find_connected_components(G.adj)


visited = {node: False for node in G}
Friends_group = []

for node in G:
    if not visited[node]:
        group = []
        dfs_collect(node, visited, G.adj, group)
        Friends_group.append(group)
print(f"Number of Friends group :{len(Friends_group)}")

#number of people in the friends group and names of the people
for i, group in enumerate(Friends_group):
    print(f"Friends group {i+1}: {group}")
    print(f"    Size of group = {len(group)}")

#group with max and min people
    sizes = [len(group) for group in Friends_group]
max_size = max(sizes)
min_size = min(sizes)

print(f"\nMaximum size of a friends group: {max_size}")
print(f"Minimum size of a friends group: {min_size}")

# code for output and graph pop up at same time
input("Press Enter to close the graph...")


