arr = [ 1,2,3,3,2,1]
flg = True
for i in range(int(len(arr)/2)):
    if arr[i] != arr[len(arr)-i-1]:
        flg = False
        break

print(flg)