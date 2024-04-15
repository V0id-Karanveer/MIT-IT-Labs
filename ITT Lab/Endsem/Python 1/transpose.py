mat = [[1,2],[3,4]]

for i in mat:
    print(i)

m = len(mat)
n = len(mat[0])
mat2 = []
for i in range(m):
    for j in range(i+1,n):
        temp = mat[i][j]
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

for i in mat:
    print(i)




