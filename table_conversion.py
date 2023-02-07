from tables import TTable
import networkx as nx
from hippocluster.graphs.abstract import RandomWalkGraph


def t_table_to_graph(T: TTable, pos_calculator: callable = None):

    G = nx.DiGraph()
    all_states = T.get_all_states()

    for state in all_states:
        for state2, weight in T.get_random_transition_probabilities_from(state).items():
            G.add_edge(state, state2, weight=weight)

    if callable(pos_calculator):
        for state in all_states:
            G.nodes[state]['pos'] = pos_calculator(state)

    return RandomWalkGraph(G)
