import random
import math
#import numpy as np

def RadixSort(A):
    k = max(A) #obtener elemento mayor
    d = math.floor(math.log10(k)) + 1 #obtiene el numero de digitos del numero mayor
    for i in range(d): #ordena una vuelta por cada digito
        A = CountingSortR(A, 10, i) #ordenamiento counting sort
    return A #retorna el arreglo ordenado

"""def RadixSort_Lex(A):
    k = max(A)
    d = len(k)
    for i in range(d): #ordena una vuelta por cada letra
        A = CountingSortR_L(A, 255, i, len(k)) #ordenamiento counting sort"""

def CountingSortR(A, b, i): #counting sort hecho para radix
    k = b-1 #arreglo de tamaño de la base
    C = [0]*(k+1) #se llena el arreglo con ceros

    for j in range(len(A)): #funcion para 
        v = A[j]
        digito = math.floor(v / math.pow(b, i)) % b #obtiene el valor del ultimo digito
        C[digito] += 1 #aumenta 1 en C en el indice igual al valor del digito
    
    for j in range(1, len(C)): # suma de frecuencias
        C[j] = C[j] + C[j-1] # suma el valor del arreglo con su elemento anterior

    B = [0]*len(A) #arreglo que contendra el arreglo ordenado, inicializado en ceros
    for j in range(len(A)-1, -1, -1): #se recorre el arreglo desde atras
        v = A[j]
        digito = math.floor(v / math.pow(b, i)) % b # en estas lineas se toma el valor de A compara en que indice esta en C y 
        pos = C[digito] # lo coloca en B en el indice proporcioando por C
        B[pos-1] = v
        C[digito] -= 1
    return B #retorna el arreglo ordenado

"""def CountingSortR_L(A, b, i, k): #counting sort hecho para radix
    k1 = b-1 #arreglo de tamaño de la base
    C = [0]*(k1+1) #se llena el arreglo con ceros
    k = k-1

    for j in range(len(A)): #funcion para 
        v = A[j]
        digito = ord(A[j][k]) #obtiene el valor del ultimo digito
        C[digito] += 1 #aumenta 1 en C en el indice igual al valor del digito
    
    for j in range(1, len(C)): # suma de frecuencias
        C[j] = C[j] + C[j-1] # suma el valor del arreglo con su elemento anterior

    B = [0]*len(A) #arreglo que contendra el arreglo ordenado, inicializado en ceros
    for j in range(len(A)-1, -1, -1): #se recorre el arreglo desde atras
        v = A[j]
        digito = math.floor(v / math.pow(b, i)) % b # en estas lineas se toma el valor de A compara en que indice esta en C y 
        pos = C[digito] # lo coloca en B en el indice proporcioando por C
        B[pos-1] = v
        C[digito] -= 1
    return B #retorna el arreglo ordenado"""

def CountingSort(A):
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

n = 200000 #tamaño del arreglo
arr = [] #declaracion del arreglo
for i in range(n): #genera arreglo con numeros aleatorios de tamaño n
    arr.append(random.randint(0, 50)) #genera numeros entre 0 y 10

print(arr)
arr = CountingSort(arr)
print(arr)
