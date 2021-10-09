import random #modulo random
from time import perf_counter # se utiliza para tomar el tiempo

def busquedaLinealM(arr, llave): # buesqueda lineal
    e = -1 #valor para retornar en caso de no encontrar
    for k in range(len(arr)-1): #buscar el mismo numero de elementos
        if arr[k] == llave: # si se encuentra la llave
            return k # se retorna
    return e #en caso de no encontar la llave se retorna -1
            
def busquedaLinealCentinela(arr, llave): #busqueda Lineal con Centinela
    tmp = arr[len(arr)-1]
    arr[len(arr)-1] = llave
    k = 0

    while (arr[k] != llave):
        k += 1
    arr[len(arr)-1] = tmp

    encontrado = None
    if (k < len(arr)-1 or arr[len(arr)-1] == llave):
        encontrado = k
    return encontrado

def busquedaBinaria(arr, llave, ini, fin):
    if ini > fin:
        return None

    mitad = (ini + fin) // 2
    if(llave == arr[mitad]):
        return mitad
    elif llave < arr[mitad]:
        return busquedaBinaria(arr, llave, ini, mitad-1)
    else:
        return busquedaBinaria(arr, llave, mitad+1, fin)

def BusquedaVecinos(arr, x, r, m):#funcion buscar m elementos en un radio r
    l = []
    i = 0
    while len(l) <= m and i <= len(arr)-1:
        if (abs(x-arr[i])) <= r:
            l.append(arr[i])
        i += 1
    return l

n = 1000000 #tamaño del arreglo
a = [] #arreglo
for i in range(n): #se llena el arreglo con numeros aleatorios
    a.append(random.randint(0, n/2))

a1 = a[:] # se hacen tres copias del arreglo una para cada metodo
a2 = a[:]
a3 = a[:]

a3.sort() #se ordena arreglo para BusquedaBin
llave = 10 #valor de la llave

t1 = perf_counter() #toma de tiempo
busLin = busquedaLinealM(a1, llave)
t2 = perf_counter() #toma de tiempo
tf = t2 - t1 #calculo tiempo final
print("\nBusqueda Lineal: n = ",n,", llave = ",llave," y t = ",tf," s") # impresion de los resultados

t1 = perf_counter() #toma de tiempo
busLinCen = busquedaLinealCentinela(a2, llave)
t2 = perf_counter() #toma de tiempo
tf = t2 - t1 #calculo tiempo final
print("\nBusqueda Lineal Centinela: n = ",n,", llave = ",llave," y t = ",tf," s") # impresion de los resultados

t1 = perf_counter() #toma de tiempo
busBin = busquedaBinaria(a3, llave, a3[0], a3[len(a3)-1])
t2 = perf_counter() #toma de tiempo
tf = t2 - t1 #calculo tiempo final
print("\nBusqueda Binaria: n = ",n,", llave = ",llave," y t = ",tf," s") # impresion de los resultados
"""
x = 11 #numeros a buscar cercanos
r = 5 #radio de distancia de elementos a buscar
m = 10 #numero de elementos a buscar

en = BusquedaVecinos(a, x, r, m)
for i in range(len(en)):
    print(en[i],"(r = distancia a",x,"=|",en[i],"-",x,"|=",abs(en[i]-x),")")"""