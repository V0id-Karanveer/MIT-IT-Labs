def addnums(n,sum):
    if n==0:
        return sum
    sum = sum+n
    return addnums(n-1,sum)

print(addnums(3,0))
