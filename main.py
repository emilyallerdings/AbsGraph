from table_conversion import t_table_to_graph
from absgraph import AbstractedGraph
import pickle

with open("t_walls_grid_world.p", "rb") as f:
    T = pickle.load(f)

G = t_table_to_graph(
    T=T,
    pos_calculator=lambda state: (state[0], state[1])
)

absgraph = AbstractedGraph(G,3, T)
print(absgraph.get_lower_abstraction_nodes(1,3,2))