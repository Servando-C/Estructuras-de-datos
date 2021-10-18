from Database_12K import Usuario
import collections

n = 1000
uBase = Usuario.GetUsuariosDB(n)

def CrearTablaHash(m):
    t = [None]*m
    for i in range(m):
        t[i] = list()

def CalcularHash(cadena, m, i):
    sum = 0
    for i in range(len(cadena)):
        sum += (i +1)*ord(cadena[i])

    hash = (sum + i) % m #hash por metodo de division
    return hash

def Agregar(t, key, valor):
    m = len(t)
    i = 0 # sondeo lineal
    while i < m: #calcular hash de la llave
        hash = CalcularHash(key, m, i)
        par = [key, valor]
        if t[hash] == None:
            t[hash] = par
            return hash
        else:
            i += 1
    print("Tabla llena")

def Buscar(t, key):
    m = len(t)
    i 0 
    while i< m:
        if t[hash] == key:
            return CalcularHash
        elif t[hash] == None:
            return None
        else:
            i += 1
    return None

m = 10
T = CrearTablaHash(m)

for i in range(n):
    Agregar(T, uBase[i].username, uBase[i])
