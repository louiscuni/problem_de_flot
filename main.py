import networkx as nx
import matplotlib.pyplot as plt
import graph1 as g1
import graph2 as g2
from graph_util import * 


plt.subplot()
G = build_G(g2.couches)
Ford_Ferkuson(G)
res, autre = nx.maximum_flow(G, 'e', 's')
print("resultat du package networkx")
print(res)

