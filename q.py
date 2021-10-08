import random
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
    for j in range(len(A)): #se recorre el arreglo desde atras
        B[C[A[j]]-1] = A[j] # en estas lineas se toma el valor de A compara en que indice esta en C y 
        C[A[j]] = C[A[j]]-1 # lo coloca en B en el indice proporcioando por C
    return B #retorna el arreglo ordenado

n = 30 #tamaño del arreglo
arr = [] #declaracion del arreglo
#x = n*10000 #valor maximo de los elemenos
for i in range(n): #genera arreglo con numeros aleatorios de tamaño n
    arr.append(random.randint(0, 100)) #genera numeros entre 0 y x

print(arr)
arr = CountingSort(arr)
print(arr)