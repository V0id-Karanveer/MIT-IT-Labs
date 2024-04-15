m = int(input("no of cols"))
n = int(input("no of rows"))

mat1 = []
mat2 = []

for i in range(m):
    temp = []
    temp2 = []
    for j in range(n):
        temp.append(int(input("enter1 "+str(i)+" "+str(j))))
        temp2.append(int(input("enter2 "+str(i)+" "+str(j))))
    mat1.append(temp)
    mat2.append(temp2)

print(mat1)
print(mat2)

mat3 = [[0 for i in range(m)] for j in range(n)]

for i in range(m):
    for j in range(n):
        mat3[i][j] = mat1[i][j]+mat2[i][j]

for i in mat3:
    print(i)