def shsort(myarray,n):
    g = n//2
    while g > 0:
        for x in range(g,n):
            y = myarray[x]
            z = x
            while z>=g and myarray[z-g] > y:
                myarray[z] = myarray[z-g]
                z -= g
            myarray[z] = y
        g//=2

s = int(input())
a = list(map(int, input().rstrip().split()))
length = len(a)
shsort(a,length)
print(a)