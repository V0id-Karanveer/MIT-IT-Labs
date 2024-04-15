for i in range(1,50):
    if i == 2:
        print(2)
    elif i!=0 and i!=1:
        flg = 1
        for j in range(2,i):
            if i%j == 0:
                flg = 0
        if flg == 1:
            print(i)

