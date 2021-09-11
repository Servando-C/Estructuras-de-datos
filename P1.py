import math # se importa modulo math
import random # se importa modulo random

def BubleSort(arr): #metodo de ordenamiento BubleSort
    
    n = len(arr) # se obtiene la longitud del arreglo recibido
    for i in range(n-1): # nos aseguramos de dar n-1 pasadas
        for j in range (n-1-i): # 
            if arr[j] > arr[j+1]: # si anterior es mayor que siguiente, cambio de posicion
            # se reliza el intercambio si se cumplen las condiciones
             #aux = arr[j]
             #arr[j] = arr[j+1]
             #arr[j+1] = aux
             arr[j], arr[j+1] = arr[j+1], arr[j] #sugar syntax

def BubleSort_Mejorado(arr): # metodo de ordenamiento BubleSort mejorado
    n = len(arr) # se obtiene la longitud del arreglo recibido
    b=1 # bandera que nos indica si hay cambios
    p=0 # no de pasadas
    while (p<(n-1) and b==1): # comprobamos que las pasadas sean menos que los elemntos del arreglo-1 y 
        #                       el valor de la bandera sea el inicializado
        b=0                   # cambiamos el valor de la bandera
        for j in range (n-p-1): # a los elementos les restamos el numero de pasadas y a todo le restamos 1
                if arr[j] > arr[j+1]:
                 b=1
                 #intercambio
                 aux = arr[j]
                 arr[j] = arr[j+1]
                 arr[j+1] = aux

def MergeSort(arr, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        MergeSort( arr, p, q)
        MergeSort( arr, q+1, r)
        Merge( arr, p, q, r)

def Merge(arr, p, q, r):
    izq = arr[p: q+1]
    der = arr[q+1: r+1]

    i=0
    j=0

    for k in range(p, r+1):
        if(j >= r-q) or ((i < q-p+1) and (izq[i] < der[j])):
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1


n = 50
a = []
for i in range(n):
    a.append(random.randint(100,200))

print("Arreglo desordenado: ", a)
#MergeSort(a, 0, len(a)-1)
BubleSort_Mejorado(a)
print("Arreglo ordenado", a)