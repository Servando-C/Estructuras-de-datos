import random
def busquedaLinealM(arr, llave):
    e = -1
    for k in range(len(arr)-1):
        if arr[k] == llave:
            return k
    return e
            
def busquedaLinealCentinela(arr, llave):
    tmp = arr[len(arr)-1]
    arr[len(arr)-1] = llave
    k = 0

    while (arr[k] != llave):
        k += 1
    arr[len(arr)-1] = tmp

    encontrado = None
    if (k < len(arr)-1 or arr[len(arr)-1] == llave):
        encontrado = k
    return encontrado

def busquedaBinaria(arr, llave, ini, fin):
    if ini > fin:
        return None

    mitad = (ini + fin) // 2
    if(llave == arr[mitad]):
        return mitad
    elif llave < arr[mitad]:
        return busquedaBinaria(arr, llave, ini, mitad-1)
    else:
        return busquedaBinaria(arr, llave, mitad+1, fin)


n = 10
a = []
for i in range(n):
    a.append(random.randint(0, 10))

a.sort()
print (a)
llave = 10
#encontrado = busquedaLinealCentinela(a, llave)
encontrado = busquedaBinaria(a, llave, a[0], a[len(a)-1])
print("llave:",llave,"encontrada en:",encontrado)