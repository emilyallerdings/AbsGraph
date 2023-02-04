import networkx as nx
import matplotlib.pyplot as plt
from environment import RandomWalkEnvironment
from hippocluster.graphs.abstract import RandomWalkGraph
from absgraph import AbstractedGraph
import tables
import pickle

def add_edge_to_graph(G, e1, e2):
    G.add_edge(e1, e2)

points = []
edges = []  # todo: is this list used?
T = tables.TTable()
T = pickle.load( open( "t_walls_grid_world.p", "rb" ) )
G = nx.Graph()

# todo: converting the T table to a graph this way is smart, but we should find a way to use the T-table probabilities as edge weights for the new graph (I can help with that)
for state in T.get_all_states():

    for state2 in T.get_states_accessible_from(state):
        if (edges.count((state, state2)) == 0 and state != state2):
            add_edge_to_graph(G, state, state2,)

for point in G.nodes():
    G.add_node(point, pos = (point[0], -point[1]))

absgraph = AbstractedGraph(RandomWalkGraph(G),1)
absgraph.printgraphs(0,1)