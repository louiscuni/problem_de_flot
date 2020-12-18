import networkx as nx

def build_G(couche):
    G = nx.DiGraph()
    for c in couche:
        for node in c.keys():
            G.add_node(node, marque='.', chaine=[], flot=0)

    for c in couche:
        for node in c.keys():
            if c[node]:
                for voisin in c[node]:
                    G.add_edge(node, voisin[0], cap=voisin[1], flot=0)

    return G

def first_chain(G, node):
    #trouver un premier flot
    if 's' in list(list(G.successors(node))) :
        return  [node, 's']
    else :
        return [node] + first_chain(G, list(G.successors(node))[0])

def cap_min_chain(G, chaine):
    cap_min = 100000
    for i in range(len(chaine)-1) :
        if cap_min > G.edges[chaine[i], chaine[i+1]]['cap']:
            cap_min = G.edges[chaine[i], chaine[i+1]]['cap']
    return cap_min

def changement_flot(G, chaine, val):
    for i in range(len(chaine)-1) :
        G.edges[chaine[i], chaine[i+1]]['flot'] += val

def update_s_value(G):
    pred = list(G.predecessors('s'))
    res = 0
    for i in pred:
        res += G.edges[i, 's']['flot']
    G.nodes['s']['flot'] = res

def first_flot(G, node):
    chain = first_chain(G, node)
    print(chain)
    valeur_flot = cap_min_chain(G, chain)
    changement_flot(G, chain, valeur_flot)
    update_s_value(G)