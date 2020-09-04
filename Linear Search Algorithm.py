def lin_search(values,n,key):
    for x in range(0,n):
        if (values[x] == key):
            return x
    return -1

values = list(map(int, input().rstrip().split()))
key = int(input())
n = len(values)
matched = lin_search(values,n,key)
if (matched == -1):
    print("The key is Not Present")
else:
    print("The key is present:",matched+1)