from representation_arbre import *
from classe_noeud import Noeud

def parfait(num):
    from random import randint
    if num == 0 :
        return None
    else:
        x = Noeud(randint(1,1000))
        x.gauche = parfait(num-1)
        x.droit = parfait(num-1)
        return x
