from representation_arbre import *
from random import randint

class Noeud:
    """un noeud d'un arbre binaire"""
    def __init__(self, valeur = None):
        self.valeur = valeur
        self.gauche = None
        self.droit  = None
        self.parents = None

    

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
    
    def eq(self,other):
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

    def ABR(self, key):
        while self.valeur is not None:
            if key < self.valeur:
                if self.gauche is None:
                    return False
                self = self.gauche
            elif key > self.valeur:
                if self.droit is None:
                    return False
                self = self.droit
            else:
                return True

    def inserer(self, valeur):
        if valeur < self.valeur:
            if self.gauche == None:
                self.gauche = self.gauche.ABR(valeur)
                self.gauche.parents = self
            else:
                self.gauche.inserer(valeur)
        else:
            if self.droit == None:
                self.droit = self.droit.ABR(valeur)
                self.droit.parents = self
            else:
                self.droit.inserer(valeur)

    def enfant_gauche(self):
        return self.parents is not None and self is self.parents.gauche

    def enfant_droit(self):
        return self.parents is not None and self is self.parents.droit

    def successeur(self, noeud):
        pass

    def min(self):
        while self.valeur is not None:
            if self.gauche is None:
                return self.valeur
            self = self.gauche

    def max(self):
        while self.valeur is not None:
            if self.droit is None:
                return self.valeur
            self = self.droit


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

    a = Noeud(50)
    a.ajoute_gauche(17)
    a.ajoute_droit(72)
    a.gauche.ajoute_gauche(12)
    a.gauche.ajoute_droit(23)
    a.droit.ajoute_gauche(54)
    a.droit.ajoute_droit(76)
    a.droit.gauche.ajoute_droit(67)
    a.gauche.gauche.ajoute_gauche(9)
    a.gauche.gauche.ajoute_droit(14)
    a.gauche.droit.ajoute_gauche(19)

    b = Noeud(12)
    b.ajoute_droit(15)
    b.ajoute_droit(14)
    b.ajoute_droit(17)
    b.ajoute_gauche(8)
    b.ajoute_gauche(6)
    def affiche(T):
        if T != None:
            return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))
    repr_graph(a)
