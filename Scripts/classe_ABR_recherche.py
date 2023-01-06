from representation_arbre import *

class ABR:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def inserer(self, valeur):
        if valeur < self.valeur:
            if self.gauche == None:
                self.gauche = ABR(valeur)
            else:
                self.gauche.inserer(valeur)
        else:
            if self.droit == None:
                self.droit = ABR(valeur)
            else:
                self.droit.inserer(valeur)

    def recherche(self, cle):
        if cle < self.valeur:
            if self.gauche is None:
                return False
            else:
                return self.gauche.recherche(cle)
        elif cle > self.valeur:
            if self.droit is None:
                return False
            else:
                return self.droit.recherche(cle)
        return True

if __name__ == '__main__':
    a = ABR(15)
    liste = [12, 17, 6, 8, 19, 14]
    for elt in liste:
        a.inserer(elt)
    print(a.recherche(18))
    print(a.recherche(19))
    arbre = repr_graph(a)

