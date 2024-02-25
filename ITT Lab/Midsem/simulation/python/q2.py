a = int(input("eneter a"))
b = int(input("eneter b"))
cnt = 0
for i in range(a,b):
    flg = 1
    for j in range(2,i):
        if(i%j==0):
            flg = 0
    if(flg == 1):
        cnt +=1
        print(i)