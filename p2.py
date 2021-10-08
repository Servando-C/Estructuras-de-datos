import random
def QuickSort(arr, p, r):
    if p < r:
        q = Particionar(arr, p, r)
        QuickSort(arr, p, q-1)
        QuickSort(arr, q+1, r)

def Particionar(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return (i+1)

n = 2000
a = []
for i in range(n):
    a.append(random.randint(0,10))

print(a)
QuickSort(a, 0, len(a)-1)
print(a)