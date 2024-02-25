mat = [[3,4,5],[1,2,3],[2,5,6]]

for i in range(0,len(mat)):
    for j in range(i+1,len(mat[0])):
        temp = mat[i][j]
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

for i in range(0,len(mat)):
    print(mat[i])