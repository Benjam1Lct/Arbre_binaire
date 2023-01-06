import networkx as nx
import matplotlib.pyplot as plt

class ArbreB:
    def __init__(self, valeur, gauche = None, droit = None):
        self.noeud = valeur
        self.gauche = gauche
        self.droit = droit
    def __repr__(self):
        return str(self.noeud) +str(self.gauche).replace('None','.')+str(self.droit).replace('None','.')
    
arbre_f = ArbreB('f')
arbre_g = ArbreB('g')
arbre_c = ArbreB('c',arbre_f,arbre_g)
arbre_h = ArbreB('h')
arbre_i = ArbreB('i')
arbre_j = ArbreB('j')
arbre_d = ArbreB('d',arbre_h,arbre_i)
arbre_e = ArbreB('e',arbre_j)
arbre_b = ArbreB('b',arbre_d,arbre_e)
arbre_a = ArbreB('a',arbre_b,arbre_c)
print(arbre_a)

# utilitaire pour représenter les arbres binaires

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))
    
def parkour(arbre, noeuds, branches, position, profondeur, pos_courante):
    if arbre is not None:
        noeuds.append(arbre.noeud)            # on complète la liste des noeuds
        position[arbre.noeud] = (pos_courante,profondeur)     # ... et la liste des positions
        profondeur -= 1 
        if arbre.gauche is not None:
            branches.append((arbre.noeud, arbre.gauche.noeud))  #... et la liste des branches
            parkour(arbre.gauche, noeuds, branches, position, profondeur, 
                    pos_courante - 2**(profondeur - 1))
        if arbre.droit is not None:
            branches.append((arbre.noeud, arbre.droit.noeud))
            parkour(arbre.droit, noeuds, branches, position, profondeur, 
                    pos_courante + 2**(profondeur - 1))
    return noeuds, branches, position 


def repr_graph(arbre):
    noeuds = []             #liste des noeuds, racines et feuilles de l'arbre
    branches =[]            # liste des branches de l'arbre
    profond = hauteur(arbre_a)        #hauteur de l'arbre
    pos_courante = 2**(profond - 1)   # position de la racine (en abscisse)
    position = {}                # dictionnaire des positions des noeuds sur la figure
     
    # appel d'une fonction récursive de parcours, ici prefixe mais ça n'a pas d'importance
    # on récupère : la liste des noeuds, la liste des branches,
    # le dictionnaire des positions des noeuds
    noeuds, branche, position  = parkour(arbre, noeuds, branches, position, profond, pos_courante)    
    #print(position)

    mon_arbre = nx.Graph()          # objet Graphe de la bibliothèque Networkxx
    mon_arbre.add_nodes_from(noeuds)
    mon_arbre.add_edges_from(branches)
    #print(list(arbre.nodes))
    #print(list(arbre.edges))
    options = {
        "font_size": 12,
        "node_size": 300,
        "node_color": "white",
        "edge_color" : "green",
        "edgecolors": "blue",
        "linewidths": 1,
        "width": 2,
    }
    nx.draw_networkx(mon_arbre, pos = position, **options)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    return(mon_arbre)      #on renvoie l'objet graphe networkxx au cas où


arbre = repr_graph(arbre_a)
