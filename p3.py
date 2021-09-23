import random
import math
#import numpy as np
def RadixSort(A):
    k = max(A) #obtener elemento mayor
    d = math.floor(math.log10(k)) + 1 #obtiene el numero de digitos del numero mayor
    for i in range(d): #ordena una vuelta por cada digito
        A = CountingSortR(A, 10, i) #ordenamiento counting sort
    return A #retorna el arreglo ordenado

def CountingSortR(A, b, i): 
    k = b-1
    C = [0]*(k+1)

    for j in range(len(A)):
        v = A[j]
        digito = math.floor(v / math.pow(b, i)) % b
        C[digito] += 1
    
    for j in range(1, len(C)):
        C[j] = C[j] + C[j-1]

    B = [0]*len(A)
    for j in range(len(A)-1, -1, -1):
        v = A[j]
        digito = math.floor(v / math.pow(b, i)) % b
        pos = C[digito]
        B[pos-1] = v
        C[digito] -= 1
    return B

def CountingSort(A):
    #para calcular el elemento mayor
    k = max(A)

    C = [0]*(k+1) #crea un arreglo lleno de 0 del tamaño del arreglo original
    for j in range(len(A)): #recorremos el arreglo el numero de elementos de A
        v = A[j] 
        C[v] += 1 #en el arreglo c
    
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    B = [0]*len(A)
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1
    return B

n = 10
arr = []
for i in range(n):
    arr.append(random.randint(0, 10))

print("arr", arr)
arr = RadixSort(arr)
#arr = CountingSort(arr)
print(arr)