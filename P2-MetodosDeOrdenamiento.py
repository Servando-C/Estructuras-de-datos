import random #se importa modulo random
import time #se importa modulo time
import sys #se importa modulo sys

sys.setrecursionlimit(25000) #aumento del limite de recursion

def QuickSort(arr, p, r):
    if p < r: #se comprueba que el arreglo no este vacio
        q = Particionar(arr, p, r) #particionar arreglo
        QuickSort(arr, p, q-1) #volver a llamar Quicksort con una primera part del arreglo
        QuickSort(arr, q+1, r) #volver a llamar Quicksort con la parte restante del arreglo

def Particionar(arr, p, r):#funcion particionar
    x = arr[r] #seleccion de un pivote
    i = p-1 #contador
    for j in range(p, r): #para el rango de numeros del arreglo recibido
        if arr[j] <= x: #si elemento de j es menor que el pivote, los intercambia
            i = i+1 #aumento del contador
            arr[i], arr[j] = arr[j], arr[i] #intercambio
    arr[i+1], arr[r] = arr[r], arr[i+1] #intercambio de ultimos elementos
    return (i+1) #retorna el valor que divide al arreglo

def MaxHeapify(arr, i, tamHeap): #comprueba que se cumpla la estrcutura del Heap
    idxIzq = 2*i+1
    idxDer = 2*i+2

    idxMax = i

    if (idxIzq < tamHeap) and (arr[idxIzq] > arr[i]): #comprueba si el valor de la izquierda es mas grande
        idxMax = idxIzq #intercambia valores

    if (idxDer < tamHeap) and (arr[idxDer] > arr[idxMax]): #comprueba si el valor de la derecha es el mas grande
        idxMax = idxDer #intercambia valores

    if (idxMax != i): #hasta que el valor de i y idxMax sea igual
        arr[i], arr[idxMax] = arr[idxMax], arr[i]
        MaxHeapify(arr, idxMax, tamHeap) #comprueba que la estructura cumpla, debido a que pueden quedar elementos 
        #que no cumplan con la estructura

def construirHeapMaxIni(arr): #construye Heap de acuerdo al tamaño de arr
    tamHeap = len(arr) # obtencion tamaño del Heap
    for i in range((tamHeap - 1) // 2, -1, -1): # se recorre el areglo hacia atras 
        MaxHeapify(arr, i, tamHeap) #

def HeapSort(arr): #estrcutur de datos Heap Sort
    construirHeapMaxIni(arr) #funcion para construir
    tamHeap = len(arr) # obtencion tamaño del Heap
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # se recorre el areglo hacia atras 
        tamHeap -= 1 #disminucion tamaño del heap
        MaxHeapify(arr, 0, tamHeap) #se asegura que el nuevo heap formado cumpla con la estrcutura

def Random_Quicksort(arr, p, r): #funcion quicksort con pivote random
    if(p < r): #se comprueba que el arreglo no este vacio
        q = Particionar_Rand(arr, p, r) #particionar arreglo
        Random_Quicksort(arr, p, q-1)  #volver a llamar Quicksort con una primera part del arreglo
        Random_Quicksort(arr, q+1, r)  #volver a llamar Quicksort con la parte restante del arreglo

def Particionar_Rand(arr, p, r): #particionar con pivote random
    randpivot = random.randrange(p, r) # obtencion de un pivote random
    arr[p], arr[randpivot] = arr[randpivot], arr[p] #intercambio de valores tal que el pivote quede en la primera posicion
    return Particionar(arr, p, r) #retorna el valor resultado de particionar

n = 5000 #numero de elementos del arreglo
a = []
for i in range(n):#se llena el arreglo con valores entre 0 y 10
    a.append(random.randint(0,10))

arr = a[:] #copias de los arreglos
arr1 = a[:]
arr2 = a[:]

print("Peor caso\n")

arr.sort(reverse=True)#ordenamiento del arreglo inversamente
arr1_1 = arr[:]
arr1_2 = arr[:]
arr1_3 = arr[:]

t1 = time.time() # toma de tiempo
QuickSort(arr1_1,0, len(arr)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nQuickSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
Random_Quicksort(arr1_2,0, len(arr)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRandom Quicksort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
HeapSort(arr1_3) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nHeap Sort: t = ",tf,"s") # impresion de los resultados

print("\nCaso promedio")

arr2_1 = arr1[:]
arr2_2 = arr1[:]
arr2_3 = arr1[:]

t1 = time.time() # toma de tiempo
QuickSort(arr2_1, 0, len(arr1)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nQuickSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
Random_Quicksort(arr2_2, 0, len(arr1)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRandom Quicksort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
HeapSort(arr2_3) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nHeap Sort: t = ",tf,"s") # impresion de los resultados

print("\nMejor caso")

arr2.sort()# ordenamiento del arreglo
arr3_1 = arr2[:]
arr3_2 = arr2[:]
arr3_3 = arr2[:]

t1 = time.time() # toma de tiempo
QuickSort(arr3_1, 0, len(arr2)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nQuickSort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
Random_Quicksort(arr3_2, 0, len(arr2)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nRandom Quicksort: t = ",tf,"s") # impresion de los resultados

t1 = time.time() # toma de tiempo
HeapSort(arr3_3) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nHeap Sort: t = ",tf,"s") # impresion de los resultados
