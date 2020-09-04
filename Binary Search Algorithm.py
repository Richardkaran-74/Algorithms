pos =-1
def bin_search(my_list,key):
    l = 0
    r = len(my_list)-1

    while l<=r:
        middle = (l+r)//2
        if my_list[middle] == key:
            globals()['pos'] = middle
            return True
        else:
            if my_list[middle] < key:
                l = middle+1
            else:
                r = middle-1
    return False

my_list = [20,27,74, 47,42]
key = 27
if bin_search(my_list,key):
    print("The key is Present:",pos+1)
else:
    print("The key is Not Present")