
from environment import RandomWalkEnvironment
from absgraph import AbstractedGraph


graph = RandomWalkEnvironment()

absgraph = AbstractedGraph(graph, 1)

absgraph.printgraphs(0,1)