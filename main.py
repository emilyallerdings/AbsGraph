from hippocluster.graphs.lattice import RandomWalkLattice
from hippocluster.graphs.environment import RandomWalkEnvironment
from hippocluster.algorithms.hippocluster import Hippocluster
from hippocluster.graphs.abstract import RandomWalkGraph
from hippocluster.graphs.absgraph import AbstractedGraph


graph = RandomWalkEnvironment()

absgraph = AbstractedGraph(graph, 1)

absgraph.printgraph()