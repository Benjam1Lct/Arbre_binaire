import networkx as nx
import matplotlib.pyplot as plt

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))
    
def parcours(arbre, valeurs, branches, position, profondeur, pos_courante):
    if arbre is not None:
        valeurs.append(arbre.valeur) # on complète la liste des valeurs
        position[arbre.valeur] = (pos_courante,profondeur)     # ... et la liste des positions
        profondeur -= 1 
        if arbre.gauche is not None:
            branches.append((arbre.valeur, arbre.gauche.valeur))  #... et la liste des branches
            parcours(arbre.gauche, valeurs, branches, position, profondeur, 
                    pos_courante - 2**(profondeur - 1))
        if arbre.droit is not None:
            branches.append((arbre.valeur, arbre.droit.valeur))
            parcours(arbre.droit, valeurs, branches, position, profondeur, 
                    pos_courante + 2**(profondeur - 1))
    return valeurs, branches, position 


def repr_graph(arbre):
    valeurs = []    #liste des valeurs, racines et feuilles de l'arbre
    branches =[]    # liste des branches de l'arbre
    profond = hauteur(arbre)    #hauteur de l'arbre
    pos_courante = 2**(profond - 1)   # position de la racine (en abscisse)
    position = {}                # dictionnaire des positions des valeurs sur la figure
     
    # appel d'une fonction récursive de parcours, ici prefixe mais ça n'a pas d'importance
    # on récupère : la liste des valeurs, la liste des branches,
    # le dictionnaire des positions des valeurs
    valeurs, branche, position  = parcours(arbre, valeurs, branches, position, profond, pos_courante)    
    #print(position)

    mon_arbre = nx.Graph()          # objet Graphe de la bibliothèque Networkxx
    mon_arbre.add_nodes_from(valeurs)
    mon_arbre.add_edges_from(branches)
    #print(list(arbre.nodes))
    #print(list(arbre.edges))
    options = {
        "font_size": 12,
        "node_size": 300,
        "node_color": "skyblue",
        "edge_color" : "royalblue",
        "edgecolors": "forestgreen",
        "linewidths": 1,
        "width": 2,
    }
    nx.draw_networkx(mon_arbre, pos = position, **options)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    return(mon_arbre)      #on renvoie l'objet graphe networkxx au cas où
