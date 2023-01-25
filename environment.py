from hippocluster.graphs.abstract import RandomWalkGraph

from networkx.generators import grid_2d_graph
from networkx import planar_layout

import networkx as nx
import matplotlib.pyplot as plt
import gymnasium as gym
import minigrid

def make_env(env_key, seed=None, render_mode=None):
    env = gym.make(env_key, render_mode=render_mode)
    env.reset(seed=seed)
    return env


def add_edge_to_graph(G, e1, e2, w):
    G.add_edge(e1, e2, weight=w)

class RandomWalkEnvironment(RandomWalkGraph):

    def __init__(self):
        """
        environment to graph

        """
        self.n_clusters = 10
        #Configuration of gymnasium/minigrid environment to use
        env = make_env("MiniGrid-Custom-TestEnv")

        width = env.grid.width
        height = env.grid.height
        self.width = width
        self.height = height
        points = []
        edges = []
        
        Grid = [[0 for y in range(height)] for x in range(width)] 
        value = 0
        for x in range(width):
            for y in range(height):
                if env.grid.get(x,y) == None:
                    value = 0
                if isinstance(env.grid.get(x,y), minigrid.core.world_object.Wall):
                    value = 1
                Grid[x][y] = value
        
        for y in range(height):
            for x in range(width):
                points.append((x,y))
                
                
        for x in range(width-1):
            for y in range(height-1):
                if Grid[x][y] == 0:
                    if Grid[x+1][y] == 0:
                        edges.append((x+(width*y), x+1+(width*y), 1))
                    if Grid[x][y+1] == 0:
                        edges.append((x+(width*y), x+(width*(y+1)), 1))
                
        
        G = nx.Graph()
        for i in range(len(edges)):
            add_edge_to_graph(G, points[edges[i][0]], points[edges[i][1]], edges[i][2])

        super().__init__(G, pos={node: list(node) for node in G.nodes})

    @property
    def communities(self):
        pass

