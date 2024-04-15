def addnum(n):
    if (n==0):
        return 0
    return n + addnum(n-1)

print(addnum(10))