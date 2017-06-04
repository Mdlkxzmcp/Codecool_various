# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

######## Creating and manipulating a Graph

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(['u', 'v'])
print("Nodes in G state 1:", G.nodes())
G.add_edge(1, 2)
G.add_edge('u', 'v')
G.add_edges_from([(1, 3), (1, 4), (1, 5), (1, 6)])
G.add_edge('u', 'w')
print("Edges in G state 2:", G.edges())
G.remove_node(2)
print("Nodes in G state 3:", G.nodes())
G.remove_nodes_from([4, 5])
print("Nodes in G state 4:", G.nodes())
G.remove_edge(1, 3)
print("Edges in G state 5:", G.edges())
G.remove_edges_from([(1, 2), ('u', 'v')])
print("Edges in G state 6:", G.edges())
print("Number of nodes in G state 6: ", G.number_of_nodes())
print("Number of edges in G state 6: ", G.number_of_edges())

######## Graph visualization

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
# plt.savefig("karate_graph.pdf")
print(G.degree())
print(G.degree(0) is G.degree()[0])

######## random graphs and general randomness

print(bernoulli.rvs(p=0.2))

N = 20
p = 0.2


def er_graph(N, p=0.2):
    """Generate an ER graph."""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G


def draw_custom_er_graph(N, p=0.2, node_size=40,
                         node_color="lightblue", edge_color="grey"):
    return nx.draw(er_graph(N, p), node_size=node_size,
                   node_color=node_color, edge_color=edge_color)

draw_custom_er_graph(50, 0.08)
# plt.savefig("er1.pdf")

######## plotting the degree distribution


def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
# plt.savefig("hist2.pdf")

######## "Descriptive Statistics of Empirical Social Networks"

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Average degree: {:.2f}".format(np.mean(list(G.degree().values()))))

plot_degree_distribution(G1)
plot_degree_distribution(G2)
# plt.savefig("village_hist.pdf")

######## largest connected component in a network

gen_1 = nx.connected_component_subgraphs(G1)
g1 = gen_1.__next__()

print(g1.number_of_nodes())
print(len(gen_1.__next__()))
print(len(G1))
print(G1.number_of_nodes)

# Largest Connected Component
G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)

print(G1_LCC.number_of_nodes() / G1.number_of_nodes())
print(G2_LCC.number_of_nodes() / G2.number_of_nodes())

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")

######## From DataCamp

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties, num_ties = 0, 0
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 > n2:
                if IDs[n1] in chars and IDs[n2] in chars:
                    if G.has_edge(n1, n2):
                        num_ties += 1
                        if chars[IDs[n1]] == chars[IDs[n2]]:
                            num_same_ties += 1
    return (num_same_ties / num_ties)
    