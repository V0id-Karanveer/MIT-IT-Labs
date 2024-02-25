mat1 = [[1,2,3],[2,3,4],[4,3,2]]
mat2 = [[3,4,5],[1,2,3],[2,5,6]]

col = int(input("no of cols?"))
row = int(input("no of rows"))

mat3 = []

for i in range(row):
    temp = []
    for j in range(col):
        
        tempinp = int(input("Enter "+str(i)+" "+str(j)))
        temp.append(tempinp)
    mat3.append(temp)

print(mat3)

mat3 = []

for i in range(row):
    temp = []
    for j in range(col):
        
        temp.append(0)
    mat3.append(temp)

print(mat3)


for i in range(3):
    for j in range(3):
        mat3[i][j] = mat1[i][j]+mat2[i][j]

print(mat3)
        
