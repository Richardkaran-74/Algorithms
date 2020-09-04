def selesort(a,s):
    for i in range(s-1):
        minpos = i
        for j in range(i,s):
            if a[j] < a[minpos]:
                minpos = j
        temp = a[i]
        a[i] = a[minpos]
        a[minpos] = temp

s = int(input())
a = list(map(int, input().rstrip().split()))
selesort(a,s)
print(a)
