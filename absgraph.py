from hippocluster.algorithms.hippocluster import Hippocluster
from hippocluster.graphs.abstract import RandomWalkGraph
from environment import RandomWalkEnvironment
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import random


class AbstractedGraph:

    def get_higher_nodes(self, node_num, cur_layer, to_layer) -> list:
        
        pointsfinal = []
        points={node for node, cluster in self.assignmentslist[cur_layer].items() if cluster == node_num}
        if ( cur_layer > to_layer ):
            for point in points:
                pointsfinal += (self.get_higher_nodes(point, cur_layer-1, to_layer))
        else:
            pointsfinal = points
        return pointsfinal
        
    def __init__(self, graph, iterations):
    
        self.colors = np.random.rand(100, 3)
        
        num = iterations
        self.n_panels = 2
        self.graphs = []
        self.assignmentslist = []
        self.nclusters = 16
        self.graphs.insert(0,graph)
        

        for count in range(num):
            # instantiate Hippocluster object
            hippocluster = Hippocluster(
                n_clusters=self.nclusters,
                drop_threshold=0.001
            )
        
            for step in range(1000):

                # get a batch of random walks
                walks = [
                    set(graph.unweighted_random_walk(length=random.randint(int(self.nclusters/2) + 2, self.nclusters+2)))
                    for _ in range(self.nclusters*5 if step == 0 else self.nclusters)
                ]
           
                
                # update the clustering
                hippocluster.update(walks)
                assignments = hippocluster.get_assignments(graph)
                
            print("inserting assignment at %d" % count)
            self.assignmentslist.insert(count,assignments)
     
            newG = nx.Graph()
            for nodenum in set(assignments.values()):
                newG.add_node(nodenum)

            for edge in graph.G.edges:
                cluster1 = assignments.get(edge[0])
                cluster2 = assignments.get(edge[1])
                if(cluster1 != cluster2):
                    newG.add_edge(cluster1, cluster2, weight = 0)
                    test = newG[cluster1][cluster2]['weight']
                    newG[cluster1][cluster2]['weight'] = test + 1
            
            print("inserting graph at %d" % count)
            self.graphs.insert(count+1, newG)
            
            self.nclusters = int(len(set(assignments.values()))/2)
            graph = RandomWalkGraph(newG)
            
    def printgraph(self, g1):
        plt.subplot(1, 1, 1)
        
        
        
        if type(self.graphs[g1]) is RandomWalkEnvironment:
            self.graphs[g1].plot(node_colors={node: self.colors[cluster][::-1] for node, cluster in self.assignmentslist[g1].items()})
            
        else:
            node_colors={node: self.colors[node][::-1] for node in self.graphs[g1].nodes}
            nx.draw(self.graphs[g1], with_labels=False,
            node_color=[node_colors.get(node, [0, 0, 0]) for node in self.graphs[g1]],
            node_size=400)
        
        plt.show()  

    def printgraphs(self, g1, g2):
        plt.clf()
        
        plt.subplot(1, 2, 2)
    
        node_colors={node: self.colors[node][::-1] for node in self.graphs[g2].nodes}
        
        nx.draw(self.graphs[g2], with_labels=False,
        node_color=[node_colors.get(node, [0, 0, 0]) for node in self.graphs[g2]],
        node_size=400)

        testcolors={}
            
        for node in self.graphs[g2]:
            for parent in self.get_higher_nodes(node, g2-1, g1):
                #print(parent)
                testcolors[parent] = self.colors[node][::-1]
        
       
        
        plt.subplot(1, 2, 1)
         
        if type(self.graphs[g1]) is RandomWalkGraph:
            nx.draw(self.graphs[g1].G, with_labels=False,pos=nx.get_node_attributes(self.graphs[g1].G,'pos'),
            node_color=[testcolors.get(node, [0, 0, 0]) for node in self.graphs[g1].G],
            node_size=50)
        else:
            nx.draw(self.graphs[g1], with_labels=False,
            node_color=[testcolors.get(node, [0, 0, 0]) for node in self.graphs[g1]],
            node_size=400)
        
        plt.show()
