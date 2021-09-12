import math # se importa modulo math
import random # se importa modulo random
import time # modulo time

def BubbleSort(arr): # metodo de ordenamiento BubleSort, recibe el arreglo
    
    n = len(arr) # se obtiene la longitud del arreglo recibido
    for i in range(n): # nos aseguramos de dar 1 pasada por cada elemento del arreglo
        for j in range (n-1): # ciclo para repetir el proceso quitandole 1 a las pasadas
            if arr[j] > arr[j+1]: # si anterior es mayor que siguiente, cambio de posicion
             # se reliza el intercambio si se cumplen las condiciones
             #aux = arr[j]
             #arr[j] = arr[j+1]
             #arr[j+1] = aux
             arr[j], arr[j+1] = arr[j+1], arr[j] #sugar syntax, hace lo de las lineas 12 a 14

def BubbleSort_Mejorado(arr): # metodo de ordenamiento BubleSort mejorado, recibe el arreglo
    n = len(arr) # se obtiene la longitud del arreglo recibido
    b=1 # bandera que nos indica si hay cambios
    p=0 # no de pasadas
    while (p<(n-1) and b==1): # comprobamos que las pasadas sean menos que los elementos del arreglo-1 y 
        #                       el valor de la bandera sea el inicializado
        b=0                   # cambiamos el valor de la bandera
        for j in range (n-p-1): # a los elementos les restamos el numero de pasadas y a todo le restamos 1
                if arr[j] > arr[j+1]: # si anterior es mayor que siguiente, cambio de posicion
                 b=1
                 #intercambio
                 aux = arr[j] # se realiza el intercambio de valores ayudandonos de un auxiliar que nos guarda el
                 arr[j] = arr[j+1] #valor para ser usado despues
                 arr[j+1] = aux
        p = p+1 # se aumenta en 1 el no de pasadas

def MergeSort(arr, p, r): # metodo de ordenamiento MergeSort, recibe el arreglo, el indice inicial y el indice final
    if p < r:    # comprobamos que el indice final sea mayor que el inicial
        q = math.floor((p + r) / 2) # redondeamos hacia abajo (p+r)/2 con la funcion floor para obtener enteros
        MergeSort( arr, p, q) # llamada recursiva a la misma funcion, ahora con la primera mitad
        MergeSort( arr, q+1, r) # llamada recursiva a la misma funcion, ahora con la segunda mitad
        Merge( arr, p, q, r) # llamada a la funcion Merge para combinar los arreglos

def Merge(arr, p, q, r): # metodo para mezclar los areglos, recibe el arreglo, indice inicial, indice medio(donde se divide) e indice final
    izq = arr[p: q+1] # copia el contenido de la primera parte de la division a otro arreglo
    der = arr[q+1: r+1] # copia el contenido de la segunda parte de la division a otro arreglo

    i=0 # indices para recorrer los arreglos divididos
    j=0

    for k in range(p, r+1): # el ciclo se va a repetir el mismo numero de veces que los elementos que tenga el arreglo original
        if(j >= r-q) or ((i < q-p+1) and (izq[i] < der[j])): # si ya han pasado todos los elementos del arreglo der o si no, 
            #                                                  pero el elemento de la izquierda es menor al de la derecha agrega el elemento que contenga izq[i]
            arr[k] = izq[i] # se agrega el elemento de izq[i] en la posicion k del arreglo original
            i += 1 # se aumenta el indice de izq[i] a comparar
        else:
            arr[k] = der[j] # se agrega el elemento de der[j] en la posicion k del arreglo original
            j += 1 # se aumenta el indice de der[j] a comparar


n = 2000000 # numero de elemntos del arreglo
a = [] # a sera el arreglo generado
for i in range(n): # ciclo para generar aleatoriamente los elementos de a
    a.append(random.randint(0,10)) # los datos estaran entre 0 y 10

#a.sort(reverse=True) # se ordena la lista en orden descendente para el peor caso
#MergeSort(a,0,len(a)-1) ordenar lista, para el mejor caso

a1 = a[:] # se hacen tres copias del arreglo una para cada metodo
a2 = a[:]
a3 = a[:]

print("Caso promedio (lista aleatoria)") # dependiendo de lo requerido se comenta/quita comentario
#print("Peor caso (lista ordenada descendente)")
#print("Mejor caso (lista ordenada ascendente)")
print("Con n =",n)

#t1 = time.time() # toma de tiempo
#BubbleSort(a1) # funcion a tomar tiempo
#t2 = time.time() # toma de tiempo
#tf = t2 - t1 # obtencion del tiempo requerido para la funcion
#print("\nBubleSort: t = ",tf," s") # impresion de los resultados

#t1 = time.time() # toma de tiempo
#BubbleSort_Mejorado(a2) # funcion a tomar tiempo
#t2 = time.time() # toma de tiempo
#tf = t2 - t1 # obtencion del tiempo requerido para la funcion
#print("\nBubleSort Mejorado: t = ",tf," s") # impresion de los resultados

t1 = time.time() # toma de tiempo
MergeSort(a3, 0, len(a3)-1) # funcion a tomar tiempo
t2 = time.time() # toma de tiempo
tf = t2 - t1 # obtencion del tiempo requerido para la funcion
print("\nMergeSort: t = ",tf," s") # impresion de los resultados
