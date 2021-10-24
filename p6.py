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
				print("Ya existe el vecino "+nodo.nombre+" en el nodo "+self.nombre)
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
		for v in self.vertices:
			if v == nombreNodo:
				print("Ya existe el vertice "+nombreNodo)
		nuevoNodo = Nodo(nombreNodo)
		self.vertices[nombreNodo] = nuevoNodo

	def agregarArista(self, nombreNodo1, nombreNodo2):

		if nombreNodo1 in self.vertices:
			nodo1 = self.vertices[nombreNodo1]
		else:
			print("No existe nodo con nombre "+nombreNodo1)
			return

		if nombreNodo2 in self.vertices:
			nodo2 = self.vertices[nombreNodo2]
		else:
			print("No existe nodo con nombre ",+nombreNodo2)
			return

		nodo1 = self.vertices[nombreNodo1]
		nodo2 = self.vertices[nombreNodo2]

		nodo1.agregarVecino(nodo2)
		nodo2.agregarVecino(nodo1)

	def bfs(self, nombreNodo):


		for u in self.vertices.values():
			u.color = "blanco"
			u.distancia = -1
			u.padre = None

		self.vertices[nombreNodo].color = "gris"
		self.vertices[nombreNodo].distancia = 0
		self.vertices[nombreNodo].padre = None

		q = [] #encolar
		q.append(self.vertices[nombreNodo]) #desencolar

		while len(q) > 0:
			u = q.pop(0)
			for v in u.vecinos:
				if v.color == "blanco":
					v.color = "gris"
					v.distancia = u.distancia + 1
					v.padre = u
					q.append(v) #tenia cola
			u.color = "negro"
	
	def __str__(self):
		s = ''
		for v in self.vertices:
			s += self.vertices[v].nombre + ' -> ['
			j = 0
			for i in self.vertices[v].vecinos:
				j += 1
				if len(self.vertices[v].vecinos) == j:
					s += ""+i.nombre
				else:
					s += ""+i.nombre + ','
			s += "]\n"
		return s

	def __repr__(self):
		s = ''
		for v in self.vertices:
			s += self.vertices[v].nombre + ", "
		return s

g = Grafo()
g.agregarVertice('0')
g.agregarVertice('1')
g.agregarVertice('2')
g.agregarVertice('3')
g.agregarVertice('4')
g.agregarVertice('5')
g.agregarVertice('6')
g.agregarVertice('7')

g.agregarArista('1','2')
g.agregarArista('1','0')
g.agregarArista('1','0')
g.agregarArista('2','0')
g.agregarArista('2','3')
g.agregarArista('0','3')
g.agregarArista('3','4')
g.agregarArista('5','4')
g.agregarArista('5','6')
g.agregarArista('6','4')
g.agregarArista('9','4')

g.bfs('0')

print(g)

