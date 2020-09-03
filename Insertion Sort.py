def isort(a):
    for x in range(1,len(a)):
        k = a[x]
        j = x -1
        while j >= 0 and k < a[j]: # K > a[j]:Descending Order
            a[j+1] = a[j]
            j -=1
        a[j+1] = k

a = [74,27,47,20]
isort(a)
print(a)