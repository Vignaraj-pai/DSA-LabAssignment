import random
import imageio
import networkx as nx
import matplotlib.pyplot as plt

#take number of nodes as input
n = int(input("Enter number of nodes: "))

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

G.add_edges_from(edge_list)
edges = list(G.edges())
weights = nx.get_edge_attributes(G, "weight")
color_map = ['#eee' for node in G.nodes()]
alphas = [1 for edge in edges]
colors = ['black' for edge in edges]
pos = nx.spring_layout(G)
nx.draw_networkx(G, node_color = color_map, with_labels = True,pos=pos , edge_color = colors, width = alphas)
plt.savefig('dfs_images/dfs0.png')
plt.clf()

main_visited = [False] * len(adj_list)

count = 0
# recursive dfs function
def dfs(adj_list, start, visited):
    global count
    global pos
    visited[start] = True
    color_map[list(G.nodes).index(start)] = '#999'
    nx.draw_networkx(G, node_color = color_map, with_labels = True,pos=pos , edge_color = colors, width = alphas)
    plt.savefig(f'dfs_images/dfs{count}'+'.png')
    count = count + 1
    plt.clf()
    print(start, end = " -> ")
    for i in adj_list[start]:
        if visited[i] == False:
            colors[edges.index((start, i))] = '#f00'
            alphas[edges.index((start, i))] = 3
            nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
            plt.savefig(f'dfs_images/dfs{count}.png')
            plt.clf()
            count = count +1
            color_map[list(G.nodes).index(i)] = '#999'
            nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
            plt.savefig(f'dfs_images/dfs{count}.png')
            plt.clf()
            count = count +1
            colors[edges.index((start, i))] = 'black'
            alphas[edges.index((start, i))] = 1
            nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
            plt.savefig(f'dfs_images/dfs{count}.png')
            plt.clf()
            count = count +1
            dfs(adj_list, i, visited)
    color_map[list(G.nodes).index(start)] = '#222'
    nx.draw_networkx(G, node_color = color_map, with_labels = True, pos = pos, edge_color = colors, width = alphas)
    plt.savefig(f'dfs_images/dfs{count}.png')
    count = count +1
    

# call dfs function
print("DFS traversal:")
for i in range(n):
    if main_visited[i] == False:
        dfs(adj_list, i, main_visited)
        print("END")
        
frames = []
for t in range(count):
    image = imageio.v2.imread(f'dfs_images/dfs{t}.png')
    frames.append(image)
    
imageio.mimsave('./dfs.gif', # output gif
                frames,          # array of input frames
                fps = 2)   



