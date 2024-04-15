mat1 = [[1,2],[3,4]]
mat2 = [[2,3],[4,5]]

cols1 = len(mat1[0])
rows1 = len(mat1)

cols2 = len(mat2[0])
rows2 = len(mat2)

mat3 = [[0 for i in range(rows1)] for j in range(cols2)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            mat3[i][j]+=mat1[i][k]*mat2[k][j]

for i in mat3:
    print(i)