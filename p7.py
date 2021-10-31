import metro

class Nodo():#clase nodo, contiene nodos que conforman el grafo

	def __init__(self, nombre):#constructor de nodo
		self.nombre = nombre #atributos del nodo
		self.vecinos = []
		self.color = "blanco"
		self.distancia = -1
		self.padre = None 

	def agregarVecino(self, nodo):#metodo para agregar nodos
		for v in self.vecinos:#recorrer vecinos
			if v.nombre == nodo.nombre:#si un vecino coincide con el nombre de otro, indica que ya existe uno
				print("Ya existe el vecino "+nodo.nombre+" en el nodo "+self.nombre)
				return
		self.vecinos.append(nodo)#agrega el vecino

	def __str__(self):#metodo que da nombre
		return self.nombre

	def __repr__(self) -> str:#metodo que genera la representacion
		return self.nombre

class Grafo():#clase grafo

	def __init__(self):#constructor del grafo
		self.vertices = {}#almacena los vertices

	def agregarVertice(self, nombreNodo):#clase agregar vertices al grafo
		for v in self.vertices:#recorrer los vertices
			if v == nombreNodo:#si se encuentra imprime que ya hay un vertice
				print("Ya existe el vertice "+nombreNodo)
		nuevoNodo = Nodo(nombreNodo)#nuevo nodo
		self.vertices[nombreNodo] = nuevoNodo#agregar vertice al grafo

	def agregarArista(self, nombreNodo1, nombreNodo2):#metodo para agregar arista

		if nombreNodo1 in self.vertices:#verifica si el nodo existe en el grafo
			nodo1 = self.vertices[nombreNodo1]#agregar vertice
		else:
			print("No existe nodo con nombre "+nombreNodo1)#si no existe el nodo imprime un error
			return

		if nombreNodo2 in self.vertices:#verifica si el nodo existe en el grafo
			nodo2 = self.vertices[nombreNodo2]#agregar vertice
		else:
			print("No existe nodo con nombre "+nombreNodo2)#si no existe el nodo imprime un error
			return

		nodo1 = self.vertices[nombreNodo1]#nombra los vertices del nodo
		nodo2 = self.vertices[nombreNodo2]

		nodo1.agregarVecino(nodo2)#agrega vecinos de ambas partes
		nodo2.agregarVecino(nodo1)

	def bfs(self, nombreNodo):#metodo de busqueda por expansion
		for u in self.vertices.values():#dejar los vertices en blanco 
			u.color = "blanco"# lo que indica que no han sido visitados
			u.distancia = -1
			u.padre = None

		self.vertices[nombreNodo].color = "gris"#visitando el nodo recibido
		self.vertices[nombreNodo].distancia = 0
		self.vertices[nombreNodo].padre = None#marcado como visitado

		q = [] #cola
		q.append(self.vertices[nombreNodo]) #encolar

		while len(q) > 0:#ciclo para visitar cada uno de los vecinos de los nodos del grafo
			u = q.pop(0)#desencolar
			for v in u.vecinos:#recorrer los vecinos del nodo
				if v.color == "blanco":#si no ha sido visitado entra al ciclo
					v.color = "gris"
					v.distancia = u.distancia + 1
					v.padre = u
					q.append(v) #tenia cola
			u.color = "negro"#indica que han sido revisados todos los vecinos

	def EncontrarCaminoBFS(self, nombreNi, nombreNf):#metodo buscar camino mas corto
		for u in self.vertices.values():#dejar los vertices en blanco 
			u.color = "blanco"# lo que indica que no han sido visitados
			u.distancia = -1
			u.padre = None

		self.vertices[nombreNi].color = "gris"#visitando el nodo recibido
		self.vertices[nombreNi].distancia = 0
		self.vertices[nombreNi].padre = None#marcado como visitado

		q = [] #cola
		q.append(self.vertices[nombreNi]) #encolar

		while len(q) > 0:#ciclo para visitar cada uno de los vecinos de los nodos del grafo
			u = q.pop(0)#desencolar
			for v in u.vecinos:#recorrer los vecinos del nodo
				if v.color == "blanco":#si no ha sido visitado entra al ciclo
					v.color = "gris"
					v.distancia = u.distancia + 1
					v.padre = u
					q.append(v) #tenia cola
			u.color = "negro"#indica que han sido revisados todos los vecinos
		u = self.vertices
		est = []
		est.append(nombreNf)
		#est.insert(u[nombreNf].distancia+1, nombreNf)
		#i = u[nombreNf].distancia
		for j in est:
			if u[j].padre == None:
				break
			else:
				est.append(u[j].padre.nombre)
		imprimirBFS(est)
	
	def dfs(self, nombreNi, nombreNf):
		for u in self.vertices:
			u.color = "blanco"
			u.padre = None
		for u in self.vertices:
			if u.color == "blanco":
				self.dfsVisitar(u)
	
	def dfsVisitar(self, u):
		#t = t+1
		#u.distancia = t
		u.color = 'gris'
		for i in u.vecinos:
			if i.color == 'blanco':
				i.padre = u
				self.dfsVisitar(i)
		u.color = 'negro'
		#t = t+1


	def __str__(self):#metodo que da nombre para identificar los nodos e imprimir
		s = ''
		for v in self.vertices:#identifica a los nombres con su atributo nombre
			s += self.vertices[v].nombre + ' -> ['
			j = 0
			for i in self.vertices[v].vecinos:#recorrer vecinos 
				j += 1# contador para ultimo corchete
				if len(self.vertices[v].vecinos) == j:#ciclo para verificar si es el ultimo elemento
					s += ""+i.nombre
				else:
					s += ""+i.nombre + ','
			s += "]\n"
		return s#retornar nombre del nodo y sus vecinos

	def __repr__(self):#metodo que genera la representacion
		s = ''
		for v in self.vertices:#representando al vertice cosu atributo nombre
			s += self.vertices[v].nombre + ", "
		return s
def imprimirBFS(est):
	print("Numero de estaciones: ",len(est))
	for i in reversed(est):
		if est[0] == i:
			print(i)
		else: 
			print(i+"->", end=" ")
g = Grafo()
for u in metro.lineas:
	i = len(u)
	for j in range(i):
		g.agregarVertice(u[j])#print(u[j])
for u in metro.lineas:
	i = len(u)
	for k in range(i-1):
		g.agregarArista(u[k],u[k+1])

g.EncontrarCaminoBFS("Indios Verdes","Misterios")
