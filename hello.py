import networkx as nx
import matplotlib.pyplot as plt
from node import *
import graph1 as g1
from graph_util import * 


plt.subplot()
G = build_G(g1.couches)
print(G.nodes['s'])
#print(G.nodes['e'])
first_flot(G, 'e')
print(G.nodes['s'])
#print(G.nodes['e'])
#print(G.edges['e', 1]['cap'])
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
