l1 = [2,4,34,1,2,3,44,34]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)