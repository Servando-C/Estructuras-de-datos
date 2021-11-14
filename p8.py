class Nodo:
	def __init__(self, val):
		self.valor = val
		self.izq = None
		self.der = None
		self.padre = None

	def setPadre(self, nodo):
		self.padre = nodo

class abb:#arbol binario de busqueda
	def __init__(self):
		self.raiz = None
	
	def setPadre(self, nodo):
		self.padre = nodo
	
	def getRaiz(self):
		return self.raiz

	def insertar(self, k):
		if self.raiz == None:
			self.raiz = Nodo(k)
		else:
			self.agregar(k, self.raiz)

	def agregar(self, k, nodo ):
			if k < nodo.valor:
				if nodo.izq == None:
					nodo.izq = Nodo(k)
					nodo.izq.setPadre(nodo)
				else:
					self.agregar(k, nodo.izq)
			if k > nodo.valor:
				if nodo.der == None:
					nodo.der = Nodo(k)
					nodo.der.setPadre(nodo)
				else:
					self.agregar(k, nodo.der)
			if k == nodo.valor:
				print("Valor ya existente")

	def impInOrden(self, nodo = "vacio"):
		if nodo == "vacio":
			nodo = self.raiz
		if nodo != None:
			self.impInOrden(nodo.izq)
			print(nodo.valor, end = " ")
			self.impInOrden(nodo.der)

	def impPreOrden(self, nodo):
		if nodo != None:
			print(nodo.valor)
			self.impPreOrden(nodo.izq)
			self.impPreOrden(nodo.der)

	def impPostOrden(self, nodo):
		if nodo != None:
			print(nodo.valor)
			self.impPostOrden(nodo.izq)
			self.impPostOrden(nodo.der)

	def anchura(self):
		cola = []
		if self.raiz != None:
			while self.raiz != None:
				nodo = cola.pop(0)
				print(nodo.valor)
				if nodo.izq != None:
					cola.append(nodo.izq)
				if nodo.der != None:
					cola.append(nodo.der)
	
	def buscar(self, k, nodo = "vacio"):
		#s = "¿Existe ",k,"?"
		if nodo == "vacio":
			nodo = self.raiz

		if nodo != None:
			if k == nodo.valor:
				return True
			if k < nodo.valor:
				return self.buscar(k, nodo.izq)
			if k > nodo.valor:
				return self.buscar(k, nodo.der)
		else:
			return False

	def maximo (self, nodo = None):
		if nodo == None:
			nodo = self.raiz
		if nodo.der:
			return self.maximo(nodo.der)
		return nodo.valor

	def minimo (self, nodo = None):
		if nodo == None:
			nodo = self.raiz
		if (nodo.izq):
			return self.minimo(nodo.izq)
		return nodo.valor

	def getNodo(self, k):
		actual = None
		if self.raiz != None:
			actual = self.raiz
			while actual is not None and actual.valor is not k:
				if k < actual.valor:
					actual = actual.izq
				else:
					actual = actual.der
		return actual

	def cambiarNodo(self, nodo, hijo):
		if hijo != None:
			hijo.setPadre(nodo.padre)
		if nodo.padre != None:
			if nodo == nodo.padre.der:
				nodo.padre.der = hijo
			else:
				nodo.padre.izq = hijo

	def borrar (self, k):
		if self.buscar(k):
			if self.raiz != None:
				nodo = self.getNodo(k)
				if nodo != None:
					if nodo.der == None and nodo.izq == None:
						self.cambiarNodo(nodo, None)
						nodo = None
					elif nodo.der == None and nodo.izq != None:
						self.cambiarNodo(nodo, nodo.izq)
					elif nodo.der != None and nodo.izq == None:
						self.cambiarNodo(nodo, nodo.der)
					else:
						aux = self.maximo(nodo.izq)
						self.borrar(aux.valor)
						nodo.valor = aux.valor

	def limpiar (self):
		root = None

arbol = abb()
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(14)
arbol.insertar(4)
arbol.insertar(7)
arbol.insertar(13)
arbol.impInOrden()

arbol.insertar(14)
arbol.insertar(1)

arbol.minimo()
arbol.maximo()

arbol.buscar(4)
arbol.buscar(8)
arbol.buscar(13)
arbol.buscar(2)
arbol.buscar(15)

arbol.borrar(7)
arbol.impInOrden()
arbol.borrar(10)
arbol.impInOrden()
arbol.borrar(6)
arbol.impInOrden()
arbol.borrar(3)
arbol.impInOrden()
arbol.borrar(3)
arbol.impInOrden()
arbol.borrar(8)
arbol.impInOrden()

arbol.insertar(100)
arbol.impInOrden()