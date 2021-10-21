class Nodo():

	def __init__(self, nombre):#clase nodo
		self.nombre = nombre #atributos del nodo
		self.vecinos = []
		self.color = "blanco"
		self.distancia = -1
		self.padre = None 

	def agregarVecino(self, nodo):
		for v in self.vecinos:
			if v.nombre == nodo.nombre:
				print("Nodo existente")
				return
		self.vecinos.append(nodo)

	def __str__(self):
		return self.nombre

	def __repr__(self) -> str:
		return self.nombre


class Grafo():

	def __init__(self):
		self.vertices = {}

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

	def bfs(self, nodoIni):
		for u in self.vertices.values():
			u.color = "blanco"
			u.distancia = -1
			u.padre = None

		self.vertices[nodoIni].color = "gris"
		self.vertices[nodoIni].distancia = 0
		self.vertices[nodoIni].padre = None

		q = [] #encolar
		q.append(nodoIni) #desencolar
		while len(q) > 0:
			u = q.pop()
			for v in u.vecinos:
				if v.color == "blanco":
					v.color = "gris"
					v.distancia = u.distancia + 1
					v.padre = u
					cola.append(v)
			u.color = "negro"
	
	def __str__(self):
		s = ""
		for v in self.vertices:
			s += self.vertices[v].nombre + "-"
			for i in self.vertices[v].vecinos:
				s =+ i.nombre + ","
			s += "\n"

	def __repr__(self):
		for v in self.vertices:
			s += self.vertices[v].nombre + ", "
		return s

g = Grafo()
g.agregarVertice('1')
g.agregarVertice('2')
g.agregarVertice('3')
g.agregarVertice('4')
g.agregarVertice('5')
g.agregarVertice('6')

g.agregarArista('1','1')
g.agregarArista('1','2')
g.agregarArista('1','5')

g.bsc("1")


