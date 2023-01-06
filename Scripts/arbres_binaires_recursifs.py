def creer_arbre(r = None):
    """renvoie un arbre vide
    ou un arbre de racine r"""
    if r:
        return[r, [], []]
    else:
        return []

def arbre_vide(a):
    return a == []

def get_gauche(a):
    if not arbre_vide(a):
        return a[1]

def get_droite(a):
    if not arbre_vide(a):
        return a[2]

def insere(a, valeur):
    if arbre_vide(a):
        a.append(valeur)
        a.append([])
        a.append([])
    elif valeur <= a[0]:
        insere(a[1], valeur)
    else:
        insere(a[2], valeur)

if __name__ == "__main__":
    a = creer_arbre(12)
    insere(a, 8)
    insere(a, 6)
    insere(a, 15)
    insere(a, 14)
    insere(a, 17)
    print(a)
