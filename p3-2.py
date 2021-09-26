import math #se importa modulo math
def RadixSort_Lex(A): #metodo de ordenamiento Radix Sort Lexicografico
    k = max(A) #maximo elemento de A
    d = len(k) #extensión del maximo elemento de A
    for i in range(len(A)): #una vuelta para cada elemento de A
        A[i] = str(A[i]).ljust(d, ' ') #agrega espacios a la derecha de acuerdo
        #                               al mayor elemento de A
    for i in range(d): #ordena una vuelta por cada letra del maximo elemento
        A = CountingSortR_L(A, 255, i) #ordenamiento counting sort
    for i in range(len(A)): #una vuelta para cada elemento de A
        A[i] = A[i].strip() #quita espacios innecesarios
    return A #retorna arreglo ordenado

def CountingSortR_L(A, b, i): #counting sort hecho para radix
    k = b-1 #arreglo de tamaño de la base
    C = [0]*(k+1) #se llena el arreglo con ceros

    for j in range(len(A)):#una vuelta para todos los elementos de A
        v = A[j] #guarda valor del arreglo original
        digito = ord(A[j][len(max(A))-1-i])#obtiene el valor del ultimo digito
        C[digito] += 1 #aumenta 1 en C en el indice igual al valor del digito
    
    for j in range(1, len(C)): # suma de frecuencias
        C[j] = C[j] + C[j-1] # suma el valor del arreglo con su elemento anterior

    B = [0]*len(A) #arreglo que contendra el arreglo ordenado, inicializado en ceros
    for j in range(len(A)-1, -1, -1): #se recorre el arreglo desde atras
        v = A[j]
        digito =  ord(A[j][len(max(A))-i-1])#en estas lineas se toma el valor de A compara en que indice esta en C y 
        pos = C[digito] # lo coloca en B en el indice proporcioando por C
        B[pos-1] = v
        C[digito] -= 1
    return B #retorna el arreglo ordenado

ar = ["Alejandro","Elizabeth","Servando","Angel","Wences",
       "Juan","Paola","Alin","Andrea","Luis"] #arreglo a ordenar
print("--Radix Sort_Lex--")
print("\nArreglo original:")
print(ar)#Impresion del arrreglo original
ar = RadixSort_Lex(ar) #llamada a funcion Radix Sort Lex
print("Arreglo ordenado:")
print(ar,"\n")#Impresion del arrreglo ya ordenado