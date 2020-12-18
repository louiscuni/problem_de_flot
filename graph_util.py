import networkx as nx

def build_G(couche):#construit un graphe a partir d'une liste de dico
    G = nx.DiGraph()
    for c in couche:
        for node in c.keys():
            G.add_node(node, marque='.', marque_suc=None, flot=0)

    for c in couche:
        for node in c.keys():
            if c[node]:
                for voisin in c[node]:
                    G.add_edge(node, voisin[0], cap=voisin[1], flot=0)

    return G

def first_chain(G, node):#trouver une premiere chaine augmentante
    if 's' in list(list(G.successors(node))) :
        return  [node, 's']
    else :
        return [node] + first_chain(G, list(G.successors(node))[0])

# def cap_min_chain(G, chaine):#trouve la capacite min d'une chaine
#     cap_min = 100000
#     for i in range(len(chaine)-1) :
#         if cap_min > G.edges[chaine[i], chaine[i+1]]['cap']:
#             cap_min = G.edges[chaine[i], chaine[i+1]]['cap']
#     return cap_min

def value_change_flot(G, chaine):#trouve la valeur d'augmentation de flot max dans une chaine
    val_plus = 100000
    val_moins = 100000
    for i in range(len(chaine)-1) :
        if G.edges[chaine[i], chaine[i+1]]:#test de l'existence de l'arete -> si elle n'existe pas, sont inverse doit l'etre
            if val_plus > G.edges[chaine[i], chaine[i+1]]['cap'] - G.edges[chaine[i], chaine[i+1]]['flot']:#recherche la valeur du flot residuel minimum
                val_plus = G.edges[chaine[i], chaine[i+1]]['cap'] - G.edges[chaine[i], chaine[i+1]]['flot']
        else :
            if val_moins > G.edges[chaine[i+1], chaine[i]]['flot']:#recherche de la valeur de reserve de flot minimum
                val_moins = G.edges[chaine[i+1], chaine[i]]['flot']
    return min(val_moins, val_plus)

# def changement_flot(G, chaine, val):#augmente le flot d'une chaine de la valeur val
#     for i in range(len(chaine)-1) :
#         G.edges[chaine[i], chaine[i+1]]['flot'] += val

def procedure_changement_flot(G, chaine, val):
    for i in range(len(chaine)-1) :
        if G.edges[chaine[i], chaine[i+1]]:
            G.edges[chaine[i], chaine[i+1]]['flot'] += val
        else :
            G.edges[chaine[i+1], chaine[i]] -= val

def update_s_value(G):
    pred = list(G.predecessors('s'))
    res = 0
    for i in pred:
        res += G.edges[i, 's']['flot']
    G.nodes['s']['flot'] = res

def first_flot(G, node):#construit un premier flot naif
    chain = first_chain(G, node)
    print(chain)
    valeur_flot = value_change_flot(G, chain)
    procedure_changement_flot(G, chain, valeur_flot)
    update_s_value(G)

def procedure_marquage(G):
    G.nodes['e']['marque'] = '+'
    list_todo = list(G.nodes)
    marque_plus(G, 'e')
    for node in list_todo:
        marque_plus(G, node)
        marque_moins(G, node)
        

def marque_plus(G, node):
    if G.nodes[node]['marque'] != '.':
        successors = list(G.successors(node))
        for s in successors:
            if G.nodes[s]['marque'] == '.' and G.edges[node, s]['flot'] < G.edges[node, s]['cap']:
                G.nodes[s]['marque'] = '+'
                G.nodes[s]['marque_suc'] = node
                print(s, ' est marque +')

def marque_moins(G, node):
     if G.nodes[node]['marque'] != '.':
        predecessors = list(G.predecessors(node))
        for p in predecessors:
            if G.nodes[p]['marque'] == '.' and G.edges[p, node]['flot'] > 0:
                G.nodes[p]['marque'] = '-'
                G.nodes[p]['marque_suc'] = node
                print(p, ' est marque -')

def flush_marque(G):
    for node in list(G.nodes):
        G.nodes[node]['marque'] = '.'

def chaine_augmentante(G, node):#construit la chaine allant de 'e' à node permettant d'augmenter le flot
#appeler que si 's' est marque '+'
    if node == 'e':
        return ['e']
    else:
        return chaine_augmentante(G, G.nodes[node]['marque_suc']) + [node] 

def Ford_Ferkuson(G):
    first_flot(G, 'e')
    procedure_marquage(G)
    while(G.nodes['s']['marque'] == '+'):
        chaine = chaine_augmentante(G, 's')
        v = value_change_flot(G, chaine)
        procedure_changement_flot(G, chaine, v)
        flush_marque(G)
        procedure_marquage(G)
    update_s_value(G)
    print(G.nodes['s'])