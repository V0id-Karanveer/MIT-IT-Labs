def sumarr(arr,sum,n):
    if n == 0:
        return sum
    sum += arr[n-1]
    return sumarr(arr,sum,n-1)

print(sumarr([1,2,3,4],0,4))

    
