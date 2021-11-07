import metro#utilizacion del codigo que contiene las lineas del metro

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
			if v == nombreNodo:#si se encuentra ya no agrega nada
				break
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

	def bfs(self, nombreNi):#metodo buscar camino mas corto
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
	
	def imprimirRutaBFS(self, nombreNi, nombreNf):#metodo imprimir ruta usando BFS
		self.bfs(nombreNi)#utilizar metodo bfs
		u = self.vertices#igualar a u para iterar sobre los vertices
		est = []#lista para guardar estaciones de la ruta
		est.append(nombreNf)#agregar la estacion final
		for j in est:#iterar sobre los padres de los elementos de la ruta
			if u[j].padre == None:#se detiene si el padre del vertice no existe
				break
			else:
				est.append(u[j].padre.nombre)#agregar el padre a la lista de estaciones
		imprimir(est)#llama al metodo para imprimir las estaciones

	def dfs(self, nombreNi):#metodo dfs
		for u in self.vertices.values():#iterar sobre los vertices y dejarlos como no visitados
			u.color = "blanco"
			u.padre = None
		nombreNi = self.vertices[nombreNi]#tomar el nodo inicial
		self.dfsVisitar(nombreNi)#metodo para visitar vecinos del nodo inicial
	
	def dfsVisitar(self, u):#metodo para visitar vertices
		u.color = 'gris'#marcar como visitado
		for i in u.vecinos:#iterar sobre los vecinos del nodo inicial
			if i.color == 'blanco':#si no se ha visitado
				i.padre = u#hacer predecesor al vertice ingresado
				self.dfsVisitar(i)#visitar el vertice actual
		u.color = 'negro'#marcar como visitado y todos sus vecinos visitados

	def imprimirRutaDFS(self, nombreNi, nombreNf):#metodo imprimir ruta usando DFS
		self.dfs(nombreNi)#utilizar metodo DFS
		u = self.vertices#igualar a u para iterar sobre los vertices
		est = []#lista para guardar estaciones de la ruta
		est.append(nombreNf)#agregar la estacion final
		for j in est:#iterar sobre los padres de los elementos de la ruta
			if u[j].padre == None:#se detiene si el padre del vertice no existe
				break
			else:
				est.append(u[j].padre.nombre)#agregar el padre a la lista de estaciones
		imprimir(est)#llama al metodo para imprimir las estaciones

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
		
def imprimir(est):#metodo para imprimir las listas de estaciones
	print("\nDe",est[len(est)-1], "a",est[0])#mensaje de estaciones inicio y final
	print("\nNumero de estaciones: ",len(est))#imprimir numero de estaciones
	for i in reversed(est):#iterar en la lista de reversa
		if est[0] == i:#incluye una impresion para cuando se refiera al ultimo elemento 
			print(i)
		else:
			print(i+" ->", end=" ")#si es un elemento intermedio imprime una flecha entre las estaciones

g = Grafo()#generar un nuevo grafo
for u in metro.lineas:#iterar sobre las lineas del metro
	i = len(u)#longiud de la linea actual
	for j in range(i):#iterar lineas mientras este en el numero de estaciones
		g.agregarVertice(u[j])#agregar estacion
for u in metro.lineas:#iterar entre las lineas del metro
	i = len(u)#longiud de la linea actual
	for k in range(i-1):#toma hasta la penultima estacion ligada a la ultima
		g.agregarArista(u[k],u[k+1])#agregar aristas entre la estacion y la siguiente
print("\nBFS:")
g.imprimirRutaBFS("Aquiles Serdán","Iztapalapa")#imprimir la ruta entre las estaciones usando bfs
print("\nDFS:")
g.imprimirRutaDFS("Aquiles Serdán","Iztapalapa")#imprimir la ruta entre las estaciones usando dfs
print("\nBFS:")
g.imprimirRutaBFS("San Antonio","Aragón")
print("\nDFS:")
g.imprimirRutaDFS("San Antonio","Aragón")
print("\nBFS:")
g.imprimirRutaBFS("Vallejo","Insurgentes")
print("\nDFS:")
g.imprimirRutaDFS("Vallejo","Insurgentes")