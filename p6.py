class Nodo():

	def __init__(self, nombre):
		self.nombre = nombre
		self.vecinos = []

	def agregarVecino(self, nodo):
		delf.vecinos.append(nodo)

class Grafo():

	def __init__(self):
		slf.vertices = {}

	def agregarVertice(self, nombreNodo):
		nuevoNodo = Nodo(nombreNodo)
		self.vertices[nombreNodo] = nuevoNodo

	def agregarArista(self, nodo1, nodo2):

		if nodo1 in self.vertices:
			n1 = self.vertices[nodo1]
		else:
			print("No existe nodo con nombre ",+nodo1)
			return

		if nodo2 in self.vertices:
			n2 = self.vertices[nodo2]
		else:
			print("No existe nodo con nombre ",+nodo1)
			return

		nodo1.agregarVecino(nodo2)
		nodo2.agregarVecino(nodo1)


g = Grafo()
g.agregarVertice('1')
g.agregarVertice('2')