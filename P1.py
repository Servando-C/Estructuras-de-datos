import math
import random
def BubleSort(arr):
    
    n = len(arr)
    for i in range(n-1):
        for j in range (n-1-i):
            if arr[j] > arr[j+1]:
            #intercambio
             aux = arr[j]
             arr[j] = arr[j+1]
             arr[j+1] = aux
            #arr[j], arr[j+1] = arr[j+1], arr[j] sugar sintact

def BubleSort_Mejorado(arr):
    n = len(arr)
    b=1
    p=0
    while (p<n-1 and b==1):
        b=0
        #for i in range(n-1):
        for j in range (n-p-1):
                if arr[j] > arr[j+1]:
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


n = 1000
a = []
for i in range(n):
    a.append(random.randint(100,200))

print("Arreglo desordenado: ", a)
#MergeSort(a, 0, len(a)-1)
BubleSort_Mejorado(a)
print("Arreglo ordenado", a)