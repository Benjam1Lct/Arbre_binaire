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

	def dfs_prefixe(self):
		if self is not None:
			print(self.valeur)
			if self.gauche is not None: self.gauche.dfs_prefixe()
			if self.droit is not None: self.droit.dfs_prefixe()

	def dfs_infixe(self):
		if self is not None:
			if self.gauche is not None: self.gauche.dfs_infixe()
			print(self.valeur)
			if self.droit is not None: self.droit.dfs_infixe()

	def dfs_suffixe(self):
		if self is not None:
			if self.gauche is not None: self.gauche.dfs_suffixe()
			if self.droit is not None: self.droit.dfs_suffixe()
			print(self.valeur)
			
			
if __name__ == '__main__':
	a = Noeud(12)
	a.ajoute_droit(15)
	a.ajoute_droit(14)
	a.ajoute_droit(17)
	a.ajoute_gauche(8)
	a.ajoute_gauche(6)
	
	def affiche(T):
		if T != None:
			return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))
	print(affiche(a))

	a.dfs_prefixe()
	a.dfs_infixe()
	a.dfs_suffixe()


