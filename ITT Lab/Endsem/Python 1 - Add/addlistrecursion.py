def addlist(list,n):
    if n==1:
        return list[0]
    return list[n-1] + addlist(list,n-1)

print(addlist([1,2,3,45],4))