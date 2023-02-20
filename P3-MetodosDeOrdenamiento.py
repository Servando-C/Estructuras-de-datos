import random
import math #modulos necesarios para el programa
import time

def RadixSort(A): #metodo de ordenamiento radix sort
    k = max(A) #obtener elemento mayor
    d = math.floor(math.log10(k)) + 1 #obtiene el numero de digitos del numero mayor
    for i in range(d): #ordena una vuelta por cada digito
        A = CountingSortR(A, 10, i) #ordenamiento counting sort
    return A #retorna el arreglo ordenado

def CountingSortR(A, b, i): #counting sort hecho para radix
    k = b-1 #arreglo de tamaño de la base
    C = [0]*(k+1) #se llena el arreglo con ceros

    for j in range(len(A)): #
        v = A[j] #guarda el valor del arreglo original
        digito = math.floor(v / math.pow(b, i)) % b #obtiene el valor del ultimo digito
        C[digito] += 1 #aumenta 1 en C en el indice igual al valor del digito

    for j in range(1, len(C)): # suma de frecuencias
        C[j] = C[j] + C[j-1] # suma el valor del arreglo con su elemento anterior

    B = [0]*len(A) #arreglo que contendra el arreglo ordenado, inicializado en ceros
    for j in range(len(A)-1, -1, -1): #se recorre el arreglo desde atras
        v = A[j] #se guarda temporalmente el valor del arreglo original
        digito = math.floor(v / math.pow(b, i)) % b # en estas lineas se toma el valor de A compara en que
        pos = C[digito] #indice esta en C y lo coloca en B en el indice proporcionado por C
        B[pos-1] = v
        C[digito] -= 1 #disminuye 1 en la frecuencia
    return B #retorna el arreglo ordenado

def CountingSort(A): #metodo de ordenamiento Counting Sort
    #para calcular el elemento mayor
    k = max(A)

    C = [0]*(k+1) #crea un arreglo lleno de 0 del tamaño del arreglo original
    for j in range(len(A)): #recorremos el arreglo el numero de elementos de A
        v = A[j] #se guarda temporalmente el valor del arreglo original
        C[v] += 1 #se agrega 1 en el indice de C correspondiente al valor en A

    for i in range(1, len(C)): #suma de frecuencias
        C[i] = C[i] + C[i-1] # suma el valor del arreglo con su elemento anterior

    B = [0]*len(A) #arreglo que contendra el arreglo ordenado, inicializado en ceros
    for j in range(len(A)-1, -1, -1): #se recorre el arreglo desde atras
        B[C[A[j]]-1] = A[j] # en estas lineas se toma el valor de A compara en que indice esta en C y 
        C[A[j]] = C[A[j]]-1 # lo coloca en B en el indice proporcioando por C
    return B #retorna el arreglo ordenado

n = 20000 #tamaño del arreglo
arr = [] #declaracion del arreglo
x = n*10000 #valor maximo de los elemenos
for i in range(n): #genera arreglo con numeros aleatorios de tamaño n
    arr.append(random.randint(0, x)) #genera numeros entre 0 y x

a = arr[:] # se hacen tres copias del arreglo una para cada metodo
a1 = arr[:]

print("\n\nPeor caso (k =",x,")") #impresion del caso
print("n = ",n)

t1 = time.time() # toma de tiempo
CountingSort(a) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nCountingSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
RadixSort(a1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRadixSort: t = ",tf,"s") # impresion de los resultados

arr = [] #declaracion del arreglo
x = 18000 #valor maximo de los elemenos
for i in range(n): #genera arreglo con numeros aleatorios de tamaño n
    arr.append(random.randint(0, x)) #genera numeros entre 0 y x

a = arr[:] # se hacen dos copias del arreglo una para cada metodo
a1 = arr[:]

print("\n\nCaso promedio (k =",x,")") #impresion del caso
print("n = ",n)

t1 = time.time() # toma de tiempo
CountingSort(a) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nCountingSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
RadixSort(a1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRadixSort: t = ",tf,"s") # impresion de los resultados

arr = [] #declaracion del arreglo
x = 100 #valor maximo de los elemenos
for i in range(n): #genera arreglo con numeros aleatorios de tamaño n
    arr.append(random.randint(0, x)) #genera numeros entre 0 y x

a = arr[:] # se hacen dos copias del arreglo una para cada metodo
a1 = arr[:]

print("\n\nMejor caso (k =",x,")") #impresion del caso
print("n = ",n)

t1 = time.time() # toma de tiempo
CountingSort(a) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nCountingSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
RadixSort(a1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRadixSort: t = ",tf,"s") # impresion de los resultados
