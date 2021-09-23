import random
import math
#import numpy as np
def RadixSort(A):
    k = max(A)
    d = math.floor(math.log10(k)) + 1
    for i in range(d):
        A = CountingSortR(A, 10, i)
        print(A)
    return A

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
        B[pos] = v

        C[digito] -= 1
def CountingSort(A):
    #para calcular el elemento mayor
    k = max(A)

    C = [0]*(k+1)
    for j in range(len(A)):
        v = A[j]
        C[v] += 1
    
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    B = [0]*len(A)
    for j in range(len(A)-1, -1, -1):
        v = A[j]
        pos = C[v]
        B[pos] = v

        C[v] -= 1

n = 10
arr = []
for i in range(n):
    arr.append(random.randint(0, 10))

print("arr", arr)
arr = RadixSort(arr)
#arr = CountingSort(arr)
print(arr)