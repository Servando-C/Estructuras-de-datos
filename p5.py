def CrearTablaHash(m):
    t = [None]*m
    return t

def CalcularHash(cadena, m, i):
    sum = 0
    for i in range(len(cadena)):
        sum += (i +1)*ord(cadena[i])

    hash = (sum + i) % m #hash por metodo de division
    return hash

def Agregar(t, key):
    m = len(t)
    i = 0 # sondeo lineal
    while i < m: #calcular hash de la llave
        hash = CalcularHash(key, m, i)
        if t[hash] == None:
            t[hash] = key
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
Agregar(T, "Jesus")
