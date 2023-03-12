
import random
import imageio
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# create a directory to store images
if not os.path.exists('bfs_images'):
    os.makedirs('bfs_images')


#take number of nodes as input
n = int(input("Enter number of nodes: "))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# randomly generate adjacency list as a dictionary
adj_list = {}
for i in range(n):
    adj_list[i] = []
    for j in range(n):
        if i != j and random.randint(0, 1):
            adj_list[i].append(j)

# print adjacency list
print("Adjacency list:")
for i in range(n):
    print(i, "->", adj_list[i])


# print adjacency matrix
print("Adjacency matrix:")
for i in range(n):
    for j in range(n):
        if j in adj_list[i]:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()

# create a edge list from the adjacency list
edge_list = []
for i in range(n):
    for j in adj_list[i]:
        edge_list.append((i, j))

G = nx.DiGraph()

main_visited = [False] * len(adj_list)
# bfs function
G.add_edges_from(edge_list)
edges = list(G.edges())
weights = nx.get_edge_attributes(G, "weight")
color_map = ['#eee' for node in G.nodes()]
alphas = [1 for edge in edges]
colors = ['black' for edge in edges]
pos = nx.spring_layout(G)
nx.draw_networkx(G, node_color = color_map, with_labels = True,pos=pos , edge_color = colors, width = alphas)
 
plt.savefig('bfs_images/bfs0.png')
plt.clf()

def bfs(adj_list, start):
    count = 1
    visited = [False] * len(adj_list)
    queue = []
    queue.append(start)
    visited[start] = True
    main_visited[start] = True
    while queue:
        s = queue.pop(0)
        color_map[list(G.nodes).index(s)] = '#999'
        nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
         
        plt.savefig(f'bfs_images/bfs{count}.png')
        plt.clf()
        count = count +1
        print(s, end = " -> ")
        for i in adj_list[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                colors[edges.index((s, i))] = '#f00'
                alphas[edges.index((s, i))] = 3
                nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
                 
                plt.savefig(f'bfs_images/bfs{count}.png')
                plt.clf()
                count = count +1
                color_map[list(G.nodes).index(i)] = '#999'
                nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
                 
                plt.savefig(f'bfs_images/bfs{count}.png')
                plt.clf()
                count = count +1
                main_visited[i] = True
                colors[edges.index((s, i))] = 'black'
                alphas[edges.index((s, i))] = 1
                nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
                 
                plt.savefig(f'bfs_images/bfs{count}.png')
                plt.clf()
                count = count +1
        color_map[list(G.nodes).index(s)] = '#222'
    nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
    plt.savefig(f'bfs_images/bfs{count}.png')
    count = count +1
    plt.clf()
    print("END")
    return count;

print("BFS traversal:")


cnt = bfs(adj_list, 0)
# check if all nodes are visited
if False in main_visited:
    for i in range(len(main_visited)):
        if main_visited[i] == False:
            cnt = cnt    + bfs(adj_list, i)

frames = []
for t in range(cnt):
    image = imageio.v2.imread(f'bfs_images/bfs{t}.png')
    frames.append(image)
    
imageio.mimsave('./bfs.gif', # output gif
                frames,          # array of input frames
                fps = 2)   
