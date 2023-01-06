from representation_arbre import *

class ArbreBinaire:
    """un valeur d'un arbre binaire"""
    def __init__(self, valeur, gauche = None, droit  = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit  = droit
    
    def ajoute_gauche(self, valeur):
        self.gauche = ArbreBinaire(valeur)
            
    def ajoute_droit(self, valeur):
        self.droit = ArbreBinaire(valeur)

if __name__ == '__main__':
    a = ArbreBinaire(12)
    a.ajoute_droit(15)
    a.droit.ajoute_droit(17)
    a.droit.ajoute_gauche(14)
    a.ajoute_gauche(8)
    a.gauche.ajoute_gauche(6)

    arbre = repr_graph(a)

    
