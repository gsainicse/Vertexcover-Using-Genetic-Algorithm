from networkx.algorithms import approximation
import networkx as nx
G = nx.Graph()
G = nx.gnm_random_graph(500,700)
print(G.nodes)
print(G.edges)
print(len(G.nodes), len(G.edges))
print("using networkx approximation algorithms :", end=" ")
print(len(approximation.min_weighted_vertex_cover(G)))