l1 = [3,43,3,2,3]
n = len(l1)

for i in range(n):
    for j in range(i+1,n):
        if l1[i]>l1[j]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp

print(l1)