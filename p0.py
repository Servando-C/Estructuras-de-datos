def BubleSort_Optimizado(arr):
    b=1
    p=0
    while (p<(n-1) and b==1):
        b=0
        for j in (j<n-p):
            if(arr[j]>arr[j+1]):
                b=1
                aux=arr[j]
                a[j]=a[j+1]
                a[j+1]=aux
        p=p+1
