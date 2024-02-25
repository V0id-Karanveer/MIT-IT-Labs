arr = [2,3,4,5,5,8]
n = len(arr)

for i in range(0,int(n/2)):
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp

print(arr)