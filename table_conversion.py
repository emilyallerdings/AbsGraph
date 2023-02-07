from tables import TTable
import networkx as nx
from hippocluster.graphs.abstract import RandomWalkGraph


def t_table_to_graph(T: TTable, pos_calculator: callable = None):
    """
    convert a T table (from a model-based RL agent) to a directed graph suitable for random walk generation
    :param T: the TTable object
    :param pos_calculator: optional callable that returns (x,y) coordinates for plotting given a state
    :return a networkx DiGraph object with a node for each state in the T table, and directed edges with weights
    representing the probability that a random action will cause that transition
    """

    G = nx.DiGraph()
    all_states = T.get_all_states()

    for state in all_states:
        for state2, weight in T.get_random_transition_probabilities_from(state).items():
            G.add_edge(state, state2, weight=weight)

    if callable(pos_calculator):
        for state in all_states:
            G.nodes[state]['pos'] = pos_calculator(state)

    return RandomWalkGraph(G)
