class Nodo:
	def __init__(slef, val):
		self.valor = val
		self.izq = None
		self.der = None

class abb:#arbol binario de busqueda
	def __init__(self):
		self.raiz = None

def agregar(self):
	pass

def agregar(self, k, nodo):
	if self.raiz == None:
		self.raiz = Nodo(k)
	else:
		if k < nodo.valor:
			if nodo.izq == None:
				nodo.izq = Nodo(k)
			else:
				agregar(k, nodo.izq)
		if k > nodo.valor:
			if nodo.der == None:
				nodo.der = Nodo(k)
			else:
				self.agregar(k, nodo.der)
		if k == nodo.valor:
			print("Valor ya existente")

def impInOrden(self, nodo):
	if nodo != None:
		self.impInOrden(nodo.izq)
		print(nodo.valor)
		self.impInOrden(nodo.der)

def maximo (self, nodo):
	if (nodo.der):
		return maximo(nodo.der)
	return nodo.valor

def limpiar (self):
	root = Null


arbol = abb()
arbol.agregar(10)