l1 = [1,2,3,4,1]
flag = 1

for i in range(int(len(l1)/2)):
    if l1[i] != l1[len(l1)-i-1]:
        flag = 0

print(flag)