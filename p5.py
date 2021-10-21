from Database_12K import Usuario
import collections
class Nodo:
    def __init__(self, dato):
        self.siguiente = None
        self.info = dato
    
    def verNodo(self):
        return self.info

class linkList:
    def __init__(self):
        self.prim = None
    
    def insertarNodo(self, dato):
        temp = Nodo(dato)
        sp = self.prim
        if (sp == None):
            temp.siguiente = self.prim
            sp = temp
        elif(sp.siguiente == None):
            sp.siguiente = temp
        else:
            temp.siguiente = None

    def vacia(self):
        if self.prim == None:
            return True
        else:
            return False
    
    def encontrar(self, dato):
        aux = self.prim
        k = 0
        if(aux.info[0] == dato):
            return aux
        elif(aux.siguiente.info[0] == dato):
            aux = aux.siguiente
            return aux
        while aux != None:
            aux = aux.siguiente

            
n = 100
uBase = Usuario.GetUsuariosDB(n)

def CrearTablaHash(m):
    t = []
    for i in range(m):
        a = linkList()
        t.append(a)
    
    return t

def CalcularHash(cadena, m):
    sum = 0
    for j in range(len(cadena)):
        sum += (j+1)*ord(cadena[j])
    
    p = round(1.7*m) #asignacion de valores aleatorios para calcular hash
    a = 0.9*p
    b = 0.2*p
    k = sum+i
    hash = round(((a*k+b) % p) % m) #hash por metodo universal
    return hash

def Agregar(t, key, valor):
    m = len(key)
    i = 0 # sondeo lineal
    while i < m: #calcular hash de la llave
        hash = CalcularHash(key, m)
        par = [key, valor]
        #if t[hash].vacia():
        t[hash].insertarNodo(par)
        return hash
        """else:
            t[hash].
            i += 1"""
    print("Tabla llena")

def Buscar(t, key):
    m = len(t)
    i = 0 
    hash = CalcularHash(key, len(key))
    while i < m:
        if t[hash].prim.info[0] == key:
            return CalcularHash
        else:
            t[hash].encontrar(key)
            i += 1
    return None

T = CrearTablaHash(n)

for i in range(n):
    Agregar(T, uBase[i].username, uBase[i])

Buscar(T, "race1")