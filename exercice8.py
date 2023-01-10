from random import randint
from classe_noeud import *
from representation_arbre import *

def peigne_gauche(h):
    a = Noeud(randint(1,100))
    for i in range(h-1):
        a.ajoute_gauche(randint(1,100))
    return a


def est_peigne_gauche(arbre):
    if arbre.droit is None:
        pass

p = peigne_gauche(4)
repr_graph(p)