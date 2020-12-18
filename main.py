import networkx as nx
import matplotlib.pyplot as plt
import graph1 as g1
from graph_util import * 


plt.subplot()
G = build_G(g1.couches)
Ford_Ferkuson(G)
#print(G.nodes['e'])
#print(G.edges['e', 1]['cap'])
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
