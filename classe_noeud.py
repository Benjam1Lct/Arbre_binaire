from representation_arbre import *
from random import randint

class Noeud:
    """un noeud d'un arbre binaire"""
    def __init__(self, valeur = None):
        self.valeur = valeur
        self.gauche = None
        self.droit  = None

    def ajoute_gauche(self, valeur):
        if self.valeur == None:
            self.valeur = valeur
        elif self.gauche is None:
            self.gauche = Noeud(valeur)
        else:
            self.gauche.ajoute_gauche(valeur)
            
    def ajoute_droit(self, valeur):
        if self.valeur == None:
            self.valeur = valeur
        elif self.droit is None:
            self.droit = Noeud(valeur)
        else:
            self.droit.ajoute_droit(valeur)

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.gauche

    def get_droit(self):
        return self.droit
    
    def __eq__(self,other):
        if type(self) is not int:
            if self.valeur() == other.valeur() and self.gauche() == other.gauche() and self.droit() == other.droit():
                return True
            else:
                return False
    
    def get_taille(self):
        tg = self.gauche.get_taille() if self.gauche else 0
        td = self.droit.get_taille() if self.droit else 0
        return 1 + tg + td

    def get_hauteur(self):
        if self is None:
            return 0
        else:
            return 1 + max(self.gauche.get_hauteur() if self.gauche else 0, self.droit.get_hauteur() if self.droit else 0)


def parfait(num):
    from random import randint
    if num == 0 :
        return None
    else:
        x = Noeud(randint(1,1000))
        x.gauche = parfait(num-1)
        x.droit = parfait(num-1)
        return x
    
if __name__ == '__main__':
    x = parfait(4)

    a = Noeud(2)
    a.ajoute_droit(4)
    a.ajoute_droit(14)
    a.ajoute_droit(7)
    a.ajoute_gauche(28)
    a.ajoute_gauche(23)
    a.ajoute_gauche(16)

    b = Noeud(12)
    b.ajoute_droit(15)
    b.ajoute_droit(14)
    b.ajoute_droit(17)
    b.ajoute_gauche(8)
    b.ajoute_gauche(6)
    """def affiche(T):
        if T != None:
            return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))"""
    print(x.get_hauteur())
    print(x.get_taille())
    repr_graph(x)
