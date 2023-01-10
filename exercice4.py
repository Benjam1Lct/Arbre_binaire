from representation_arbre import *
from classe_noeud import Noeud
from random import randint

def parfait(h):
    random_num = randint(1,100)
    if h == 0 :
        return None
    else:
        x = Noeud(random_num)
        x.gauche = parfait(h-1)
        x.droit = parfait(h-1)
        return x

p = parfait(1)
print(p.valeur)
repr_graph(p)