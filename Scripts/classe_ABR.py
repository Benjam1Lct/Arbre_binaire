from representation_arbre import *

class ABR:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.gauche

    def get_droit(self):
        return self.droit

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

if __name__ == '__main__':
    a = ABR(15)
    liste = [12, 17, 6, 8, 19, 14]
    for elt in liste:
        a.inserer(elt)
    arbre = repr_graph(a)
