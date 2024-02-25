mat1 = [[1,2,3],[2,3,4],[4,3,2]]
mat2 = [[3,4,5],[1,2,3],[2,5,6]]

rows1 = len(mat1)
cols2 = len(mat2[0])
cols1 = len(mat1[0])
result = []

for i in range(rows1):
    result.append([])
    for j in range(cols2):
        result[i].append(0)

print(result)

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += mat1[i][k]*mat2[k][j]

for i in range(rows1):
    print(result[i])


