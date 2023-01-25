
from hippocluster.graphs.environment import RandomWalkEnvironment
from absgraph import AbstractedGraph


graph = RandomWalkEnvironment()

absgraph = AbstractedGraph(graph, 4)

absgraph.printgraphs(1,3)