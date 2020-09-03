def Bubblesort(a):
    b = len(a) -1
    swaps = 0
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1] = a[y+1],a[y]
                swaps += 1
    return a,swaps

n = int(input())
a = list(map(int, input().rstrip().split()))
sorts = Bubblesort(a)
print("The sorted Array is:", a)
print("Array is sorted in" ,sorts[1],"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])

