l1 = [232,23,23,23,2,3]

for i in range(int(len(l1)/2)):
    temp = l1[i]
    l1[i] = l1[len(l1)-i-1]
    l1[len(l1)-i-1] = temp

print(l1)