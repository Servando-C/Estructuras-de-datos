from Database_12K import Usuario
import collections
class Nodo:
    def __init__(self, dato):
        self.siguiente = None
        self.info = dato
    
    def verNodo(self):
        return self.info

class linkList(object):
    def __init__(self):
        self.prim = None
    
    def insertarNodo(self, dato):
        temp = Nodo(dato)
        temp.siguiente = self.prim
        self.prim = temp
    
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

n = 100
uBase = Usuario.GetUsuariosDB(n)

def CrearTablaHash(m):
    t = linkList*m
    return t

def CalcularHash(cadena, m, i):
    sum = 0
    aux = 0
    for i in range(len(cadena)):
        sum += (i+1)*ord(cadena[i])

    hash = round((sum + i) % 11 + (aux//10)) #hash por metodo de division
    return hash

def Agregar(t, key, valor):
    m = len(key)
    i = 0 # sondeo lineal
    while i < m: #calcular hash de la llave
        hash = CalcularHash(key, m, i)
        par = [key, valor]
        if t[hash] == []:
            t[hash] = par
            return hash
        else:
            i += 1
    print("Tabla llena")

def Buscar(t, key):
    m = len(t)
    i = 0 
    while i< m:
        if t[hash] == key:
            return CalcularHash
        elif t[hash] == None:
            return None
        else:
            i += 1
    return None

T = CrearTablaHash(n)

for i in range(n):
    Agregar(T, uBase[i].username, uBase[i])

Buscar(T, "race1")