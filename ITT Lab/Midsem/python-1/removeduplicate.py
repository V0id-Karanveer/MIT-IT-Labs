arr = [2,2,3,4,4,6]
res = []
for i in arr:
    if i not in res:
        res.append(i)

print(res)