import random #modulo random
from time import perf_counter # se utiliza para tomar el tiempo

def busquedaLinealM(arr, llave): # buesqueda lineal
    e = -1 #valor para retornar en caso de no encontrar
    for k in range(len(arr)-1): #buscar el mismo numero de elementos
        if arr[k] == llave: # si se encuentra la llave
            return k # se retorna
    return e #en caso de no encontar la llave se retorna -1
            
def busquedaLinealCentinela(arr, llave): #busqueda Lineal con Centinela
    tmp = arr[len(arr)-1] #ultimo elemento como temporal
    arr[len(arr)-1] = llave #sustituir ultimo elemento como la llave
    k = 0 #contador

    while (arr[k] != llave): #se comprueba que el elemento del arrelgo no sea igual a la llave
        k += 1 #indice en aumento
    arr[len(arr)-1] = tmp #encontrada la llave el ultimo elemento recupera su valor

    encontrado = None #encontrado como none en caso de no encontrarlo
    if (k < len(arr)-1 or arr[len(arr)-1] == llave):#condiciones para comprobar que se esta dentro del arreglo
        encontrado = k #iguala valor al encontrado
    return encontrado #retorna resultado

def busquedaBinaria(arr, llave, ini, fin):#busqueda binaria
    if ini > fin:#arreglo no vacio
        return None

    mitad = (ini + fin) // 2 #obtiene numero entero para la dividir el arreglo
    if(llave == arr[mitad]): #si la llave esta en la division, retorna mitad
        return mitad 
    elif llave < arr[mitad]:#si la llave esta en la primera mitad, vuelve a llamar a si misma
        return busquedaBinaria(arr, llave, ini, mitad-1)#recursividad con indicees de la primera mitad
    else: #si esta en la segunda mitad, se vuelve a llamar a si misma
        return busquedaBinaria(arr, llave, mitad+1, fin)#recursividad con indicees de la segunda mitad

def BusquedaVecinos(arr, x, r, m):#funcion buscar m elementos en un radio r
    l = [] #lista para guardar valores
    i = 0 # se usara como indice
    while len(l) <= m and i <= len(arr)-1: #mientras la lista no este llena y se permanezca dentro del indice
        if (abs(x-arr[i])) <= r: #se compara la distancia entre numros con el radio
            l.append(arr[i]) #se agrega el dato a la lista
        i += 1 #aumento el indice
    return l #retorna la lista

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
print("\nBusqueda Binaria: n = ",n,", llave = ",llave," y t = ",tf," s\n") # impresion de los resultados

x = 11 #numeros a buscar cercanos
r = 5 #radio de distancia de elementos a buscar
m = 10 #numero de elementos a buscar

en = BusquedaVecinos(a, x, r, m)
for i in range(len(en)):#imprime los datos 
    print(en[i],"(r = distancia a",x,"=|",en[i],"-",x,"|=",abs(en[i]-x),")")